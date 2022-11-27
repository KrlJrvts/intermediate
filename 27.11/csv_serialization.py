# import csv
# import random
#
# doc = "data.csv"
#
#
#
# # data = [
# #     ["cat", "dog", "rat"],
# #     ["audi", "BMW", "lada"],
# #     ["13", "18", "48"]
# # ]
#
# high_score = []
# score_headers = ["car, time", "place"]
# cars = ["audi", "BMW", "lada"]
# times = [10, 20, 30]
#
# high_score.append(score_headers)
#
# for i in range(10):
#     car = cars[random.randint(0, len(cars)-1)]
#     time_ = times[random.randint(0, len(times)-1)]
#     places = random.randint(1, 5)
#     score = [car, time_, places]
#     high_score.append(score)
#
#
# with open(doc, "a", newline="") as f:
#     writer = csv.writer(f)
#     for line in data:
#         writer.writerow(line)
#
# with open(doc, "r") as f:
#     for line in csv.reader(f):
#         print(line)


import csv
import random

file = "data.csv"

data = [
    ["cats", "dogs", "birds"],
    ["fish", "octopus", "shark"],
    [1, 2, 3, 4]
]
high_score = []
score_headers = ["car", "time", "place"]
cars = ["Audi", "BMW", "Porsche"]
times = [10, 15, 20]
high_score.append(score_headers)
for i in range(10):
    car = cars[random.randint(0, len(cars) - 1)]
    time_ = times[random.randint(0, len(times) - 1)]
    place = random.randint(1, 5)
    score = [car, time_, place]
    high_score.append(score)


with open(file, "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    for line in high_score:
        writer.writerow(line)

with open(file, "r") as f:
    for line in csv.reader(f):
        print(line)
