def bfs_list(graph):
    q = [0]
    values = []
    seen = {}

    while len(q):
        node = q.pop(0)
        values.append(node)
        seen[node] = True 
        connections = graph[node]
        for c in connections:
            if not seen[c]:
                q.append(c)

def dfs_list(graph, target, node, seen):
    if node == target: 
        return True    
    seen[node] = True 
    connections = graph[node]
    print(connections)
    for c in connections:
        if c not in seen:
            res = dfs_list(graph, target, c, seen)
            if res == True:
                return True 

    return False    
