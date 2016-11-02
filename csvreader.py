import csv

with open('DEV_2014.csv') as dvt:
    lector = csv.DictReader(dvt)
    for item in dvt:
        print(item)