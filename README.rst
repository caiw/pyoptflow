.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1043971.svg
   :target: https://doi.org/10.5281/zenodo.1043971
   
.. image:: https://travis-ci.org/scivision/pyoptflow.svg?branch=master
   :target: https://travis-ci.org/scivision/pyoptflow
   
.. image:: https://coveralls.io/repos/github/scivision/pyoptflow/badge.svg?branch=master
   :target: https://coveralls.io/github/scivision/pyoptflow?branch=master
   
.. image:: https://ci.appveyor.com/api/projects/status/9iv32q84vd3gbdde?svg=true
    :target: https://ci.appveyor.com/project/scivision/pyoptflow

.. image:: https://img.shields.io/pypi/pyversions/pyoptflow.svg
  :target: https://pypi.python.org/pypi/pyoptflow
  :alt: Python versions (PyPI)

.. image::  https://img.shields.io/pypi/format/pyoptflow.svg
  :target: https://pypi.python.org/pypi/pyoptflow
  :alt: Distribution format (PyPI)

.. image:: https://api.codeclimate.com/v1/badges/b7a550fa1d50af8491d3/maintainability
   :target: https://codeclimate.com/github/scivision/pyoptflow/maintainability
   :alt: Maintainability


.. image:: http://pepy.tech/badge/pyoptflow
   :target: http://pepy.tech/project/pyoptflow
   :alt: PyPi Download stats

=====================================
Optical Flow: Horn-Schunck
=====================================
Python implementation of optical flow estimation using only the Scipy stack for:

* Horn Schunck


Lucas-Kanade is also possible in the future, let me know if you're interested in Lucas Kanade.

.. contents::

Install
=======
Requires Python >= 3.6::

    pip install -e .
    
    
optionally, to run self-tests::

    pip install -e .[tests]
    
    pytest -v
    

Examples
========

The program scripts expect <directory> <glob pattern>
It uses [imageio](https://imageio.github.io/) to load a very wide varity of images *and* video.

Box
---
::

  python HornSchunck.py data/box box*.bmp


Office
------
all time steps::

  python HornSchunck.py data/office office*.bmp
  
or just the first 2 time steps::

  python HornSchunck.py data/office office.[0-2].bmp

Rubic
------
::

  python HornSchunck.py data/rubic rubic*.bmp

Sphere
------
::

  python HornSchunck.py data/sphere sphere*.bmp

Comparision with Matlab Computer Vision toolbox
===============================================
In ``Matlab`` directory, similar method in Octave and a comparison plot using Matlab Computer Vision toolbox.


Reference
=========
`Inspiration <https://github.com/ablarry91/Optical-Flow-LucasKanade-HornSchunck/>`_
