from lab2_percepts import load_percepts, flicker_percepts
from lab2_model import ReflexAgent, StatefulAgent

print("Lab 2 trace (limits 18 and 26 are synthetic lab assumptions)")
print()

reflex = ReflexAgent()
stateful = StatefulAgent()
reflex_count = 0
stateful_count = 0
all_ok = True

step = 1
for p in load_percepts():
    previous = stateful.previous_mode         
    target, send = stateful.act(p)
    r_target, r_send = reflex.act(p)

    if r_send:
     reflex_count = reflex_count + 1
    if send:
     stateful_count = stateful_count + 1
    if send:
     outcome = "SEND command " + target
    else:
        outcome = "no command"

    ok = (target == p["expected_target"]) and (send == p["expected_send"])
    if not ok:
        all_ok = False

    print("Step", step, "-", p["label"])
    print("  previous mode :", previous)
    print("  percept   : temperature", p["temperature"], "occupied", p["occupied"])
    print("  target mode :", target)
    print("  stateful  :", outcome)
    print("  reflex  : SEND command", r_target)
    print("  check  :", "match" if ok else "MISMATCH")
    print()
    step = step + 1

print("Reflex agent commands  :", reflex_count)
print("Stateful agent commands:", stateful_count)
print("All checks matched" if all_ok else "SOME CHECKS MISMATCHED")

# edge case, temperature goes up and down around the lower limit
print()
print("Edge case - sensor going up and down around 18")
edge = StatefulAgent()
for p in flicker_percepts():
 previous = edge.previous_mode
target, send = edge.act(p)
 print("  previous", previous, "| temperature", p["temperature"], "| target", target, "|", "SEND" if send else "no command")
