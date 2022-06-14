from graph_inait import Graph


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


def test_plot_hist():
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 1),
             (1, 2),
             (1, 3),
             (1, 5),
             (3, 4)]
    graph = Graph(list_nodes=nodes, list_edges=edges)
    graph.plot_histogram_degree_out()
    graph.to_hdf5(file_name='ex.h5')
    graph.read_hdf5(file_name='ex.h5')
    assert True
