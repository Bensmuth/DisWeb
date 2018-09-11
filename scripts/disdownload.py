import requests
import os

def download(index):
    didconnect = False

    hosts = open("files/hosts.txt",'r')
    host = hosts.readline().splitlines() #removes \n at line end (also makes it easier to read from in later for loop)

    for x in range(len(host)):
        try:
        ##get main page
            for y in range(1, len(index)-1): ##removes first backslash and makes first level dir TODO: add more dir levels support
                if index[y] == "/":
                    index = index[1:]
                    if not os.path.exists(directory):
                        os.makedirs("scripts/WebServer/" + index[:y])

            url = ("http://" + str(host[x]) + "/" + str(index))
            r = requests.get(url, allow_redirects=True)
            open('scripts/WebServer/' + index, 'wb').write(r.content)
            didconnect = True

            ##get hosts file
            url = ("http://" + str(host[x]) + "/hosts.txt")
            h = requests.get(url, allow_redirects=True)
            open('files/hosts.txt', 'wb').write(h.content)

        except:
            pass

    hosts.close()
    if didconnect:
        print("A Host was found at: " + url)
