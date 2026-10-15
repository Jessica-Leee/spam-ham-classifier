"""Archive compatibility helper for DATA C100 Fall 2024 Project B2.

The function below is copied verbatim from the owner's recovered Project B1
answer. It replaces reliance on the upstream Python 3.11-specific .pyc helper.
It is binary substring-presence featurization, not tokenization.
"""
import numpy as np

def words_in_texts(words, texts):
    """
    Args:
        words (list): Words to find.
        texts (Series): Strings to search in.
    
    Returns:
        A 2D NumPy array of 0s and 1s with shape (n, d) where 
        n is the number of texts, and d is the number of words.
    """
    indicator_array = np.array([[1 if word in text else 0 for word in words] for text in texts])
    
    return indicator_array
