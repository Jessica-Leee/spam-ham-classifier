"""Exercise only the recovered feature functions on synthetic text; no training."""
from pathlib import Path
import ast
import importlib.util
import json
import re

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def main():
    spec = importlib.util.spec_from_file_location("archive_helper", ROOT / "notebooks/projB2_utils.py")
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    actual = helper.words_in_texts(["hello", "bye", "world"], pd.Series(["hello", "hello worldhello"]))
    assert np.array_equal(actual, [[1, 0, 0], [1, 0, 1]])

    notebook = json.loads((ROOT / "notebooks/projB2.ipynb").read_text())
    source = next("".join(c["source"]) for c in notebook["cells"]
                  if c["cell_type"] == "code" and "def refined_features_extraction" in "".join(c["source"]))
    parsed = ast.parse(source)
    # Load just the fixed keyword list and two feature functions, not fit/predict calls.
    nodes = [node for node in parsed.body
             if isinstance(node, ast.FunctionDef)
             or (isinstance(node, ast.Assign)
                 and any(isinstance(t, ast.Name) and t.id == "words" for t in node.targets))]
    scope = {"np": np, "pd": pd, "re": re}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), "recovered-feature-functions", "exec"), scope)
    examples = pd.DataFrame({"email": ["URGENT cash!", "hello world", None],
                             "subject": ["WINNER!", "hello", None]})
    features = scope["refined_features_extraction"](examples)
    assert features.shape == (3, 24)
    assert np.isfinite(features.to_numpy()).all()
    assert features.loc[0, "body_urgent_exist"] == 1
    assert features.loc[0, "num_exclamations_body"] == 1
    assert features.loc[2, "body_word_count"] == 0
    print("Synthetic feature checks passed: B1 substring matrix; B2 24 finite features and missing-text handling.")
    print("No emails from the course dataset were loaded, and no model was fitted.")


if __name__ == "__main__":
    main()
