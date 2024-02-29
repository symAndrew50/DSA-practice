# Connected components

edges = [
    ['A', 'B'],
    ['A', 'C'],
    ['A', 'D'],
    ['B', 'E'],
    ['D', 'E'],
    ['F', 'H'],
    ['F', 'G'],
    ['I', 'J']
]
nodes = ['A','B','C','D','E','F','G','H','I','J','K']
graph = {}


def dfs(graph, node, visited):
    
    print(node)
    visited.add(node)

    for item in graph[node]:
        if item not in visited:
            dfs(graph,item,visited)


for key in nodes:
    graph[key] = []

for (u,v) in edges:
    graph[u].append(v)
    graph[u].append(u)

# print(graph)
visited = set()
answer = []
for item in nodes:
    if item not in visited:
        temp = dfs(graph,'A', visited)
        answer.append(temp)

print(answer)



