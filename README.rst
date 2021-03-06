.. image:: https://travis-ci.org/Y-oHr-N/kenchi.svg?branch=master
    :target: https://travis-ci.org/Y-oHr-N/kenchi

.. image:: https://ci.appveyor.com/api/projects/status/5cjkl0jrxo7gmug0/branch/master?svg=true
    :target: https://ci.appveyor.com/project/Y-oHr-N/kenchi/branch/master

.. image:: https://coveralls.io/repos/github/Y-oHr-N/kenchi/badge.svg?branch=master
    :target: https://coveralls.io/github/Y-oHr-N/kenchi?branch=master

.. image:: https://codeclimate.com/github/Y-oHr-N/kenchi/badges/gpa.svg
    :target: https://codeclimate.com/github/Y-oHr-N/kenchi

.. image:: https://badge.fury.io/py/kenchi.svg
    :target: https://badge.fury.io/py/kenchi

.. image:: https://anaconda.org/Y_oHr_N/kenchi/badges/version.svg
    :target: https://anaconda.org/Y_oHr_N/kenchi

.. image:: https://readthedocs.org/projects/kenchi/badge/?version=latest
    :target: http://kenchi.readthedocs.io/en/latest/?badge=latest

kenchi
======

This is a set of python modules for anomaly detection.

Requirements
------------

-  Python (>=3.6)
-  matplotlib (>=2.1.1)
-  networkx (>=2.0)
-  numpy (>=1.14.0)
-  pandas (>=0.22.0)
-  scikit-learn (>=0.19.1)
-  scipy (>=1.0.0)

Installation
------------

You can install via ``pip``

::

    pip install kenchi

or ``conda``.

::

    conda install -c y_ohr_n kenchi

Usage
-----

.. code:: python

    import matplotlib.pyplot as plt
    from kenchi.datasets import make_blobs
    from kenchi.outlier_detection import SparseStructureLearning

    # Generate the training data
    X, _ = make_blobs(centers=1, random_state=1, shuffle=False)

    # Fit the model according to the given training data
    det  = SparseStructureLearning(alpha=0.2).fit(X)

    # Plot the anomaly score for each training sample
    det.plot_anomaly_score(linestyle='', marker='.')

    plt.show()

.. image:: docs/images/plot_anomaly_score.png
    :align: center
    :alt: Anomaly score

License
-------

The MIT License (MIT)

Copyright (c) 2017 Kon
