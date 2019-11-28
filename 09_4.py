name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dict={}

for lines in handle:
    if lines.startswith("From "):
        words = lines.rstrip().split()
        emails = words[1]
        dict[emails] = dict.get(emails, 0) + 1
                   
email = None
count = None

for k, v in dict.items():
    if count is None or count < v:
        count = v
        email = k
print(email, count)
