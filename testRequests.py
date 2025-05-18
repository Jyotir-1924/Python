import requests

r = requests.get('https://api.github.com/events')

print(r.text)

with open("Req_Print.txt" , "w") as f:
    f.write(r.text)