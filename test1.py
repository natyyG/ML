import csv

# with open('./sampledata.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for line in csv_reader:
#         print(line[3])

with open('./newdata.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(['name', 'email', 'password'])
    csv_writer.writerow(['naruto', 'naruto@gmail.com', 'minatouzu'])