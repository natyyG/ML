import csv

with open('./sampledata.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        print(line)