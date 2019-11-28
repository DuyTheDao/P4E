# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)

count = 0
avg = 0
total = 0

for line in fh:
    
    if not line.startswith("X-DSPAM-Confidence:"): continue
    pos = line.find("0")

    values = float(line[pos:].rstrip())

    count = count + 1
    total = total + values
    avg = total / count
print("Average spam confidence:", avg)
#print("Done")
