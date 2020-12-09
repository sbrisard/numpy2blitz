import configparser

import pybind11
import setuptools



def pybind11_extension(module_name, metadata):
    return setuptools.Extension(
        ".".join([metadata["name"], module_name]),
        include_dirs=[pybind11.get_include(), metadata["scapin_include_dir"]],
        sources=[os.path.join(metadata["name"], module_name + ".cpp")],
        # TODO: Check that this is necessary
        define_macros=[
            ("__SCAPIN_VERSION__", r"\"" + metadata["version"] + r"\""),
            ("__SCAPIN_AUTHOR__", r"\"" + metadata["author"] + r"\""),
            ("_USE_MATH_DEFINES", ""),
        ],
    )


if __name__ == "__main__":
    numpy2blitz = setuptools.Extension("numpy2blitz",
                                       include_dirs=[pybind11.get_include()],
                                       sources=["numpy2blitz.cpp"])
    setuptools.setup(
        name="numpy2blitz",
        ext_modules=[numpy2blitz],
    )
