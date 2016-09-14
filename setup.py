import os

# Working dir
current_path = os.path.abspath(os.path.dirname(__file__))

# Load package info
exec(compile(open(os.path.join(current_path, 'arle', 'package.py')).read(),
    'package.py', 'exec'), globals(), locals())

from setuptools import find_packages, setup

import sys

# Check Python version
# Not sure yet which py verions to support
# So until decided fix it to 3.5
py_version = sys.version_info[:2]
if py_version[0] == 3 and py_version < (3, 5):
    raise RuntimeError('Asus ROG Linux Extras requires 3.5.x or better')

setup(
    name='arle',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Operating System :: POSIX :: Linux',
        'Topic :: Utilities',
    ],
    keywords='asus rog linux',
    author=author,
    author_email=email,
    url=url,
    license=license,
    packages=find_packages("."),
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    entry_points='''
        [console_scripts]
        arle=arle.cli:entry_point
    '''
)
