import numpy as np
import numpy2blitz

if __name__ == "__main__":
    a = np.array([[1., 2., 3.], [4., 5., 6.]])
    print("I'm a numpy array")
    print(a)
    numpy2blitz.dummy(a)

    print("I'm a numpy array again (and I've changed)");
    print(a)
