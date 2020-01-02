import csv

with open('C:/Users/sormosi/Desktop/Projects/csv_columns.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)