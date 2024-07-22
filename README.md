# MultiXVERSE

Embedding of Monoplex, Multiplex, Heterogeneous, Multiplex-Heterogeneous and full Multiplex-Heterogeneous Networks.

You can find in this repository the necessary files to use MultiXVERSE for universal multilayer network embedding. You can find the corresponding preprint on osf here: (https://files.osf.io/v1/resources/d78wb/providers/osfstorage/6684cbed9c98c701b51b3f77?action=download&direct&version=3)

To employ MultiXVERSE, it is essential that the networks are formatted similarly to the example found in the /airport directory, as this format is required for utilizing MultiXRank (available at https://github.com/anthbapt/multixrank). The airport network provided in this directory originates from the same source.

## Requirements

Python 3:
* multixrank
* gensim (fast_version enabled)
* networkx=2.2
* numba=0.50.1
* scikit-learn=0.21.3 (for evaluation)
* pandas

A good way to set up the appropriate environement is to use the associated .yml conda environment.

## MultiXVERSE.py example:

This program allows to apply MultiXVERSE on a multilayer network, here the airport network.

The usage is the following:

`python3 MultiXVERSE.py`

The output of this command is the embedding 'embedding_MH.npy' in the directory Results_Embeddings. The embedding is a dictionary with the index as key and the corresponding embedding as value.
