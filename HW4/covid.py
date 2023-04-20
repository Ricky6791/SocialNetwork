import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import HTML

url = 'https://covid19.colorado.gov/data'
headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.3'}
request = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(request).read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', attrs={'dir': "ltr"})
rows = []
for row in table.findAll('tr'):
    headers = []
    for header in row.findAll('td'):
        text = header.text
        headers.append(text)
    rows.append(headers)
stuff = pd.DataFrame(data=rows)
stuff_transposed = stuff.T

file1 =open("extraCredit.md", "w")
file1.write(stuff_transposed.to_html())
file1.close()

