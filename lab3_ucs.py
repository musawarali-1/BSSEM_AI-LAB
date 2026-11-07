
import heapq

edges = [
    ("A", "B", 2),
    ("A", "C", 1),
    ("B", "D", 1),
    ("B", "E", 6),
    ("C", "F", 2),
    ("D", "E", 1),   
    ("E", "G", 5),
    ("F", "G", 7),
]


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "E"],
    "E": ["B", "D", "G"],
    "F": ["C", "G"],
    "G": ["E", "F"],
}


def weight(a, b):
    for x, y, w in edges:
        if (x == a and y == b) or (x == b and y == a):
            return w
    return None


def ucs(start, goal):
    counter = 0
    pq = [(0, counter, [start])]
    processed = []
    while len(pq) > 0:
        cost, c, path = heapq.heappop(pq)
        node = path[-1]
        if node in processed:
            print("skip", node, "with cost", cost, "(already processed)")
            continue
        processed.append(node)
        print("process", node, "cost", cost, "path", "-".join(path))
        if node == goal:
            return path, cost, processed
        for nxt in graph[node]:
            if nxt not in processed:
                counter = counter + 1
          heapq.heappush(pq, (cost + weight(node, nxt), counter, path + [nxt]))
    return None, None, processed


def bfs(start, goal):
    queue = [[start]]
    visited = [start]
    while len(queue) > 0:
        path = queue.pop(0)
        if path[-1] == goal:
         return path
        for nxt in graph[path[-1]]:
            if nxt not in visited:
       visited.append(nxt)
                queue.append(path + [nxt])
    return None


def path_cost(path):
    total = 0
    for i in range(len(path) - 1):
        total = total + weight(path[i], path[i + 1])
    return total


print("UCS from A to G")
path, cost, processed = ucs("A", "G")
print("UCS path       :", "-".join(path))
print("UCS returned cost :", cost)
print("Independent sum   :", path_cost(path))
print("Processing order  :", ", ".join(processed))
print()
b = bfs("A", "G")
print("BFS path (fewest hops) :", "-".join(b), "| hops", len(b) - 1)
print("BFS path cost        :", path_cost(b))
print("UCS path hops     :", len(path) - 1)
