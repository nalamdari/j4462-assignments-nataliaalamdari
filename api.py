# 1. openstates.org/api/v1/legislators/?state=mo&active=true

# 2. openstates.org/api/v1/bills/?state=mo&chamber=upper&search_window=session:2016

# 3. openstates.org/api/v1/bills/?state=mo&chamber=upper&search_window=session:2016&subjects=guns
import json, requests

url = 'http://openstates.org/api/v1/bills/?state=mo&search_window=session:2016&subject=Immigration'

r = requests.get(url)

response_data = r.content

data = json.loads(response_data)

for item in data: 
    url_id = ['id']
    r2 = requests.get('http://openstates.org/api/v1/bills/' + 'url_id')
    response_data2 = r.content
    data2 = json.loads(response_data2)

for item in data:
    print item ['bill_id']
    print item ['title']
    for item in data2:
        if item ['actions']['date'] is item ['action_dates']['last']:
            print item ['actions']['action']

