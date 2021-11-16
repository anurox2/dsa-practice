
def explore(graph, current, visited):
    if(current in visited):
        return False

    visited.add(current)

    for item in graph[current]:
        explore(graph, item, visited)

    return True


def count_connected_components(graph):
    visited = set()
    component_count = 0

    for node in graph:
        result = explore(graph, node, visited)
        if(result):
            component_count += 1

    return component_count


def exploreSum(graph, current_node, visited):
    if(current_node in visited):
        return 0

    visited.add(current_node)
    count = 1

    for node in graph[current_node]:
        count += exploreSum(graph, node, visited)

    return count


def largest_component(graph):
    visited = set()

    max_size = 0

    for node in graph:
        size = exploreSum(graph, node, visited)
        max_size = max(max_size, size)

    return max_size


adj_list = {
    0: [8, 1, 5, 4],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}


print(count_connected_components(adj_list))

print(largest_component(adj_list))
