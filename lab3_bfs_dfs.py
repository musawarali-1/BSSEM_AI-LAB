

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "G"],
    "F": ["C", "G"],
    "G": ["E", "F"],
}


def show(items):
   
    names = []
    for p in items:
        names.append(p[-1])
    return "[" + ", ".join(names) + "]"


def bfs(start, goal):
    queue = [[start]]
    visited = [start]
    order = []
    step = 1
    while len(queue) > 0:
        path = queue.pop(0)
        node = path[-1]
        order.append(node)
        print("Step", step, "- process", node, "- path", "-".join(path))
        if node == goal:
            print("  goal reached, stop")
            return path, order
        for nxt in graph[node]:
            if nxt not in visited:
                visited.append(nxt)
                queue.append(path + [nxt])
        print("  queue after", show(queue))
        step = step + 1
    return None, order


def dfs(start, goal):
    stack = [[start]]
    processed = []
    order = []
    step = 1
    while len(stack) > 0:
        path = stack.pop()          
        node = path[-1]
        if node in processed:
            continue
        processed.append(node)
        order.append(node)
        print("Step", step, "- process", node, "- path", "-".join(path))
        if node == goal:
            print("  goal reached, stop")
            return path, order
       
        for nxt in reversed(graph[node]):
            if nxt not in processed:
                stack.append(path + [nxt])
        print("  stack after (top is last)", show(stack))
 step = step + 1
    return None, order


print("BFS (start A, goal G)")
path, order = bfs("A", "G")
print("Final path   :", "-".join(path))
print("Visit order  :", ", ".join(order))
print()
print("DFS (start A, goal G)")
path, order = dfs("A", "G")
print("Final path   :", "-".join(path))
print("Visit order  :", ", ".join(order))
