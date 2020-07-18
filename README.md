<img src="recipe/tauari.png" height="100">

__Leonardo de Oliveira Martins<sup>1</sup>__
<br>
<sub>1. Quadram Institute Bioscience, Norwich Research Park, NR4 7UQ, UK</sub>

## Introduction

Python bindings for biomcmc-lib 

**tauari** is the name of an endangered Brazilian timber tree. 

## Installation

Make sure you clone this repository recursively
```
git clone --recursive  https://github.com/leomrtns/tauari.git
```
### dependencies

* development package with the API python/C library, which is installed with your python conda installation or as `python-dev` from linux. 
In any case `setuptools` checks for it and installs from `pip` if missing. 
* `autotools`, for installing the lowlevel `biomcmc-lib`. 


## License 
SPDX-License-Identifier: GPL-3.0-or-later

Copyright (C) 2020-today  [Leonardo de Oliveira Martins](https://github.com/leomrtns)

Tauari is free software; you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later
version (http://www.gnu.org/copyleft/gpl.html).
