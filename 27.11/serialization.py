import pickle

data = {
    "a": [1, 2.0, 3],
    "b": ("This lesson", "is for", "serialization"),
    "c": [False, True, False]
}

with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

with open("data.pickle", "rb") as f:
    data = pickle.load(f)


data.close()

print(data)
