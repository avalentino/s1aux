s1aux
=====

.. badges

|PyPI Status| |GHA Status| |Python Versions| |License|

.. |PyPI Status| image:: https://img.shields.io/pypi/v/s1aux.svg
    :target: https://pypi.org/project/s1aux
    :alt: PyPI Status
.. |GHA Status| image:: https://github.com/avalentino/s1aux/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/avalentino/s1aux/actions
    :alt: GitHub Actions Status
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/s1aux
    :target: https://pypi.org/project/s1aux
    :alt: Supported Python versions
.. |License| image:: https://img.shields.io/pypi/l/s1aux
    :target: https://pypi.org/project/s1aux
    :alt: License

.. description

High level tools and function for the management of Sentinel-1 auxiliary
data produced by the ESA SAR Mission Performance Cluster (SAR-MPC_).


.. _SAR-MPC: https://sar-moc.eu


Download
--------

The ``s1aux`` source code can be downloaded from the Git_
repository on GitHub_ at https://github.com/avalentino/s1aux
or from PyPI_: https://pypi.org/project/s1aux.


.. _Git: https://git-scm.com
.. _GitHub: https://github.com
.. _PyPI: https://pypi.org


Installation
------------

The pip_ tool can be used to install the package::

  $ python3 -m pip install s1aux


.. _Pip: https://pip.pypa.io


Testing
-------

``s1aux`` includes a quite complete test suite.
It is recommended to use the pytest_ tool to run the tests::

  $ python3 -m pytest tests


.. _pytest: https://docs.pytest.org


License
-------

Copyright (c) 2024-2025 Antonio Valentino

The `s1aux` package is distributed under the Apache-2.0 License
(see the `LICENSE` file).

The package also include test data that are distributed under the terms
of use of the Copernicus Sentinel Data and Service Information legal
notice as described in

  https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice

The text of the Copernicus Sentinel Data and Service Information legal
notice is also reported in `tests/data/LICENSE.txt`.
