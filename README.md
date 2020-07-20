<img src="recipe/tauari.png" height="100">

__Leonardo de Oliveira Martins<sup>1</sup>__
<br>
<sub>1. Quadram Institute Bioscience, Norwich Research Park, NR4 7UQ, UK</sub>

# Introduction
Phylogenetic library in python. 
It will contain python bindings for the low-level [biomcmc-lib](https://github.com/quadram-institute-bioscience/biomcmc-lib)
phylogenetic library in C.
Very beta at the moment. Empty, to be precise. 


**tauari** is the name of an endangered Brazilian timber tree. Tree &#8594; towa-ree &#8594; tauari. 

# Installation

Make sure you clone this repository recursively:
```
git clone --recursive  https://github.com/leomrtns/tauari.git
```
Right now I am testing two ways of installing it, I'll probably use the second one (autotools).
Needless to say the instructions are incomplete at this point. 

### Dependencies

* development package with the API python/C library, which is installed with your python conda installation or as `python-dev` from linux. 
* `automake`, the `check` unit test framework, and `zlib` are required for installing the lowlevel `biomcmc-lib`.
* python > 3.6 and a C compiler, e.g. `gcc`
* The lowlevel phylogenetic library [biomcmc-lib](https://github.com/quadram-institute-bioscience/biomcmc-lib), which is installed together

## installation using `pip` 

You can create a conda environment 
```bash
conda update -n base -c defaults conda # probably not needed, but some machines complained about it
conda env create -f environment.yml
conda activate tauari
pip install .

## since this software is under development, these two commands are also quite useful:

conda env update -f environment.yml # updat conda evironment after changing dependencies
pip install -e . # installs in development mode (modifications to python files are live)
python setup.py develop # same as above, but more verbose and overwriting ./build_setup directory
```

However this method assumes that `biomcmc-lib` is installed globally, which is not its original or main purpose (to be
an auxiliary, lowlevel library).
I won't write the details here because I'll probably abandon this approach.

## autotools-based installation 
This will probably be the default approach once this software becomes useful, since it compiles the lowlevel
`biomcmc-lib` together with the C components of *tauari* and generates a dynamic library. 
It still needs `setuptools` to install the python components. 

`autotools` can find the shared library installation path relative to the environment root (e.g. `conda info --base` when installing
locally or `/` if installing it system-wide).
Or it can install a regular libotool library (the difference is `pyexec_LTLIBRARIES` or `lib_`)
I plan to also generate a pre-install step in `setup.py` that runs autotools if library is absent. 

# License 
SPDX-License-Identifier: GPL-3.0-or-later

Copyright (C) 2020-today  [Leonardo de Oliveira Martins](https://github.com/leomrtns)

Tauari is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later
version (http://www.gnu.org/copyleft/gpl.html).
