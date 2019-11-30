import urllib.request, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_333904.xml'
print("Retrieving: " + url)

xml = urllib.request.urlopen(url).read()
print("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print("Count: " + str(len(counts)))

counter = 0

for count in counts:
    counter += int(count.text)

print ("Sum: " + str(counter))
