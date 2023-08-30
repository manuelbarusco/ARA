# ARA

Acordar Reproducibility and Results Analysis (ARA) repository contains some Python scripts and Jupyter Notebooks for the analysis of a reproducibility study conducted on the ACORDAR collection. The scripts analyze the results and informations obtained by parsing the collection with [ADE](https://github.com/manuelbarusco/ADE/tree/main) and indexing and searching over it by using [ARDFS](https://github.com/manuelbarusco/ARDFS). 

The repository structure is the following:
* <code>/files</code>: contains all the runs and runs scores that must be analyzed. It also contains the empty, partial and empty datasets lists for every parsing strategy and the ACORDAR provided files: queries, qrels and datasets.json files. 
* <code>/output</code>: it contains some output files that are produced during the analysis
* <code>/script</code>: it contains all the Jupyter Notebook and Python scripts for the run results analysis, collection analysis (duplicated and general purpose datasets) and qrels analysis. 

