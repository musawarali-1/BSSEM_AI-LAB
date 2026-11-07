import heapq

edges = [
    ("S", "A", 2),
    ("S", "B", 4),
    ("A", "C", 2),
    ("A", "D", 4),
    ("B", "D", 1),
    ("C", "G", 5),
    ("D", "G", 5),
]

graph = {
    "S": ["A", "B"],
    "A": ["S", "C", "D"],
    "B": ["S", "D"],
    "C": ["A", "G"],
    "D": ["A", "B", "G"],
    "G": ["C", "D"],
}

h_original = {"S": 8, "A": 6, "B": 6, "C": 4, "D": 5, "G": 0}
h_zero = {"S": 0, "A": 0, "B": 0, "C": 0, "D": 0, "G": 0}


def weight(a, b):
    for x, y, w in edges:
        if (x == a and y == b) or (x == b and y == a):
            return w
    return None


def show_frontier(pq, h):
    items = sorted(pq)
    parts = []
    for f, order, g, path in items:
        parts.append(path[-1] + "(g" + str(g) + " h" + str(h[path[-1]]) + " f" + str(f) + ")")
    return ", ".join(parts)


def astar(start, goal, h):
    counter = 0
    pq = [(h[start], counter, 0, [start])]
    processed = []
    log = []
    stale = 0
    while len(pq) > 0:
        f, order, g, path = heapq.heappop(pq)
        node = path[-1]
        if node in processed:
            stale = stale + 1
            log.append("skip " + node + " (stale entry, g " + str(g) + ")")
            continue
        processed.append(node)
        log.append("process " + node + " | g " + str(g) + " | h " + str(h[node]) + " | f " + str(f) + " | path " + "-".join(path))
        if node == goal:
            log.append("goal processed, stop")
            return path, g, processed, log, stale
        for nxt in graph[node]:
            if nxt not in processed:
                counter = counter + 1
                g2 = g + weight(node, nxt)
                heapq.heappush(pq, (g2 + h[nxt], counter, g2, path + [nxt]))
        log.append("   frontier after: " + show_frontier(pq, h))
    return None, None, processed, log, stale


def path_cost(path):
    total = 0
    for i in range(len(path) - 1):
        total = total + weight(path[i], path[i + 1])
    return total


def true_costs(goal):
    dist = {}
    for n in graph:
        dist[n] = 1000
    dist[goal] = 0
    todo = list(graph.keys())
    while len(todo) > 0:
        best = todo[0]
        for n in todo:
            if dist[n] < dist[best]:
                best = n
        todo.remove(best)
        for nxt in graph[best]:
            if dist[best] + weight(best, nxt) < dist[nxt]:
                dist[nxt] = dist[best] + weight(best, nxt)
    return dist
