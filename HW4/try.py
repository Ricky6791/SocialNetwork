import json
from urllib.request import urlopen

with urlopen("http://www.ucdenver.edu/pages/ucdwelcomepage.aspx") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['department']:
    name = item['name']['telephone']['url']
    print(name)