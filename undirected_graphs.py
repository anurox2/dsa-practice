edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
]


def create_adj_list(edge_list):
    """This function takes in an edge list and returns
    an adjacency list

    :param edge_list: List of edges connected to each other
    :return: Return an adjacency list in dict form
    """
    graph = {}

    for edge in edge_list:
        if(edge[0] not in graph):
            graph[edge[0]] = []
        if(edge[1] not in graph):
            graph[edge[1]] = []

        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph


def hasPath(graph, src, dst, visited):
    """This function takes in a graph, a source node, a destination
    node, and a set of visited nodes. It recursively checks
    if the src node has a path to the dst node.

    :param graph: Adjacency list
    :param src: Source node
    :param dst: Destination node
    :param visited: A set of nodes which have been travelled to
    :return: True or False
    """
    if(src == dst):
        return True

    if(src in visited):
        return False

    visited.add(src)

    for item in graph[src]:
        if(hasPath(graph, item, dst, visited)):
            return True

    return False


def undirected_path(edge_list, nodeA, nodeB):
    """This function creates an adjacency list and figures out
    if there's a path between node A and node B (Undirected Graph)
     - The graph can have cycles

    :param edge_list: List of connected edges
    :param nodeA: Source node
    :param nodeB: Destination node
    :return: True or False
    """
    graph = create_adj_list(edge_list)
    visited = set()
    return hasPath(graph, nodeA, nodeB, visited)


print(undirected_path(edges, 'o', 'n'))
