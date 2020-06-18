import json

with open('Json-2020-Jun-18__17_23_55.json') as json_data:
    jsonData =json.load(json_data)

for i in jsonData:
    print('\n')
    print(i['Date'])
    print('\t')
    print(i['Heading'])
