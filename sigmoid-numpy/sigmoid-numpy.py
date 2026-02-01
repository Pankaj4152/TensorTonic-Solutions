import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    if x.ndim==0:
        x = x.reshape(1)
    return 1/(1+np.exp(-x))