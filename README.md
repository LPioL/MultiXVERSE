# MultiXVERSE

# MultiVERSE
Embedding of Monoplex, Multiplex, Heterogeneous, Multiplex-Heterogeneous and full Multiplex-Heterogeneous Networks.

You can find in this repository the necessary files to use MultiXVERSE for universal multilayer network embedding. You can find the corresponding preprint on osf here: (https://files.osf.io/v1/resources/d78wb/providers/osfstorage/6684cbed9c98c701b51b3f77?action=download&direct&version=3)

In order to use MultiXVERSE, you need the networks to be in the same format as the example in /airport.


## Requirements

Python 3:
* multixrank
* gensim (fast_version enabled)
* networkx=2.2
* numba=0.50.1
* scikit-learn=0.21.3 (for evaluation)
* pandas

A good way to set up the appropriate environement is to use the associated .yml conda environment.

## MultiXVERSE:

**MultiXVERSE_M.py**

This program allows to apply MultiVERSE on a multiplex network.

The usage is the following for this example with the airport multilayer network:

`python3 MultiXVERSE.py`

          Options:
                 -k NUMERIC
                   Value of the position of the networks in the list 'Test_Networks'

To use the example, you can write in a terminal the following command:

The output of this command is the embedding 'embedding_MH.npy' in the directory ResultsèEmbeddings. The embedding is a dictionary with the index as key and the corresponding embedding as value.
