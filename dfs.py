
# Алгоритм поиска в глубину на Python

# Сам алгоритм dfs
def dfs(graph, begin, visited=None):
    if visited is None:
        visited = set()
    visited.add(begin)

    print(begin)
    i = 0
    for next in graph[begin] - visited:
        try: # обработка исключений
            dfs(graph, next, visited)
            i +=1 # Подсчет проходов.
        except: print('none Value Exception')
    return visited, i

# наш граф
graph = {'0': set(['4', '2']),
         '1': set(['1', '3']),
         '3': set(['2', '4'])}

dfs(graph, '0') # Вызов функции (для проверки)123