# Validation record

## Checks completed

- Parsed both notebook JSON files and checked retained output structure.
- Parsed all **41 retained code cells** with Python's `ast.parse`: B1 has 18, B2 has 23. Also parsed the readable compatibility helper.
- Verified the retained notebooks contain no email-address literal or Otter grading/export call.
- Checked the original student implementation/model cells against the recovered originals; they are unchanged.
- Decoded embedded PNG output and inspected the saved ROC figure. Its legend displays **AUC = 0.90**, computed on training predictions in the source code.
- Ran only the recovered feature functions on synthetic text using available local NumPy/pandas: B1's substring-indicator example matched; B2 produced 24 finite numeric features and handled missing text. No course emails were loaded and no classifier was fitted.

## Recorded model facts

The B1 five-word model uses `drug`, `bank`, `prescription`, `memo`, and `private`, with `LogisticRegression()` and saved training accuracy `0.7576201251164648`. Its recorded confusion counts are TP 219, TN 5473, FP 122, FN 1699; rounded precision is 0.64, recall 0.11, and false-positive rate 0.02.

B2 creates 12 keyword-presence columns and 12 numeric text features, then fits `LogisticRegression(max_iter=500)`. Saved training accuracy is `0.8860641554638626`. The fitting output includes an `lbfgs` iteration-limit convergence warning. The `pipeline` variable is that estimator alone; there is no actual scaling pipeline, fitted PCA, grid search, or cross-validation in the final submitted code. A validation split is created but no final-model validation score is reported. No exact held-out test accuracy is established by the notebook outputs.

## Preserved limitations

The complete notebooks were not executed during preparation. The original dataset was absent, and the available local runtime did not contain the complete model/plotting environment. Requirements list the necessary packages without guessed historical version pins. The B1 notebook also retains a coefficient assertion whose outcome may depend on the historical scikit-learn environment.

The B2 written explanation mentions `StandardScaler`, but the implementation does not apply it. Its keyword list contains `Bonus` and `Project`, while the matching code lowercases the body text without lowercasing those keywords; those two features therefore do not match as written. These original details were preserved rather than silently corrected or presented as improvements.

All listed accuracies and the ROC figure are retained historical outputs. Syntax checks and synthetic feature checks do not establish model generalization, a new test-set result, or numerical reproducibility of the original execution.
