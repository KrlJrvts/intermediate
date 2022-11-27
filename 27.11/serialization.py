import pickle

data = {
    "a": [1, 2.0, 3],
    "b": ("this lesson", "is for", "Serialization"),
    "c": [False, True, False]
}

with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

print(data)
