import pathlib, setuptools, sys, os
import setuptools.command.develop
import setuptools.command.install
import setuptools.command.egg_info
import subprocess

min_version = (3, 6)

if sys.version_info < min_version:
    error = """
Python {0} or above is required.

Make sure you have an up-to-date pip installed.  
""".format('.'.join(str(n) for n in min_version)), sys.exit(error)

base_dir = pathlib.Path(__file__).parent.resolve()
version_file = base_dir/"tauari/__version__.py" # not a string but a file handler
readme_file  = base_dir/"README.md"
build_path   = f"{base_dir}/build"
biomcmc_path = f"{build_path}/biomcmc-lib"
source_files = ["tauari_module.c"]
source_files = [f"src/{x}" for x in source_files]

# Eval the version file to get __version__; avoids importing our own package
with version_file.open() as f: exec(f.read())
with readme_file.open(encoding = "utf-8") as f: long_description = f.read()

module_c = setuptools.Extension('_tauari_c',
    include_dirs = ["build/include/biomcmc"], 
    library_dirs =  ["build/lib"],
    runtime_library_dirs = ["build/lib"], 
    libraries = ['biomcmc'],
    undef_macros = [ "NDEBUG" ],
    sources = source_files)

if not os.path.exists(biomcmc_path): # developers can have their own links (without submodule)
    source = f"{base_dir}/submodules/biomcmc-lib/"
    if not os.path.exists(source):
        sys.exit(f"Tauari:: No '{source}' found;\n You must download this repository with 'git clone --recursive' or add biomcmc-lib by hand to {biomcmc_path}")
    print (f"Tauari:: Creating a link '{biomcmc_path}' pointing to '{source}'")
    os.symlink(source, biomcmc_path)

def biomc2_compilation (debug = ""):
    autoconf_path = f"{biomcmc_path}/configure"
    subprocess.call(f"{autoconf_path} --prefix={build_path} {debug}".split(), cwd=build_path) 
    subprocess.call(f"make install".split(), cwd=build_path) # biomcmc is installed locally, both prefix and `make  install` are useless
    print (" 2 :", os.listdir(build_path))

class PrePostDevelopCompile(setuptools.command.develop.develop):
    """pre- and post-compilation for development mode (only pre- currently)"""
    def run(self):
        biomc2_compilation("--enable-debug")
        setuptools.command.develop.develop.run(self) # run() after chec k_call means pre-install
class PrePostInstallCompile(setuptools.command.install.install):
    """Pre- and post-compilation for installation mode (only pre- currently)"""
    def run(self):
        biomc2_compilation()
        setuptools.command.install.install.run(self)
class PrePostEggInfoCompile(setuptools.command.egg_info.egg_info):
    """Pre- and post-compilation for installation mode (only pre- currently)"""
    def run(self):
        biomc2_compilation()
        setuptools.command.egg_info.egg_info.run(self)

setuptools.setup(
    name = "tauari",
    version = __version__,
    author = "Leonardo de Oliveira Martins",
    author_email = "Leonardo.de-Oliveira-Martins@quadram.ac.uk",
    description = "Python bindings for biomcmc-lib, a C library for phylogenetics",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = "phylogenetics",
    url = "https://github.com/quadram-institute-bioscience",
    project_urls = {
        "Source": "https://github.com/quadram-institute-bioscience",
    },
    packages = setuptools.find_packages(),
    include_package_data=True,
    package_data = {'tauari': ["build/lib","build/lib/libbiomcmc*", "build/include/*", "build/include/biomcmc/*"]}, # relative paths to setup.py only 
    data_files = [("", ["LICENSE"])],
    python_requires = '>={}'.format('.'.join(str(n) for n in min_version)),
    license='GPLv3+',
    install_requires=[
        'biopython >= 1.68'
       ],
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    # Install a "tauari" program which calls tauari.__main__.main()
    #entry_points = { "console_scripts": ["tauari = tauari.tauari:main"]},
    cmdclass={
        'develop':  PrePostDevelopCompile,
        'install':  PrePostInstallCompile,
        'egg_info':  PrePostEggInfoCompile,
    },
    ext_modules = [module_c]
)
