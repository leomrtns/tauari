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

### Dependencies

* python development package (with the API python/C library).  Installed with your python conda installation or as `python-dev` from linux. 
* `automake`, the `check` unit test framework, and `zlib` are required for installing the lowlevel `biomcmc-lib`.
* python > 3.6 and a C compiler, e.g. `gcc`
* The lowlevel phylogenetic library [biomcmc-lib](https://github.com/quadram-institute-bioscience/biomcmc-lib), which should be included here
(it will be compiled as well). 
For a more up-to-date list you may need to check the conda/docker files once they are complete.

# Installation

Make sure you clone this repository recursively:
```
git clone --recursive  https://github.com/leomrtns/tauari.git
```

**tl;dr:** You can create a conda environment (or not) and then run `pip install .`  
```bash
conda update -n base -c defaults conda # probably not needed, but some machines complained about it
conda env create -f environment.yml
conda activate tauari
pip install .

## since this software is under development, I find these two commands quite useful:

conda env update -f environment.yml # updat conda evironment after changing dependencies
pip install -e . # installs in development mode (modifications to python files are live)
python setup.py develop # same as above, but more verbose and overwriting ./build_setup directory
```

## Details: autotools-based installation 

Originally `biomcmc-lib` is an auxiliary, lowlevel library, and as such should not be directly exposed to the user or
shared system-wide (you can do it, btw, but it's intended as a "subdir" for autotools).
Therefore **tauari** compiles `biomcmc-lib` together with its C components, generating a dynamic library.
Just like [setuptools.Extension](https://docs.python.org/3/extending/building.html), but using autotools.
It still needs `setuptools` to install the python components and move the library to the correct location.  

Calling `pip install .` (or `python setup.py install`) will run autotools in the background, but if you want you can run it by hand:
```bash
cd build_setup
../configure --prefix="." 
make && make install
ls lib/
```
The file "tauari_c.so" can be imported in python.

# License 
SPDX-License-Identifier: GPL-3.0-or-later

Copyright (C) 2020-today  [Leonardo de Oliveira Martins](https://github.com/leomrtns)

Tauari is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later
version (http://www.gnu.org/copyleft/gpl.html).
