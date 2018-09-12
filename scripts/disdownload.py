import requests
import os

def urlspliter(index): ##removes first backslash and makes first level dir TODO: add more dir levels support
    print("splitter")
    slash = 0
    index = index[1:]
    for y in range(0, len(index)):
        if index[y] == "/":
            slash = y
    if not os.path.exists("scripts/WebServer/" + index[:slash]):
        os.makedirs("scripts/WebServer/" + index[:slash])
    return index

def pagegrab(host, index, x):
    print("pagegrab")
    url = ("http://" + str(host[x]) + "/" + str(index))
    r = requests.get(url, allow_redirects=True)
    open('scripts/WebServer/' + index, 'wb').write(r.content)
    print("A Host was found at: " + url)

def hostgrab(host, x):     ##get hosts file
    print("hostgrab")
    url = ("http://" + str(host[x]) + "/hosts.txt")
    h = requests.get(url, allow_redirects=True)
    open('files/hosts.txt', 'wb').write(h.content)


def download(index):
    didconnect = False

    hosts = open("files/hosts.txt",'r')
    host = hosts.readline().splitlines() #removes \n at line end (also makes it easier to read from in later for loop)

    for x in range(len(host)):
        try:
            index = urlspliter(index)
            for x in range(len(host)):
                pagegrab(host,index,x)
                hostgrab(host,x)

        except Exception as e:
            print(e)
            pass

    hosts.close()
