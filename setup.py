#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "PyNN",
    version = "0.3.0",
    package_dir={'pyNN': ''},
    packages = ['pyNN'],
    author = "The NeuralEnsemble Community",
    author_email = "pynn@neuralensemble.org",
    description = "A Python package for simulator-independent specification of neuronal network models",
    license = "CeCILL",
    keywords = "computational neuroscience simulation neuron nest pcsim neuroml",
    url = "http://neuralensemble.org/PyNN/",
     )