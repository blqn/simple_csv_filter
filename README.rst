=================
Simple CSV Filter
=================


Pure Python CSV filter with simple regex.

* Free software: BSD license


Features
--------

* Filter a CSV file with simple patterns
* Based on *.ini* config files

Install
-------

From sources
~~~~~~~~~~~~

* Clone your fork locally::

    $ git clone git@github.com:blqn/simple_csv_filter.git
    $ cd simple_csv_filter

* Install:

    - in a custom environment(recommended)::

        $ pipenv --three
        $ pipenv install .
        $ pipenv run simple_csv_filter -h

    - in the user environment::

        $ pip install --user .

    - in the system environment::

        $ sudo pip install .


Usage
-----

The CSV filter is based on a python configuration file.
The file can contain a *CSV parser* configuration field and other filters fields.

CVS parser
~~~~~~~~~~

Argument that are passed to **csv.reader** and **csv.writer** methods (`<https://docs.python.org/library/csv.html>`_) through \*\*kwargs.
The key *out* can be passed to indicate the saveas filename.

.. code-block:: none

    [csv]
    out = out.csv
    encoding = UTF-8

Filter
~~~~~~

Filter are setup in parts named [filter.**name**].
Each part are applied on csv file in the file order.
Filter have a type(default **type = or**):

* **or**: Match row if one condition is validated
* **and**: Match row if all conditions are validated
* **none**: Match row if not any condition is validated

Other filter keys need to match one csv headers and the value is a regex.

.. code-block:: none

    [filter.toto]
    type = and
    column1 = \*toto\*
    column2 = \*toto\*

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

