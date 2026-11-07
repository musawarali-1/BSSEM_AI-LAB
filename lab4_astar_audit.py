from lab4_astar import *


def audit(h, name):
    print("Heuristic audit -", name)
    true = true_costs("G")
    for n in ["S", "A", "B", "C", "D", "G"]:
        if h[n] <= true[n]:
            ok = "ok"
        else:
            ok = "OVERESTIMATE by " + str(h[n] - true[n])
        print("  ", n, "| h", h[n], "| true remaining cost", true[n], "|", ok)
    bad = 0
    for a, b, w in edges:
     if h[a] > w + h[b]:
            print("   consistency broken", a, "to", b, ":", h[a], ">", w, "+", h[b])
            bad = bad + 1
    if h[b] > w + h[a]:
            print("   consistency broken", b, "to", a, ":", h[b], ">", w, "+", h[a])
            bad = bad + 1
    if bad == 0:
        print("   consistency ok on every edge")
    print()


def run(name, h):
    print("RUN -", name)
    path, cost, processed, log, stale = astar("S", "G", h)
    for line in log:
        print("  ", line)
    print("  returned path        :", "-".join(path))
    print("  returned cost        :", cost)
    print("  independent cost sum :", path_cost(path))
    print("  processed nodes      :", ", ".join(processed))
    print("  expansion count      :", len(processed), "(goal counted, stale skipped not counted)")
    print("  stale entries skipped:", stale)
    print()


print("TASK 1 and 2 - heuristic audit and runs")
print()
audit(h_original, "original heuristic")
run("A* with the original heuristic", h_original)
run("UCS (zero heuristic)", h_zero)

print("TASK 3 - one heuristic value changed")
print("h(C) original 4, modified 10, true remaining cost of C is", true_costs("G")["C"])
print()
h_bad = dict(h_original)
h_bad["C"] = 10
audit(h_bad, "modified h(C)=10")
run("A* with h(C)=10", h_bad)

print("EXTRA - small overestimate h(C)=6")
h_small = dict(h_original)
h_small["C"] = 6
run("A* with h(C)=6", h_small)
