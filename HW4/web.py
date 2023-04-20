import requests
from bs4 import BeautifulSoup
import json

#url = "https://old.reddit.com/top/"
url = "http://www.ucdenver.edu/pages/ucdwelcomepage.aspx"
#download the URL and extract
#request = requests.get(url)
#html = urllib.request.urlopen(request).read()
headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.3'}
request = requests.get(url,headers=headers)
soup = BeautifulSoup(request.content, 'html.parser')
links = soup.find_all('script', type='application/ld+json')
extracted = []
for script in links:
    extracted.append(script.contents[0])
#print(extracted)
data = json.loads(extracted[0])
with open('data.json', 'w') as outfile:
    json.dump(data['department'][0]['name'], outfile, indent=2)
    outfile.write('\n')
    json.dump(data['department'][0]['telephone'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][0]['url'],outfile,indent=2)
    outfile.write('\n')
    outfile.write('\n')
    json.dump(data['department'][1]['name'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][1]['url'],outfile,indent=2)
    outfile.write('\n')
    outfile.write('\n')
    json.dump(data['department'][2]['name'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][2]['telephone'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][2]['url'],outfile,indent=2)
    outfile.write('\n')
    outfile.write('\n')
    json.dump(data['department'][3]['name'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][3]['telephone'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][3]['url'],outfile,indent=2)
    outfile.write('\n')
    outfile.write('\n')
    json.dump(data['department'][4]['name'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][4]['url'], outfile, indent=4)
    outfile.write('\n')
    outfile.write('\n')
    json.dump(data['department'][5]['name'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][5]['telephone'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][5]['url'],outfile,indent=2)
    outfile.write('\n')
    outfile.write('\n')
    json.dump(data['department'][6]['name'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][6]['telephone'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][6]['url'],outfile,indent=2)
    outfile.write('\n')
    outfile.write('\n')
    json.dump(data['department'][7]['name'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][7]['telephone'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][7]['url'],outfile,indent=2)
    outfile.write('\n')
    outfile.write('\n')
    json.dump(data['department'][8]['name'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][8]['telephone'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][8]['url'],outfile,indent=2)
    outfile.write('\n')
    outfile.write('\n')
    json.dump(data['department'][9]['name'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][9]['telephone'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][9]['url'],outfile,indent=2)
    outfile.write('\n')
    outfile.write('\n')
    json.dump(data['department'][10]['name'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][10]['telephone'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][10]['url'],outfile,indent=2)
    outfile.write('\n')
    outfile.write('\n')
    json.dump(data['department'][11]['name'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][11]['telephone'],outfile,indent=2)
    outfile.write('\n')
    json.dump(data['department'][11]['url'],outfile,indent=2)


# extracted = []
# for script in links:
#     name = script.text
#     telephone = script.text
#     url = script.get('href','')
#     if not url.startswith('http'):
#         url = "ucdenver.edu"+url
#
#     record = {'name': name, 'telephone': telephone, 'url': url}
#     res = json.loads(telephone)
#     extracted.append(res)
# with open('data.json', 'w') as outfile:
#      json.dump(extracted, outfile, indent=4)
# for i in extracted:
#     dict = json.loads(i)
#     print(dict["name"])
#data = json.loads(soup.find('script', type='application/ld+json').text)
#print(data['department'][5]['address'])
#pass the HTML to Beautifulsoup
#soup = BeautifulSoup(request.string, 'html.parser')
#get the html of the table called site Table where all the links are displayed
#main_table = soup.find("div", attrs={'id':'siteTable'})
#now we go into main_table and get every element in it which has a class "title"
#links = main_table.find_all('a',class_="title")
#things = soup.find_all('script', class_ = "title")
#from each link extract the text of the link and the link itsel
#List to store a dict of the data we extracted
# extracted_records = []
# for link in things:
#     title = link.text
#     url = link['href']
#     if not url.startswith('http'):
#         url = "https://reddit.com"+url
#     record = {'title': title, 'url': url}
#     extracted_records.append(record)
# print(extracted_records)
# with open('data.json', 'w') as outfile:
#     json.dump(extracted_records, outfile, indent=4)

