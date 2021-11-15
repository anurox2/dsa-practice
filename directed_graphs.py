
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}


def dfs_traversal(graph, node, node_to_reach=None):
    current_node = node

    stack = [current_node]

    while (len(stack) > 0):
        print(f'Removing {stack[-1]} from {stack}')
        node_to_check = stack.pop(-1)
        if(node_to_reach is not None):
            if(node_to_reach == node_to_check):
                return True
        print(
            f'\tAt node {node_to_check}. It has child {graph[node_to_check]}')
        for nodes in graph[node_to_check]:
            stack.append(nodes)

        print(f'\tStack updated: {stack}')

    print(f'Graph traversed from {node} to {node_to_check}')
    if(node_to_reach is not None):
        return False


def bfs_traversal(graph, node, node_to_reach=None):
    
    
    current_node = node

    queue = [current_node]

    while(len(queue) > 0):
        print(f'Removing last element {queue[-1]} from {queue}')
        node_to_check = queue[-1]
        if(node_to_reach is not None):
            if(node_to_reach == node_to_check):
                return True

        queue = queue[:-1]

        print(
            f'\t At node {node_to_check}. It has child {graph[node_to_check]}')
        for nodes in graph[node_to_check]:
            queue.insert(0, nodes)

        print(f'\tQueue updated: {queue}')

    print(f'Graph traversed from {node} to {node_to_check}')
    if(node_to_reach is not None):
        return False


status = dfs_traversal(graph, 'c', 'b')
print(status)

# status = bfs_traversal(graph, 'b', 'a')
# print(status)
