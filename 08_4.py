fname = input("Enter file name: ")
fh = open(fname)

lst = []
lines = [line.split() for line in fh]

for line in lines:
    for word in line:
        if word not in lst:
            lst.append(word)
            
lst.sort()
print(lst)

