"""
AI Lab - Minimax and Alpha-Beta Pruning
Tree: depth 3, branching factor 2, 8 leaves. Root is a MAX node.
A tree is a nested list. A number is a leaf, a list is an internal node.
"""
import random
import copy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------- the tree (change this if your lab sheet has a different tree) ----------
TREE = [[[3, 5], [6, 9]],
        [[1, 2], [0, -1]]]

# ---------- counters ----------
minimax_leaves = 0
alphabeta_leaves = 0


def minimax(node, is_max):
    global minimax_leaves
    if not isinstance(node, list):          # leaf
        minimax_leaves += 1
        return node
    if is_max:
        best = float("-inf")
        for child in node:
            best = max(best, minimax(child, False))
        return best
    else:
        best = float("inf")
        for child in node:
            best = min(best, minimax(child, True))
        return best


def alphabeta(node, is_max, alpha, beta):
    global alphabeta_leaves
    if not isinstance(node, list):          # leaf
        alphabeta_leaves += 1
        return node
    if is_max:
        best = float("-inf")
        for child in node:
            best = max(best, alphabeta(child, False, alpha, beta))
            alpha = max(alpha, best)
            if alpha >= beta:               # prune
                break
        return best
    else:
        best = float("inf")
        for child in node:
            best = min(best, alphabeta(child, True, alpha, beta))
            beta = min(beta, best)
            if alpha >= beta:               # prune
                break
        return best


def run_both(tree):
    """Run both algorithms on a tree, return (value_mm, leaves_mm, value_ab, leaves_ab)."""
    global minimax_leaves, alphabeta_leaves
    minimax_leaves = 0
    alphabeta_leaves = 0
    v1 = minimax(tree, True)
    v2 = alphabeta(tree, True, float("-inf"), float("inf"))
    return v1, minimax_leaves, v2, alphabeta_leaves


# ---------- reordering helpers ----------
def value_of(node, is_max):
    """plain minimax without touching the counters (used only for sorting)"""
    if not isinstance(node, list):
        return node
    vals = [value_of(c, not is_max) for c in node]
    return max(vals) if is_max else min(vals)


def best_order(node, is_max):
    """MAX node: best child first. MIN node: smallest child first."""
    if not isinstance(node, list):
        return node
    kids = [best_order(c, not is_max) for c in node]
    kids.sort(key=lambda c: value_of(c, not is_max), reverse=is_max)
    return kids


def worst_order(node, is_max):
    """opposite of best order"""
    if not isinstance(node, list):
        return node
    kids = [worst_order(c, not is_max) for c in node]
    kids.sort(key=lambda c: value_of(c, not is_max), reverse=not is_max)
    return kids


def random_order(node, rng):
    if not isinstance(node, list):
        return node
    kids = [random_order(c, rng) for c in node]
    rng.shuffle(kids)
    return kids


def leaf_list(node):
    if not isinstance(node, list):
        return [node]
    out = []
    for c in node:
        out += leaf_list(c)
    return out


if __name__ == "__main__":
    print("=== Task 2: both algorithms on the supplied tree ===")
    v1, c1, v2, c2 = run_both(TREE)
    print("Minimax    value =", v1, " leaves evaluated =", c1)
    print("Alpha-beta value =", v2, " leaves evaluated =", c2)
    print("Same value?", v1 == v2)

    print("\n=== Task 3: reordering branches ===")
    results = {}
    results["Original"] = (TREE, run_both(TREE))
    b = best_order(TREE, True)
    results["Best order"] = (b, run_both(b))
    w = worst_order(TREE, True)
    results["Worst order"] = (w, run_both(w))

    print(f"{'Ordering':<12}{'Leaves in order':<30}{'MM val':<8}{'AB val':<8}{'MM leaves':<11}{'AB leaves'}")
    for name, (t, r) in results.items():
        print(f"{name:<12}{str(leaf_list(t)):<30}{r[0]:<8}{r[2]:<8}{r[1]:<11}{r[3]}")

    # 200 random shuffles
    rng = random.Random(1)
    counts = []
    all_same = True
    for _ in range(200):
        t = random_order(copy.deepcopy(TREE), rng)
        r = run_both(t)
        counts.append(r[3])
        if r[0] != r[2]:
            all_same = False
    print("\n200 random orderings: min AB leaves =", min(counts),
          " max =", max(counts), " average =", round(sum(counts) / len(counts), 2))
    print("Alpha-beta value always equal to minimax value?", all_same)

    # plot
    names = list(results.keys())
    ab = [results[n][1][3] for n in names]
    mm = [results[n][1][1] for n in names]
    x = range(len(names))
    plt.figure(figsize=(6, 4))
    plt.bar([i - 0.2 for i in x], mm, 0.4, label="Minimax")
    plt.bar([i + 0.2 for i in x], ab, 0.4, label="Alpha-beta")
    plt.xticks(list(x), names)
    plt.ylabel("Leaves evaluated")
    plt.title("Leaf evaluations for different branch orderings")
    plt.legend()
    plt.tight_layout()
    plt.savefig("leaf_counts.png", dpi=150)
    print("\nSaved plot: leaf_counts.png")
