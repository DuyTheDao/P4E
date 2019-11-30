# Extracting Data from JSON

import json
import urllib.request, urllib.error, urllib.parse

url = 'http://py4e-data.dr-chuck.net/comments_333905.json'

data = urllib.request.urlopen(url).read()
info = json.loads(data)["comments"]

count = 0
for i in info:
  count += int(i['count'])

print("Scraping: " + url)
print("Scraped characters: " + str(len(data)))
print("Count: " + str(len(info)))
print("Total: " + str(count))
print("\nSubscribe to YouTube.com/madgans")
