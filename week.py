import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
     data=json.load(response)
clist = data["result"]["results"]
with open("open.txt","w",encoding="utf-8") as file:
     for information in clist:
          pic= "http"+information["file"].split("http")[1]
          file.write(information["stitle"]+","+information["longitude"]+","+pic+"\n")