
User Connectedness
========
.. image:: /top_users.png

Wikipedia User Connectedness is a demo software to load data of 100 Wikipedia user talk pages, their friends and friends of friends through `MediaWiki API <https://mediawiki.org/wiki/API>`, calculate the connectedness of those 100 users, and export their data for visualization in `Gephi <https://gephi.org>` format. 

Requirements
--------------
To run this software you need to first install `mwclient <https://github.com/mwclient/mwclient>` library which provides access to most Mediawiki API functionality. mwclient is `available through PyPI <https://pypi.python.org/pypi/mwclient>`_:
 
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
* The network visualization is done using a network visulaization software `Gephi <https://gephi.org>`. 
* The nodes/links file ``Gephi100.dl`` can be imported directly into Gephi, but some knowledge with Gephi settings is required to get good visualization results. For this type of networks ``Yifan Hu`` layout is recommended, while assigning node size as a function to its in-degree value. 
* Since the size of the graph is huge, prunning the graph by filtering out all nodes with in-degree 2 or less is recommeded.
* For a quick look of what an ideal version of the graph should look like, ``Gephi_file.gephi`` can be loaded with Gephi. (The result in the file should look like ``vis3.pdf``)
