from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    values, counts = np.unique(x, return_counts=True)
    mean=float(np.mean(x))
    median=float(np.median(x))
    mode = float(values[np.argmax(counts)])

    return {"mean": mean,"median": median,"mode":mode}
    pass