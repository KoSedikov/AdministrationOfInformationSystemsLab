
# Алгоритм поиска в глубину на Python

def dfs(graph, begin, visited=None):
    if visited is None:
        visited = set()
    visited.add(begin)

    print(begin)

    for next in graph[begin] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['4', '2']),
         '1': set(['1', '3']),
         '3': set(['2', '4'])}

dfs(graph, '0')