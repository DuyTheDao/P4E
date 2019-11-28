# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh.readlines():
    line = line.upper().strip()
    print(line)
