import csv
def load_percepts(filename="percepts.csv"):
percepts=[]
    with open(filename) as f:
     for row in csv.DictReader(f):
     item = {}
    item["label"] = row["label"]
    item["temperature"] = float(row["temperature"])
    item["occupied"] = row["occupied"] == "true"
    item["expected_target"] = row["expected_target"]
     item["expected_send"] = row["expected_send"] == "true"
     percepts.append(item)
    return percepts

def flicker_percepts():
    temps = [17.9, 18.0, 17.9, 18.0, 17.9]
    result = []
    for t in temps:
   result.append({"label": "flicker", "temperature": t, "occupied": True})
    return result
