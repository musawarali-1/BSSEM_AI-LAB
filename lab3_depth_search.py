
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
   "E": ["B", "G"],
    "F": ["C", "G"],
    "G": ["E", "F"],
}


def dls(node, goal, limit, path, visited):
    visited.append(node)             
 if node == goal:
        return "FOUND", path
 if limit == 0:
        return "CUTOFF", None
    cutoff = False
    for nxt in graph[node]:
        if nxt in path:              
            continue
        status, result = dls(nxt, goal, limit - 1, path + [nxt], visited)
        if status == "FOUND":
            return status, result
        if status == "CUTOFF":
            cutoff = True
    if cutoff:
        return "CUTOFF", None
    return "FAILURE", None


def iddfs(start, goal, max_depth):
    attempted = []
    total = 0
    status = "FAILURE"
    for limit in range(0, max_depth + 1):
        visited = []
        status, path = dls(start, goal, limit, [start], visited)
        attempted.append(limit)
        total = total + len(visited)
        print("    limit", limit, "->", status, "| nodes visited", len(visited), "|", "-".join(visited))
        if status == "FOUND":
            return status, path, attempted, total
    return status, None, attempted, total


print("DLS from A to G")
for limit in [1, 2, 3, 4]:
    visited = []
    status, path = dls("A", "G", limit, ["A"], visited)
    if path is None:
        p = "none"
    else:
        p = "-".join(path)
    print("limit", limit, "| status", status, "| path", p, "| visit order", "-".join(visited))

print()
print("IDDFS from A to G")
for m in [1, 2, 3, 4]:
    print("max depth", m)
    status, path, attempted, total = iddfs("A", "G", m)
    if path is None:
        p = "none"
    else:
        p = "-".join(path)
    print("  result", status, "| path", p, "| limits attempted", attempted, "| total nodes visited", total)
