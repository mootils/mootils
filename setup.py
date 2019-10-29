from setuptools import setup

from mootils.version import __version__

# ---------------------------------------------------------------------------------------------------------
# GENERAL
# ---------------------------------------------------------------------------------------------------------


__name__ = "mootils"
__author__ = ""
__url__ = ""
__email__ = ""

__licence__ = ""
#__licence__ = "Apache License 2.0"

data = dict(
    name=__name__,
    version=__version__,
    author=__author__,
    url=__url__,
    python_requires='>=3.5',
    author_email=__email__,
    description="Exploration and Analysis in Multi-objective Optimization",
    license=__licence__,
    keywords="optimization",
    install_requires=['numpy>=1.15', 'pandas', 'matplotlib', 'scipy'],
    platforms='any',
    packages=['mootils', 'mootils.analysis', 'mootils.qualityindicator', 'mootils.visualization'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics'
    ]
)


# ---------------------------------------------------------------------------------------------------------
# OTHER METADATA
# ---------------------------------------------------------------------------------------------------------


# update the readme.rst to be part of setup
def readme():
    with open('README.md') as f:
        return f.read()


data['long_description'] = readme()


# ---------------------------------------------------------------------------------------------------------
# RUN
# ---------------------------------------------------------------------------------------------------------


setup(**data)
