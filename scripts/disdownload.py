import requests


hosts = open("files/hosts.txt",'r')
host = hosts.readline().splitlines()
print("host: " + host[0])

url = ("http://" + str(host[0]) + "/")
print("url: " + url)
r = requests.get(url, allow_redirects=True)
open('scripts/WebServer/index.html', 'wb').write(r.content)

hosts.close()
