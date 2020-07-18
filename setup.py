import pathlib, setuptools, sysi, os
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess

min_version = (3, 6)

if sys.version_info < min_version:
    error = """
Python {0} or above is required.

Make sure you have an up-to-date pip installed.  
""".format('.'.join(str(n) for n in min_version)), sys.exit(error)

base_dir = pathlib.Path(__file__).parent.resolve()
version_file = f"{base_dir}/tauari/__version__.py"
readme_file  = f"{base_dir}/README.md"
build_path   = f"{base_dir}/build"
biomcmc_path = f"{build_path}/biomcmc-lib"
include_path = f"{build_path}/include"
library_path = f"{build_path}/lib"
source_files = ["tauari_module.c"]
source_files = [f"{base_dir}/src/{x}" for x in source_files]

# Eval the version file to get __version__; avoids importing our own package
with version_file.open() as f: exec(f.read())
with readme_file.open(encoding = "utf-8") as f: long_description = f.read()

module_c = setuptools.Extension('_tauari_c',
  include_dirs = [include_path],
  library_dirs = [library_path],
  runtime_library_dirs = [library_path],
  libraries = ['biomcmc'],
  sources = source_files)

if not os.path.exists(biomcmc_path): # developers can have their own links (without submodule)
    source = f"{base_dir}/submodules/biomcmc-lib/"
    if not os.path.exists(source):
        sys.exit(f"Tauari:: No '{source}' found;\n You must download this repository with 'git clone --recursive' or add biomcmc-lib by hand to {biomcmc_path}")
    print (f"Tauari:: Creating a link '{biomcmc_path}' pointing to '{source}'")
    os.symlink(source, biomcmc_path)

def biomc2_compilation (debug = ""):
    autoconf_path = f"{biomcmc_path}/configure"
    subprocess.check_call(f"cd {build_path} && {autoconf_path} --prefix={build_path} {debug}".split())
    subprocess.check_call(f"cd {build_path} && make".split())
    subprocess.check_call(f"cd {build_path} && make install".split())
class PreDevelopCompile(develop):
    """pre-compilation for development mode"""
    def run(self):
        biomc2_compilation("--enable-debug")
        develop.run(self) # run() after check_call means pre-install
class PreInstallCompile(install):
    """Pre-compilation for installation mode"""
    def run(self):
        biomc2_compilation()
        install.run(self)

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
    package_data = {'tauari': [f"{include_path}/*",f"{library_path}/*"]},
    data_files = [("", ["LICENSE"])],
    python_requires = '>={}'.format('.'.join(str(n) for n in min_version)),
    license='GPLv3+',
    install_requires=[
        'python-dev',
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
        'develop': PostDevelopCompile,
        'install': PostInstallCompile,
    },
    ext_modules = [module_c]
)
