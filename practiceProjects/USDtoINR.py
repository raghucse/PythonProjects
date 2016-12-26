import urllib.request
import json
import sys

#fetch latest currency rate
print(sys.argv)

base = sys.argv[1]
to = sys.argv[2]

u = urllib.request.urlopen("http://api.fixer.io/latest?base={}".format(base));

data = u.read()
print(data)
jsonData = json.loads(data)
print(jsonData["base"])
print("INR: ",jsonData["rates"][to])

#print(jsonData)