import os
import shutil
import struct
import sys

from os.path import normpath as norm

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'discord', 'ext', 'copus'))

# System info
platform = sys.platform
arch = struct.calcsize('P') * 8

# Defaults
bindir = norm(os.path.join(os.path.abspath('.'), 'bin', f'x{arch}'))

include_dirs = []
library_dirs = [bindir]
runtime_lib_dirs = [bindir]
extra_compile_args = ['-O2', '-march=native']
extra_link_args = ['-O2', '-march=native']

compiler_directives = {
    'language_level': 3
}
libraries = {
    'win32': ['opus-0'],
    'linux': ['opus']
}

# Platform tweaks
if platform == 'win32':
    include_dirs.append(norm('D:/MinGW/include'))
    library_dirs.append(norm('D:/MinGW/lib'))

    if arch == 64:
        extra_compile_args.append('-DMS_WIN64')

setup(
    ext_modules = cythonize([
        Extension(
            "_copus",
            ["_copus.pyx"],
            libraries=libraries[platform],
            include_dirs=include_dirs,
            library_dirs=library_dirs,
            extra_compile_args=extra_compile_args,
            extra_link_args=extra_link_args,
            runtime_library_dirs=runtime_lib_dirs)
        ],
        nthreads=3,
        annotate=True,
        compiler_directives=compiler_directives)
)

shutil.rmtree("./build")
