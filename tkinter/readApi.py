#https://docs.python.org/3/library/json.html?highlight=json
import json
from urllib.request import urlopen


url = "https://pierre.lesacteursduweb.fr/api/quotes.json"

print(url)

# store the response of URL
response = urlopen(url)

# storing the JSON response from url in data
data_json = json.loads(response.read())

#json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
json.dumps(data_json);

#print(data_json)
#print(type(data_json))
#print(data_json[0])
#print(type(data_json[0]))
print("-> " + data_json[0]['data'])

exit(0)