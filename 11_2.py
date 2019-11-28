# http://py4e-data.dr-chuck.net/regex_sum_333900.txt

import re

fopen = open("text.txt")
list = []

for line in fopen:
    line = line.rstrip()
    parse = re.findall("([0-9]+)", line)

    if len(parse) < 1:
        continue

    for word in range(len(parse)):
        number = float(parse[word])
        list.append(number)
        
print(sum(list))
