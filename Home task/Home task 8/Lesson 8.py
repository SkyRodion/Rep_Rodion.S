# task 1

import csv

Uah_rate = 37.5

with open('test_file.csv', mode='r') as file:
    read = csv.reader(file)
    text = list(read)
  #  print(text[::1])

for row in text[1:]:
    for i in range(1, len(row)):
        row[i] = str(int(float(row[i]) * Uah_rate))

with open('salaries_uah.csv', mode='w') as file:
    write = csv.writer(file)
    write.writerows(text)