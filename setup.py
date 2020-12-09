import pybind11
import setuptools

if __name__ == "__main__":
    numpy2blitz = setuptools.Extension("numpy2blitz",
                                       include_dirs=[pybind11.get_include()],
                                       sources=["numpy2blitz.cpp"])
    setuptools.setup(
        name="numpy2blitz",
        ext_modules=[numpy2blitz],
    )
