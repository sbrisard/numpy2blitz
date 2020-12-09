# numpy2blitz
An example of numpy ↔ blitz++ interoperability through pybind11


## Installation

Create a file `setup.cfg` alongside the `setup.py` file. Edit this file as follows

```
[blitz]
include_dir = ...
```

where the “...” should be replaced with the full path to the `blitz` headers. For example, is `blitz/array.h` is located at `C:\opt\blitz-1.0.2\include\blitz\array.h`, then use the following description

```
[blitz]
include_dir = C:\opt\blitz-1.0.2\include
```

Then, to install locally

```
python setup.py install --user
```

<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- End: -->
