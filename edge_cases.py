"""Edge case tests: both algorithms must give the same root value."""
from minimax_lab import run_both

tests = {
    "Single leaf":              7,
    "All leaves equal":         [[[4, 4], [4, 4]], [[4, 4], [4, 4]]],
    "All negative leaves":      [[[-3, -5], [-6, -9]], [[-1, -2], [-7, -8]]],
    "Skewed (one deep branch)": [[[1, 2], 3], 4],
    "Ties at root":             [[[5, 1], [5, 2]], [[5, 3], [5, 4]]],
}

for name, tree in tests.items():
    v1, c1, v2, c2 = run_both(tree)
    status = "OK" if v1 == v2 else "MISMATCH"
    print(f"{name:<26} minimax={v1:<4} (leaves {c1})  alphabeta={v2:<4} (leaves {c2})  {status}")
