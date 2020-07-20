This folder is usually empty, with two occasions where it may be used:

1. If you (like me) want to share the same `biomcmc-lib` code across repositories. 
I have a symbolic link pointing to the "master repository" (it is ignored by git, and `setup.py` checks for its
presence)

2. When running `python setup.py install` or `python setup.py develop`, biomcmc-lib is compiled here (making it easier
to debug). `pip` does everything on `/tmp`, and suppresses output. 

The script `../clean_dist.sh` deletes all generated files.
