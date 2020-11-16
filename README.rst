==============
meteo-terminal
==============

**Installation:**

Displays weather forecast based on meteo-villes list of cities with assessed weather forecast.

.. code:: bash

    # Weather forecast for today in Toulouse
    meteo
    # Weather forecast for Paris tomorrow
    meteo -c paris -t
    # weather forecast in Biarritz yesterday
    meteo -c biarritz -y
    # print available cities and prompt:
    meteo -c


.. code:: bash

    $ pip install meteo-terminal


.. code:: bash


    virtualenv venv

    source venv/bin/activate

    pip install -r requirements.txt

    pip install -r test-requirements.txt



Run the tests to ensure this all worked.


.. code:: bash

    py.test tests
