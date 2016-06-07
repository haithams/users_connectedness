

User Connectedness
========

Wikipedia User Connectedness is a demo software to read data of 100 users, their friends and friends of friends through `MediaWiki API <https://mediawiki.org/wiki/API>`, calculate the connectedness of those 100 users, and export their data for visualization using `Gephi <https://gephi.org>`. 

Requirements
--------------
To run this software you need to first install `mwclient <https://github.com/mwclient/mwclient>` library - which provides access to most API functionality- is `available through PyPI <https://pypi.python.org/pypi/mwclient>`_:

.. code-block:: console

    $ pip install mwclient

Implementation notes
--------------------
* ``Read_API.py`` : loads data from MediaWiki API, and saves it to a local file ``List100.txt`` in an original format.

* ``Sort.py`` : loads data from ``List100.txt``, calculates connectedness of 100 users, stores results in ``100users_connectedness.txt``, and exports node&link data in gephi format ``Gephi100.dl`` (for visualization).

* The number of users is limited to 100 as the API load time increases exponentially when considering second degree friends.
* The 100 users are the first 100 registered accounts on English Wikipedia.
* Connectedness was calculated only for the 100 users in the cohort only. Calculating connectedness of all the users (friends and friends-of-friends .. etc) would require loading the full database.
* Connectedness of a user X was weighted by 1 for edits from X's friends, and by 0.1 for edits from X's friends-of-friends.
* Low-degree nodes were omitted in the visualizations to prevent cluttering the graph. (further custom visualizations can be produced using Gephi)

Data Visualization 
----------------
