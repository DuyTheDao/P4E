name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dict = {}

for lines in handle:
    if lines.startswith("From") and len(lines.split()) > 2:
        line = lines.split()
        
        if not dict.has_key(line[5][:2]):
            dict[line[5][:2]] = 1
            
        else:
            dict[line[5][:2]] += 1
                
keys = sorted(dict)

for items in keys:
    print(items, dict[items])
