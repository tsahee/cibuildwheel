import os
import platform

from setuptools import (
    Extension,
    setup,
)

standard = os.environ["STANDARD"]

if platform.system() == 'Windows':
    extra_compile_args = ["/std:c++" + standard, '/DSTANDARD' + standard]

    if standard == '17':
        extra_compile_args.append("/wd5033")
else:
    extra_compile_args = ["-std=c++" + standard, "-DSTANDARD=" + standard]
    
    if standard == "17":
        extra_compile_args.append("-Wno-register")

setup(
    name="spam",
    ext_modules=[Extension('spam', sources=['spam.cpp'], language="c++", extra_compile_args=extra_compile_args)],
    version="0.1.0",
)
