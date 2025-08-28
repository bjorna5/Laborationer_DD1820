import csv

with open("kdrama.txt", mode="r") as dramafil:
    csvfile = csv.reader(dramafil, delimiter=",")
    next(csvfile)
    for line in csvfile:
        print(line)