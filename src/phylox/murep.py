import networkx as nx
import numpy as np
from phylox import DiNetwork

def add_mu_vectors_as_attribute(network):

    for node in network.nodes:
        network.nodes[node]["muvec"] = np.zeros(len(network.leaves))
    
    for i, leaf in enumerate(network.leaves):
        network.nodes[leaf]["muvec"][i] = 1
        _update_parents(network, leaf, network.nodes[leaf]["muvec"])


def _update_parents(network, node, muvec):
    for parent in network.predecessors(node):
        network.nodes[parent]["muvec"] += muvec
        _update_parents(network,parent,muvec)
    