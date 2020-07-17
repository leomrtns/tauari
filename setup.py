from pathlib import Path
import setuptools, sys
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess

min_version = (3, 6)

if sys.version_info < min_version:
    error = """
Python {0} or above is required.

Make sure you have an up-to-date pip installed.  
""".format('.'.join(str(n) for n in min_version)), sys.exit(error)

base_dir = Path(__file__).parent.resolve()
version_file = base_dir / "tauari/__version__.py"
readme_file = base_dir / "README.md"
#csrc_path = os.path.relpath(os.path.join(os.path.dirname(__file__), "src"))
src_path = base_dir / "src"
build_path = base_dir/ "build"

# Eval the version file to get __version__; avoids importing our own package
with version_file.open() as f: exec(f.read())
with readme_file.open(encoding = "utf-8") as f: long_description = f.read()

module_c = setuptools.Extension('_tauari_c',
  include_dirs = [f"{build_path}/include"],
  library_dirs = [f"{build_path}/lib"],
  runtime_library_dirs = [f"{build_path}/lib"],
  libraries = ['biomcmc'],
  sources = [f"{src_path}/somefile.c"])

def biomc2_compilation (debug = ""):
    autoconf_path = base_dir / "submodules/biomcmc-lib/configure"
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
    package_data = {'peroba': ['data/*','data/report/*']},
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
    entry_points = {
        "console_scripts": [
            "tauari = tauari.tauari:main"
        ]
    },
    cmdclass={
        'develop': PostDevelopCompile,
        'install': PostInstallCompile,
    },
    ext_modules = [module_c]
)
