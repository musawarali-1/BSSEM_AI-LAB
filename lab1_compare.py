
def rule_check(score, docs, attendance, record):
    if score >= 70 and docs and attendance >= 75 and not record:
    return "ELIGIBLE"
    return "NOT ELIGIBLE"


def weighted_check(score, docs, attendance, record):
    composite = 0.6 * score + 0.4 * attendance
    # documents and conduct are still must-have
    if docs and not record and composite >= 75:
     return "ELIGIBLE", composite
    return "NOT ELIGIBLE", composite


print("ID  Score  Att Rules  Weighted  Composite")
disagreements = []

with open("applicants.csv") as f:
    for row in csv.DictReader(f):
        score = float(row["score"])
        attendance = float(row["attendance_pct"])
        docs = row["documents_complete"] =="true"
        record = row["disciplinary_record"] =="true"

        a =rule_check(score, docs, attendance, record)
        b,composite = weighted_check(score, docs, attendance, record)

        print(row["id"], "  ", int(score), "   ", int(attendance), "  ", a.ljust(13), " ", b.ljust(13), " ", round(composite, 2))

        if a!= b:
            disagreements.append((row["id"], score, attendance, a, b, composite))
print()
print("Disagreements:", len(disagreements), "out of 12")
for d in disagreements:
    print(d[0], "score", int(d[1]), "attendance", int(d[2]), "-> rules:", d[3], "| weighted:", d[4], "(composite", round(d[5], 2), ")")
