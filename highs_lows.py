import csv

#Get high temperature from file.
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
#    print(header_row)


    highs = [int(row[1]) for row in reader]
    print(highs)
    
#    for index, column_header in enumerate(header_row):
#        print(index, column_header)
