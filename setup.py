from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

version=open("VERSION").readline().strip()

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    'baker >= 1.3',
    'python-dateutil >= 1.5, < 2.0',    # python-dateutil-2.0 is for Python 3.0
    'pandas >= 0.9.0',
    'tstoolbox >= 0.5',
    'construct >= 2.0.6',
]


setup(name='hspfbintoolbox',
    version=version,
    description="Reads Hydrological Simulation Program - FORTRAN binary files and prints to screen.",
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='hspf binary hydrologic',
    author='Tim Cera, P.E.',
    author_email='tim@cerazone.net',
    url='http://pypi.python.org/pypi/hsbfbintoolbox',
    license='GPL',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['hspfbintoolbox=hspfbintoolbox:main']
    }
)
