import csv

def writecsv():
    file_name = input("Write the name of your csv file: ")
    with open(file_name, 'w') as csv_file:
        write_csv = csv.writer(csv_file, delimiter =",")
        csv_header = input("Enter the header of your csv files separated by space: ")
        header_list = csv_header.split(" ")
        write_csv.writerow(header_list)
        print("Now Enter the data you want to put in your file one row at a time Enter '0' when finishing")
        x = 1
        while (x == 1):
            data = input("Enter the data: ")
            if (data == "0"):
                x = 0
                break
                
            else:
                data_list = data.split(" ")
                write_csv.writerow(data_list)
               
def readcsv():
    file_name = input("Enter the name of the file you want to read: ")
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            print(line)
        filter = int(input("Enter the number of the column you want to separate: "))
        for lines in csv_reader:
            print(line[filter])
        




print("What do you want to do")
print("1. Write file to the csv file")
print("2. Read file to the csv file")


choice = input("Choice: ")

if (choice == "1"):
    writecsv()
elif (choice == "2"):
    readcsv()
else:
    print("wrong input Program terminated rerun")
