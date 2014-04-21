from distutils.core import setup
from distutils.extension import Extension

import glob

sources = ['pycrfsuite/pycrfsuite.cpp']

# crfsuite
sources += glob.glob('crfsuite/lib/crf/src/*.c')
sources += glob.glob('crfsuite/swig/*.cpp')

sources += ['crfsuite/lib/cqdb/src/cqdb.c']
sources += ['crfsuite/lib/cqdb/src/lookup3.c']

# lbfgs
sources += glob.glob('liblbfgs/lib/*.c')

includes = [
    'crfsuite/include/',
    'crfsuite/lib/cqdb/include'
]

ext_modules = [Extension('pycrfsuite/pycrfsuite',
    include_dirs=includes,
    language='c++',
    sources=sources
)]

setup(
    name='pycrfsuite',
    version="0.0.1",
    description="Python CRFsuite binding",
    author="Terry Peng",
    author_email="pengtaoo@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
    packages=['pycrfsuite'],
    ext_modules=ext_modules
)