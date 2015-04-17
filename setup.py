from sys import version_info
from grid_virt_sort_release.__version__ import version

try:
    from setuptools import setup, find_packages
except ImportError:
	try:
            from distutils.core import setup
	except ImportError:
            from ez_setup import use_setuptools
            use_setuptools()
            from setuptools import setup, find_packages
# we want this module for nosetests
try:
    import multiprocessing
except ImportError:
    # its not critical if this fails though.
    pass

setup(name='org-desy-grid-virt-sort-release',
    version=version,
    description="Sorts tags and similar so we always get the newest version",
    author="O M Synge",
    author_email="owen.Synge@desy.de",
    url="www-it.desy.de",
    scripts = ["org_desy_grid_virt_sort_release.py"],
    packages = ['grid_virt_sort_release'],
    tests_require=[
        'coverage >= 3.0',
        'nose >= 1.1.0',
        'mock',
    ],
    setup_requires=[
        'nose',
    ],
    test_suite = 'nose.collector',
)
