Consistent ``pip`` Requirements
===============================

.. image:: https://github.com/smsearcy/pre-commit-poetry-export/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/smsearcy/pre-commit-poetry-export/actions/workflows/tests.yml
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

|

A ``pre-commit`` hook to ensure that multiple Python requirements files
(e.g. for development and production)
have consistent versions.


Why?
----

You're using `pip-tools <https://pypi.org/project/pip-tools/>`_
(or something similar)
to manage production and development requirements files
and want to make sure that nothing gets out of sync.


How to Use
----------

Add the following to your `.pre-commit-config.yaml` file:

.. code-block:: yaml

    repos:
      - repo: https://github.com/smsearcy/pre-commit-consistent-pip-requirements
        rev: v0.1.0
        hooks:
          - id: check-requirements


How it Works
------------

Compares the versions of packages in multiple requirements files
and fails if any packages that exist in multiple files do not have the same version.

If there is a ``requirements`` folder, it compares all ``*.txt`` files in that folder.
Otherwise it finds files matching the pattern ``*requirements*.txt`` in the root of the repository and checks those files.

If the hook fails then you'll need to fix the discrepancy and then re-commit.


Contributing
------------

Found an issue or want to suggest an improvement in the code?
Please contribute by opening an issue or a pull request.

Thanks! :)
