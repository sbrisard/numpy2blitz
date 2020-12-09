# numpy2blitz

An example of numpy ↔ blitz++ interoperability through pybind11


## Installation

Create a file `setup.cfg` alongside the `setup.py` file. Edit this file as follows

```
[blitz]
include_dir = ...
```

where the “...” should be replaced with the full path to the `blitz`
headers. For example, is `blitz/array.h` is located at
`C:\opt\blitz-1.0.2\include\blitz\array.h`, then use the following description

```
[blitz]
include_dir = C:\opt\blitz-1.0.2\include
```

Then, to install locally

```
python setup.py install --user
```

## What this module does

This is a very simple demo of numpy ↔ blitz++ interoperability. The C++
extension is called from python with a numpy array. This array is converted
internally to a blitz++ array and altered. The changes affect the original numpy
array. This is illustrated by the `demo.py` python script

```
(base) PS C:\Users\nemo> python .\demo.py
I'm a numpy array
[[1. 2. 3.]
 [4. 5. 6.]]
-----
Now, I'm a blitz array
(0,1) x (0,2)
[ 1 2 3
  4 5 6 ]

I'm still a blitz array (but I've changed)
(0,1) x (0,2)
[ 1 1 1
  1 1 1 ]

-----
I'm a numpy array again (and I've changed)
[[1. 1. 1.]
 [1. 1. 1.]]
```

To do this, we use

- The [pybind11/numpy.h](https://pybind11.readthedocs.io/en/latest/advanced/pycpp/numpy.html#numpy) library. In particular, the method `mutable_data()` is useful.
- The ability to create blitz++ arrays from existing data (see §2.3.7 of the
  blitz++ docs). **It is essential to use the `blitz::neverDeleteData` option!**.

<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- End: -->
