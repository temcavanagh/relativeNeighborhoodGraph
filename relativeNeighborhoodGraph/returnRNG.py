
import networkx as nx
import numpy as np
import pandas as pd

def returnRNG(numpy_distance_matrix):
    
    # Create fully connected and weighted graph
    graph_input = nx.from_numpy_matrix(np.matrix(numpy_distance_matrix), create_using=nx.Graph)
    
    # Create graph with nodes only and no weights
    graph_output = nx.classes.function.create_empty_copy(graph_input) 
    
    # Relative Neighbourhood Graph function
    def compute_rng(graph_input, graph_output): 
        for i in graph_input.nodes():
            for j in graph_input.nodes(): 
                try:
                    d_ij = graph_input[i][j]['weight']
                except KeyError:
                    d_ij = None
                    continue
                for x in graph_input.nodes(): 
                    try:
                        d_ix = graph_input[i][x]['weight']
                    except KeyError:
                        d_ix = None
                        continue
                    try:
                        d_xj = graph_input[x][j]['weight']
                    except KeyError:
                        d_xj = None
                        continue
                    if max(d_ix, d_xj) < d_ij: break
                else:
                    graph_output.add_edge(i,j, weight=d_ij)
                    
    # Compute RNG
    compute_rng(graph_input, graph_output)
    
    # Convert to numpy matrix
    rng_matrix_numpy = nx.to_numpy_matrix(graph_output)
    
    # Convert to pandas dataframe with labels
    rng_matrix_pd = pd.DataFrame(rng_matrix_numpy)
    
    return rng_matrix_pd