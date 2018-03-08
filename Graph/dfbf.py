import sys

def read(fnm, db):
    """
    read file fnm into dictionary
    each line has a nodeName followed by its adjacent nodeNames
    """
    file = open(fnm)
    graph = {}  # dictionary
    for line in file:
        l = line.strip().split(" ")
        if db: print("l:", l, "len(l):", len(l))
        # remove empty lines
        if l == ['']:
            continue
        # dict: key: nodeName  value: (color, adjList of names)
        graph[l[0]] = ('white', l[1:])
    return graph


def dump(graph):
    print("dumping graph: nodeName (color, [adj list]) ")
    for node in graph:
        print(node, graph[node])


def bfs(graph, list):
    """
    breadth first search graph from root in list
    return list: array of tuples [(nodename, distance from root), ...]
    """
    # get first list of children
    que = []
    que.append(list[0][0])
    depth = 1
    while que:
        visited = False

        current = que.pop(0)
        # append the current node to the list
        children = graph[current][1]
        for c in children:
            if graph[c][0] == "white":
                c1 = graph[c][1]
                visited = True
                graph[c] = ("black", c1)
                list.append((c, depth))
                que.append(c)
        if visited:
            depth += 1

    return list


def white(graph):
    """
     paint all graph nodes white
    """
    for node in graph:
        gr[node] = ('white', gr[node][1])


def dfs(r):
    """  depth first left to right search dd from r for cycles
         if cycle found (grey node encountered) print( "cycle in", nodename)
    """
    # color our self grey
    gr[r] = ("grey", gr[r][1])
    for item in gr[r][1]:
        if gr[item][0] == "grey":
            print("cycle in " + item)
        if gr[item][0] == "white":
            dfs(item)

    gr[r] = ("black", gr[r][1])



if __name__ == "__main__":
    # db: debug flag
    db = len(sys.argv) > 3
    gr = read(sys.argv[1], db)
    root = sys.argv[2]
    if db:
        dump(gr)
    print("root key:", root)
    # don't need grey for bfs
    gr[root] = ('black', gr[root][1])
    q = bfs(gr, [(root, 0)])
    print("BFS")
    print(q)
    if db:
        dump(gr)
    white(gr)
    if db:
        dump(gr)
    print("DFS")
    dfs(root)
    if db: dump(gr)
