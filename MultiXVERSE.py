# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:09:00 2019

@author: Léo Pio-Lopez
"""

import numpy as np
import argparse
import os
import datetime
import utils as f
import pandas as pd
import multiprocess

import multixrank
import pandas as pd
import multiprocess as mp
import yaml


def main(args=None):
        


    ########################################################################
    # Parameters multiverse and train/test
    ########################################################################

    EMBED_DIMENSION = 128
    CLOSEST_NODES = np.int64(300)
    NUM_SAMPLED = np.int64(10)
    LEARNING_RATE = np.float64(0.01)
    NB_CHUNK = np.int64(1)
    CHUNK_SIZE = np.int64(100)
    NUM_STEPS_1 = np.int64(100*10**6/CHUNK_SIZE)
    

    #If toy example
    EMBED_DIMENSION = 128
    CLOSEST_NODES = np.int64(2)
    NUM_SAMPLED = np.int64(10)
    LEARNING_RATE = np.float64(0.01)
    NB_CHUNK = np.int64(1)
    CHUNK_SIZE = np.int64(2)
    NUM_STEPS_1 = np.int64(100*10**6/CHUNK_SIZE)
    
    
    ##################################################################################
    # Ensure that the nodes in the bipartite network match those in the multiplex networks. 
    # If there are nodes in the multiplex networks that are not present in the bipartite network, these extra nodes must be removed.
    # Or self-loops on this missing nodes must be added in one layer of the corresponding multiplex and the parameter 'self-loops' passed to 1 in the multixrank parameters
    ##################################################################################
    

    ###################################################################################"
    # MULTIXRANK
    ###################################################################################"
 

    num_cpu=4

    multixrank_obj = multixrank.Multixrank(config="airport/config_minimal.yml", wdir="airport")
    nodes_multiplex = multixrank_obj.multiplexall_node_list2d
    # Using list comprehension to flatten the list of lists
    nodes_multiplex = pd.DataFrame([(i, node) for i, nodes in enumerate(nodes_multiplex) for node in nodes], columns=['network', 'node'])

    # Make all seeds.txt and associated config_minimal.yml
    with open('airport/config_minimal.yml', 'r') as file:
        file_param = yaml.safe_load(file)
            
    for i in  range(len(nodes_multiplex.node)):
        with open('airport/configs/seeds'+str(i)+'.txt', 'w+') as file:
            file.write(str(nodes_multiplex.node[i]))

        file_param['seed'] = 'seeds'+str(i)+'.txt'
        with open('airport/configs/config_minimal'+str(i)+'.yml', 'w+') as file:
            document = yaml.dump(file_param, file)

    def mxrank(k):
        print(str(k) + '\n')
        multixrank_obj = multixrank.Multixrank(config='airport/configs/config_minimal'+str(k)+'.yml', wdir="airport/configs")
        print('he')
        ranking_df = multixrank_obj.random_walk_rank()
        output_obj = multixrank.Output(ranking_df, multixrank_obj, top=None)
        res = output_obj._df
        res.multiplex=multixrank_obj.seed_obj.seed_list*len(res)   
        return res

    list_similarities=[]
    p = mp.Pool(processes=num_cpu)
    list_similarities.append(p.map(mxrank, [i for i in range(len(nodes_multiplex.node))])    )

    similarity_matrix_list = pd.concat(list_similarities[0], axis=0, ignore_index=False)
    similarity_matrix = similarity_matrix_list.pivot(index='multiplex', columns='node', values='score')


        ########################################################################
        # Processing of the network
        ########################################################################
        
    reverse_data_DistancematrixPPI, list_neighbours, nodes, rawdata_DistancematrixPPI, neighborhood, nodesstr = f.netpreprocess1(similarity_matrix, CLOSEST_NODES)
     
        ########################################################################
        # Initialization
        ######################################################################## 

    embeddings = np.random.normal(0, 1, [np.size(nodes), EMBED_DIMENSION])
 
        ########################################################################
        # Training and saving best embeddings   
        ######################################################################## 
    # Train and test during training
    neighborhood = np.asarray(neighborhood)
    nodes= np.asarray(nodes)
    
    embeddings = f.train(neighborhood, nodes, list_neighbours, NUM_STEPS_1, NUM_SAMPLED, LEARNING_RATE, \
                         CLOSEST_NODES, CHUNK_SIZE, NB_CHUNK, embeddings, reverse_data_DistancematrixPPI)
 
    X = dict(zip(range(embeddings.shape[0]), embeddings))
    X = {str(int(nodesstr[key])+1): X[key] for key in X}
    np.save('embeddings_MH',X)
    os.replace('embeddings_MH.npy', './results_Embeddings/'+ 'embeddings_MH.npy')
    
if __name__ == "__main__":
    main()
    
    
    
  













