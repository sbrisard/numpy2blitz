#define _USE_MATH_DEFINES

#include <cmath>
#include <complex>

#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(numpy2blitz, m) {
  m.doc() = "Example of numpy/blitz interoperability through pybind11.";

  m.attr("__version__") = "1.0";
  m.attr("__author__") = "S. Brisard";

  m.def("add", &add, "A function which adds two numbers");
}
