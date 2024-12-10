# Create a file - check for it's existence
# if exists, throw error
# if not, create a file with rw permission in the present folder
# Capture the content from a website in text

import html2text
import urllib.request
import os

'''
with urllib.request.urlopen("http://www.msnbc.com") as r:
    html_content = r.read()
rendered_content = html2text.html2text(html_content)
file = open('URL.txt', 'w')
file.write(rendered_content)
file.close()

'''

import sys
if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen
# Your code where you can use urlopen
with urlopen("https://www.ibm.com/products?ibmTopics[0][0]=cat.topic%3AAnalytics") as r:
    s = r.read().decode('utf-8')
#rendered_content = html2text.html2text(html_content)
rendered_content = html2text.html2text(s)
file = open('URL.txt', 'w')
file.write(rendered_content)
file.close()