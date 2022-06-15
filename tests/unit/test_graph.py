from graph_inait import Graph
from random import randint


def test_smoke_graph():
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2),
             (2, 3),
             (3, 4),
             (4, 5),
             (5, 1)]
    graph = Graph(list_nodes=nodes, list_edges=edges)
    assert graph.n_nodes == 5
    assert graph.n_edges == 5


def test_replicated_nodes():
    nodes = [1, 3, 3, 3, 5]
    edges = [(1, 1),
             (1, 1),
             (3, 3),
             (3, 5),
             (5, 5)]
    graph = Graph(list_nodes=nodes, list_edges=edges)
    assert graph.n_nodes == 3
    assert graph.n_edges == 4


def test_plot_hist_with_str():
    nodes_plot = [str(item) for item in range(1, 101)]
    edges_plot = [(str(randint(1, 100)), str(randint(1, 100))) for _ in range(12000)]
    graph_plot = Graph(list_nodes=nodes_plot, list_edges=edges_plot)
    graph_plot.plot_histogram_degree_out(n_bins=20)
    graph_plot.to_hdf5(file_name='ex.h5')
    graph_plot.read_hdf5(file_name='ex.h5')
    assert True
