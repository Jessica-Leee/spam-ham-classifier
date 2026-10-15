"""Parse every retained code cell without executing notebooks or requiring data."""
from pathlib import Path
import ast
import base64
import json
import re

ROOT = Path(__file__).resolve().parents[1]
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def main():
    total = 0
    for path in sorted((ROOT / "notebooks").glob("*.ipynb")):
        notebook = json.loads(path.read_text())
        assert notebook["nbformat"] == 4
        assert "otter" not in notebook.get("metadata", {})
        count = 0
        for index, cell in enumerate(notebook["cells"]):
            source = "".join(cell.get("source", []))
            if cell["cell_type"] == "code":
                ast.parse(source, filename=f"{path.name}:cell-{index}")
                assert "grader.check(" not in source and "grader.export(" not in source
                assert not any(line.lstrip().startswith(("%", "!")) for line in source.splitlines())
                count += 1
                for output in cell.get("outputs", []):
                    kind = output["output_type"]
                    if kind == "stream":
                        assert "metadata" not in output and "name" in output and "text" in output
                    elif kind in {"execute_result", "display_data"}:
                        assert "data" in output and "metadata" in output
                        if "image/png" in output["data"]:
                            image = base64.b64decode(output["data"]["image/png"])
                            assert image.startswith(b"\x89PNG\r\n\x1a\n")
                    elif kind == "error":
                        assert "ename" in output and "evalue" in output and "traceback" in output
                    else:
                        raise AssertionError(f"Unknown output type: {kind}")
        # Raw-email saved previews were removed; no address literal should remain.
        assert not EMAIL.search(path.read_text()), f"Email address literal remains in {path.name}"
        print(f"{path.name}: {count} code cells parsed; output structure and privacy checks passed")
        total += count
    helper = ROOT / "notebooks" / "projB2_utils.py"
    ast.parse(helper.read_text(), filename=str(helper))
    print(f"Total: {total} code cells and the compatibility helper parsed. No notebook was executed.")


if __name__ == "__main__":
    main()
