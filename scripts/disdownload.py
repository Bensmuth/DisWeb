import requests


hosts = open("files/hosts.txt",'r')
host = hosts.readline(1)


url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
open('google.ico', 'wb').write(r.content)
