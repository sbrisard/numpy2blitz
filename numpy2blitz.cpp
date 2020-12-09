#define _USE_MATH_DEFINES

#include <cmath>
#include <complex>

#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>

#include "blitz/array.h"

void dummy(blitz::Array<double, 2> &a) {
  std::cout << "-----" << std::endl;
  std::cout << "Now, I'm a blitz array" << std::endl;
  std::cout << a << std::endl;
  std::cout << "I'm still a blitz array (but I've changed)" << std::endl;
  a = 1.0;
  std::cout << a << std::endl;
  std::cout << "-----" << std::endl;
}

blitz::Array<double, 2> numpy2blitz(pybind11::array_t<double, pybind11::array::c_style> &a) {
  if (a.ndim() != 2) {
    std::cerr << "I can only handle matrices" << std::endl;
  }
  blitz::TinyVector<int, 2> shape{int(a.shape(0)), int(a.shape(1))};
  blitz::Array<double, 2> a_blitz{
    a.mutable_data(),
    blitz::shape(a.shape(0), a.shape(1)),
    blitz::neverDeleteData};
  return a_blitz;
}

PYBIND11_MODULE(numpy2blitz, m) {
  m.doc() = "Example of numpy/blitz interoperability through pybind11.";

  m.attr("__version__") = "1.0";
  m.attr("__author__") = "S. Brisard";

  m.def("dummy", [](pybind11::array_t<double, pybind11::array::c_style> &a){
    dummy(numpy2blitz(a));
  });
}
