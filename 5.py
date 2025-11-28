import json

data = [

    {"name": "Akbota", "grade": 100},

    {"name": "Balsulu", "grade": 90},

    {"name": "Ayanat", "grade": 80}

]

with open("data.json", "w", encoding="utf-8") as f:

    json.dump(data, f, ensure_ascii=False, indent=4)

scores = [item["grade"] for item in data]

print(f"Average grade: {sum(scores)/len(scores)}")