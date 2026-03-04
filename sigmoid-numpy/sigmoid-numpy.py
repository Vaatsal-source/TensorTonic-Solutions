import numpy as np
import math 

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    result = 1 / (1 + np.exp(-np.array(x)))
    return result
    pass