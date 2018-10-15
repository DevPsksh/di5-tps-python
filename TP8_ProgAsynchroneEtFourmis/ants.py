
import json
import io

with io.open("ants_params.json") as file:
    data = json.load(file)

WIDTH = data["width"]
HEIGHT = data["height"]
ANT_COUNT = data["ant_count"]
ANTS = [
    (elem["color"], elem["follow_color"], elem["pg"], elem["pd"], elem["pt"], elem["move_type"], elem["ps"])
    for elem in data["ants"]
]

print(data)
