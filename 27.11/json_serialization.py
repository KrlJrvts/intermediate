import json

json_file = "data.json"

data = {
    "a": 1,
    "b": 2,
    "c": 3
}
# new_data = []
# for i in range (5):
#     new_data.append(data)
#
# with open(json_file, "w") as f:
#     json.dump(new_data, f, indent=2)


with open(json_file, "r") as f:
    in_data = json.load(f)

data_two = []
for i in range(len(in_data)):
    temp_dict = in_data[i]
    temp_dict["d"] = temp_dict.get("d", 69)
    data_two.append(temp_dict)

data_three = [x for x in in_data]
data_three[0]["a"] = 420


print(f"{in_data = }")
print(f"{in_data[2].get('b', 20) = }")
print(f"{in_data[3].get('d', 20) = }")

print(data_two)
print(data_three)
