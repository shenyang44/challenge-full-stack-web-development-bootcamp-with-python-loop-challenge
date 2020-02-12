info = [
    ["name", "age", "pet"],
    ["Amy", "20", "bird"],
    ["John", "21", "cat"],
    ["Ash", "24", "dog"],
]

class_info = {}

keys = info.pop(0)

for i in range(0, len(info)):
    new_row = {i: dict.fromkeys(keys)}
    for j in range(len(keys)):
        new_row[i][keys[j]] = info[i][j]

    class_info.update(new_row)

print(class_info)
