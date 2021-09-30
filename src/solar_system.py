import pandas as pd
import numpy as np
import scipy as sp
import networkx as nx
import matplotlib.pyplot as plt
import pyvis
from pyvis.network import Network
import collections


def main():
    node_df = pd.read_csv('nodes.csv')
    edge_df = pd.read_csv('edges.csv')
    graph = nx.from_pandas_edgelist(edge_df, 'Source', 'Target')

    net = Network(height='100%', width='100%', notebook=True, bgcolor='#000000', font_color='#ffffff')
    for idx, row in node_df.iterrows():
        net.add_node(row['Node'], size=row['Size'], mass=row['Mass'], color=row['Color'])
    for idx, row in edge_df.iterrows():
        net.add_edge(row['Source'], row['Target'])
    for node in net.nodes[0:14]:
        node['shape'] = 'circularImage'
        node['image'] = 'imgs/' + str(node['id']).lower() + '.jpg'
    net.show_buttons(True)
    net.show('example.html')
    plot_degree(graph)
    eigen = nx.eigenvector_centrality_numpy(graph)
    print('eigenvalue', eigen)
    betweeness = nx.betweenness_centrality(graph)
    print('betweeness', betweeness)
    closeness = nx.closeness_centrality(graph)
    print('clossness:', closeness)
    # plt.show()


def plot_degree(graph):
    degree_sequence = sorted([d for n, d in graph.degree()], reverse=True)  # degree sequence
    # print "Degree sequence", degree_sequence
    degree_count = collections.Counter(degree_sequence)
    deg, cnt = zip(*degree_count.items())

    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color='b')

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)


if __name__ == '__main__':
    main()