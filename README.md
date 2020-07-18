<img src="recipe/tauari.png" height="100">

__Leonardo de Oliveira Martins<sup>1</sup>__
<br>
<sub>1. Quadram Institute Bioscience, Norwich Research Park, NR4 7UQ, UK</sub>

## Introduction

Python bindings for [biomcmc-lib](https://github.com/quadram-institute-bioscience/biomcmc-lib), a phylogenetic library in C.


**tauari** is the name of an endangered Brazilian timber tree. Tree &#8594; towa-ree &#8594; tauari. 

## Installation

Make sure you clone this repository recursively:
```
git clone --recursive  https://github.com/leomrtns/tauari.git
```

Then you can create a conda environment 
```bash
conda update -n base -c defaults conda # probably not needed, but some machines complained about it
conda env create -f environment.yml
conda activate tauari
pip install .
```

Or maybe just `pip install .` in your current environment.
Since this software is under development, these two commands are quite useful:

```bash
conda env update -f environment.yml # updat conda evironment after changing dependencies
pip install -e . # installs in development mode (modifications to python files are live)
```

### Dependencies

* development package with the API python/C library, which is installed with your python conda installation or as `python-dev` from linux. 
* `automake`, the `check` unit test framework, and `zlib` are required for installing the lowlevel `biomcmc-lib`.
* python > 3.6 and a C compiler, e.g. `gcc`

The lowlevel phylogentic library [biomcmc-lib](https://github.com/quadram-institute-bioscience/biomcmc-lib)


## License 
SPDX-License-Identifier: GPL-3.0-or-later

Copyright (C) 2020-today  [Leonardo de Oliveira Martins](https://github.com/leomrtns)

Tauari is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later
version (http://www.gnu.org/copyleft/gpl.html).
