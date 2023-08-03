def find_paths(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_paths(graph, node, end, path)
            for m in new_paths:
                paths.append(m)
    return paths


g = {
    'A': ['B', 'C'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
s = 'A'
e = 'F'
p = find_paths(g, s, e)
print("Все пути от", s, "до", e, ":", p)