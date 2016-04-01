import requests
import json

print "downloading with requests"
username = raw_input("username: ")
response = requests.get('https://api.github.com/users/'+ username)
print response.status_code
pic_json = json.loads(response.content)
pic = str(pic_json["avatar_url"])
poza = requests.get(pic)
with open("poza.jpg","wb") as code:
    code.write(poza.content)
