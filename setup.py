#!/usr/bin/env python3

import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

setup(
    ext_modules=[
        Pybind11Extension(
            'pytomlpp._impl',
            ['src/pytomlpp.cpp', 'src/type_casters.cpp', 'src/encoding_decoding.cpp', *glob.glob('third_party/**/*.cpp', recursive=True), *glob.glob('external/**/*.cpp', recursive=True)],
            include_dirs=[
                'include',
                'third_party',
            ],
			cxx_std=17,
        ),
    ],
)
