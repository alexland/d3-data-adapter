#!/usr/local/bin/python2.7
# encoding: utf-8

# TODO: add exception handling for adjmatrix_tojson--e.g., if numpy array passed  
# TODO: add to utests, code for reading from json files, converting to adj matrix then comp w/ original adj matrix, assert orign == this instance


import os
import random as RND
import numpy as NP
import itertools
import networkx as NX
import json as JSON


#---------------------- convert adj matrix to JSON ---------------------#

def adjmatrix_tojson(adj_matrix):
    """
        returns valid JSON-encoded graph
        pass in: graph represented as adjacency matrix (python nested list)
        
    """
    G = {"links": [], "nodes": []}
    n = len(adj_matrix[0])
    keys_links = ("source", "target", "value")
    keys_nodes = {"group", "name"}
    for i, row in enumerate(adj_matrix):
        G["nodes"].append( dict(zip(keys_nodes, 
            (1, "n{0}".format(i)))) )
        for j, itm in enumerate(row):
            G["links"].append( dict(zip(keys_links, (i, j, itm))) )
    return G


#---------------------- write json-encoded graph to file ---------------------#

def write_jsongraph(graphfilename, json_graph_obj):
    """
        returns: nothing writes JSON-encoded graph to file
        whose name and location are passed in
        pass in: 'fname', file path and name of data file created
        upon execution of this fn 
    """
    with open(graphfilename, mode="w") as f:
        JSON.dump(json_graph_obj, f, indent=2)


#------------- teset --------------#

def utest1():
    G = NX.florentine_families_graph()
    AM = NX.to_numpy_matrix(G).tolist()
    write_jsongraph("gd1.json", adjmatrix_tojson(AM))


def utest2():
    G = NX.erdos_renyi_graph(25, .1, 456)
    AM = NX.to_numpy_matrix(G).tolist()
    write_jsongraph("gd1.json", adjmatrix_tojson(AM))


def utest3():
    G = NX.bipartite_gnmk_random_graph(20, 10, 50)
    AM = NX.to_numpy_matrix(G).tolist()
    write_jsongraph("gd1.json", adjmatrix_tojson(AM))
    


    



