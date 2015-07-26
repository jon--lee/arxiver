arxiver 0.0.1
*************

arxiver is an unoffical API for Cornell's arxiv.org. This package allows access for search results and new publications in various topics.

- Contribute on `Github <https://github.com/jon--lee/arxiver>`_

Getting started
===============
Install **arxiver** by running the following command::

    $ pip install arxiver

And then in your Python file add::

    import arxiver
    
There are two main arxiver functions: :code:`get_new_publ` and :code:`search`.

:code:`get_new_publ(topic)`
===================
Returns all new publications posted on arxiv.org given a certain topic in a :code:`Paper` list. 

**Parameters**

:code:`topic`: string that identifies from which topic the new publications should be retrieved. List of valid topics::

    'astro-ph'      # Astrophysics
    'cond-mat'      # Condensed Matter
    'gr-qc'         # General Relativity and Quantum Cosmology
    'hep-ex'        # High Energy Physics - Experiment
    'hep-lat'       # High Energy Physics - Lattice
    'hep-ph'        # High Energy Physics - Phenomenology
    'hep-th'        # High Energy Physics - Theory
    'math-ph'       # Mathematical PHysics
    'nlin'          # Nonlinear Sciences
    'nucl-ex'       # Nuclear Experiment
    'nucl-th'       # Nuclear Theory
    'physics'       # Physics
    'quant-ph'      # Quantum Physics
    
    'math'          # Mathematics
    
    'cs'            # Computer Science
    
    'q-bio'         # Quantitative Biology
    'q-fin'         # Quantitative Finance
    'stat'          # Statistics

**Example**

Return of list of papers from new publications in Computer Science and print out the link to each pdf::

    papers = arxiver.get_new_publ('cs')
    for paper in papers:
        print paper.pdf

:code:`search(query, max_results=30)`
====================================
Return list of :code:`Paper` objects from arxiv given a search query and a maximum number of results.

**Parameters**

:code:`query`: string search query to pass to arxiv.org

:code:`max_results`: positive integer maxiumum number of results to be returned (default is 30)

**Example**

Return a list of fifteen papers given 'electron' as a search term and print the abstract of each one::

    papers = arxiver.search('electron', max_results=15)
    for paper in paper:
        print paper.abstract
    
:code:`Paper`
============
:code:`Paper` objects have the following properties:

- :code:`Paper.title` the title of the paper
- :code:`Paper.abstract` the abstract or short summary
- :code:`Paper.arxiv_id` unique string that identifies the arxiv paper
- :code:`Paper.pdf` link to the pdf file of the whole paper
- :code:`Paper.page` link to the page on arxiv.org that includes more information
- :code:`Paper.authors` list of authors reprented by dictionaries with key :code:`'name'` and :code:`'link'`
