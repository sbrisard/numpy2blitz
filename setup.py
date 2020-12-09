import configparser
import pybind11
import setuptools

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("setup.cfg")
    blitz_include_dir = config["blitz"].get("include_dir", "")

    numpy2blitz = setuptools.Extension("numpy2blitz",
                                       include_dirs=[pybind11.get_include(),
                                                     blitz_include_dir],
                                       sources=["numpy2blitz.cpp"])
    setuptools.setup(
        name="numpy2blitz",
        ext_modules=[numpy2blitz],
    )
