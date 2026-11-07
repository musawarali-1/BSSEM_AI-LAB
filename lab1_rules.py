MIN_SCORE = 70
MIN_ATTENDANCE = 75

def check_student(score, documents_complete, attendance, has_disciplinary_record):
    # returns the decision and the reason
    reasons = []

    if score < MIN_SCORE:
        reasons.append("score" + str(score)+ " is less than " +str(MIN_SCORE))
    if not documents_complete:
        reasons.append("documents are not complete")

    if attendance < MIN_ATTENDANCE:  # rule 1: minimum_attendance
        reasons.append("attendance " + str(attendance) + "% is less than "+ str(MIN_ATTENDANCE) + "%")
    if has_disciplinary_record:  # rule 2: clean_conduct
        reasons.append("student has a disciplinary record")

    if len(reasons) == 0:
     return "ELIGIBLE","all rules passed"
    return "NOT ELIGIBLE", "; ".join(reasons)


# four test cases
tests = [
    ("T1 normal pass", (85, True, 90, False), "ELIGIBLE"),
    ("T2 fails minimum_attendance", (85, True, 60, False), "NOT ELIGIBLE"),
    ("T3 fails clean_conduct", (85, True, 90, True), "NOT ELIGIBLE"),
    ("T4 boundary, score is exactly 70", (70, True, 75, False), "ELIGIBLE"),
]

print("Lab 1 rule based checker")
print("(thresholds are synthetic lab assumptions)")
print()

for name, data, expected in tests:
    actual, reason = check_student(*data)
    print(name)
    print(" input    :", data)
    print(" expected :", expected)
    print(" actual   :", actual)
    print(" reason   :", reason)
    if actual == expected:
        print("  result   : match")
 else:
        print("  result : MISMATCH")
    print()
