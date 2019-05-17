import os
import pathlib
import struct
import sys

from setuptools import setup

from distutils.extension import Extension
from Cython.Build import cythonize

# System info
platform = sys.platform
arch = struct.calcsize('P') * 8

# Paths
cwd = pathlib.Path('.')
readme_path = cwd / 'README.md'
extension_path = cwd / 'copus'
binary_path = extension_path / 'bin' / f'x{arch}'

def normalize(path_list, relative_to=None):
    """
    Converts a list of pathlib.Paths into a list of strings relative to a directory.
    """

    relative_to = relative_to or cwd
    return [(relative_to / x).as_posix() for x in path_list]

# Compile options
include_dirs = [cwd, extension_path]
library_dirs = [binary_path]
runtime_lib_dirs = [binary_path]
extra_compile_args = ['-O2', '-march=native']
extra_link_args = ['-O2', '-march=native']

compiler_directives = {
    'language_level': 3
}
libraries = {
    'win32': ['opus'],
    'linux': ['opus']
}

# Platform tweaks
if platform == 'win32':
    include_dirs.append(cwd / 'include')
    runtime_lib_dirs = []

    if arch == 64:
        extra_compile_args.append('-DMS_WIN64')

# Package setup
with open(readme_path, 'r', encoding='utf-8') as fp:
    README = fp.read()

setup(
    name='discord-ext-copus',
    author='imayhaveborkedit',
    url='https://github.com/imayhaveborkedit/discord-ext-copus',

    license='MIT',
    description='Cython bindings of libopus for discord.py',
    long_description=README,
    long_description_content_type='text/markdown',
    project_urls={
        'Code': 'https://github.com/imayhaveborkedit/discord-ext-copus',
        'Issue tracker': 'https://github.com/imayhaveborkedit/discord-ext-copus/issues'

    },

    version='0.0.1',
    python_requires='>=3.6.0',
    setup_requires=['Cython==0.27.3'],
    zip_safe=False,

    packages=['discord.ext.copus'],
    package_dir={'discord.ext.copus': 'copus'},
    provides=['discord.ext.copus'],

    ext_modules = cythonize([
        Extension(
            'discord.ext.copus._copus',
            normalize([
                '_copus.pyx',
            ], extension_path),
            libraries=libraries[platform],
            include_dirs=normalize(include_dirs),
            library_dirs=normalize(library_dirs),
            extra_compile_args=extra_compile_args,
            extra_link_args=extra_link_args,
            runtime_library_dirs=normalize(runtime_lib_dirs))
        ],
        nthreads=3,
        annotate=True,
        compiler_directives=compiler_directives
    )
)
