# Data and runtime dependencies

The recovered notebooks expect `spam_ham_data.zip` in their working directory and read `train.csv` and `test.csv` directly from it. The course describes 8,348 labeled training examples and 1,000 unlabeled test examples, with spam labeled `1` and ham labeled `0`. The corpus contains actual historical emails, so raw saved email previews have been removed from this archive.

## Obtain the matching Fall 2024 data

1. Open the official [DS-100/fa24-student B2 data file](https://github.com/DS-100/fa24-student/blob/main/proj/projB2/spam_ham_data.zip).
2. Use GitHub's **Download raw file** action.
3. Save it as `notebooks/spam_ham_data.zip`, beside both project notebooks. Leave it zipped.

The official B1 and B2 directories reference the same 11,654,380-byte ZIP. Its Git blob SHA-1 is `8ef17e6372785d3d654105a95acf671d6d453f50` (this is Git's blob identifier, not a plain file SHA-256). This was checked from the official repository listing; the archive was not downloaded during preparation.

The [B1 official materials](https://github.com/DS-100/fa24-student/tree/main/proj/projB1) and [B2 official materials](https://github.com/DS-100/fa24-student/tree/main/proj/projB2) provide course context. Although the underlying corpus is associated with SpamAssassin, downloading a different raw public corpus does not reproduce this course's cleaned CSVs, labels, or split.

The official [Fall 2024 Data 100 course schedule](https://ds100.org/fa24/) identifies these assignments as Project B1: Spam & Ham I and Project B2: Spam & Ham II. Use that archived offering and its official public materials, rather than another semester's data.

The archive deliberately does not bundle the email dataset, a replacement toy dataset, a fitted estimator, or prediction CSVs. Existing saved plots and aggregate metrics remain available in the notebooks.

## Runtime packages

`requirements.txt` lists the packages imported by the retained notebooks: NumPy, pandas, Matplotlib, seaborn, scikit-learn, and IPython, plus JupyterLab to open them. Exact historical package versions were not embedded in the submissions. No packages were installed during preparation.

The original official B2 directory supplies `projB2_utils.pyc` rather than a `.py` source file. To avoid a Python-bytecode version dependency, the archive includes a readable `.py` helper using the owner's recovered B1 `words_in_texts` function unchanged. No upstream bytecode was executed or decompiled.

Instructional precision/recall figures link to their verified official upstream image paths; those optional course reference images require network access. The student's saved charts, including the recorded ROC figure, remain embedded locally.
