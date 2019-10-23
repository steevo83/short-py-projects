import sys
import csv

pipe, comma = sys.argv[1:]

with open(pipe, newline='') as fin:
    reader = csv.reader(fin, delimiter='|')
    rows = list(reader)
        
with open(comma, mode='wt', newline='') as fout:        
    writer = csv.writer(fout)
    writer.writerows(rows)