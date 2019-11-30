#1

'''import urllib.request
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_333902.html'


html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')
tag = soup('span')
count = 0

for i in tag:
	count += int(i.contents[0])

print(count)
'''

#2

'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/known_by_Temilade.html'

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
counts = 0

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print('Retrieving: ' + tag.get('href', None))
    '''
#3
import urllib.request, urllib.parse, urllib.error
from bs4 import *
import ssl

current_count = 0
url = 'http://py4e-data.dr-chuck.net/known_by_Temilade.html'
repeat_count = int(input('Enter count: '))
pos = int(input('Enter position: '))

def get_html(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while current_count < repeat_count:
    print('Retrieving: ', url)
    tags = get_html(url)
    for index, item in enumerate(tags):
        if index == position - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    current_repeat_count += 1
print('Last Url: ', url)
