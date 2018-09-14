from http.server import BaseHTTPRequestHandler, HTTPServer
from shutil import copyfile
import disdownload

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
  # GET
    def do_GET(self):
        connected_ip = str(self.client_address[0])
        toapp = open("files/hosts.txt", "a")
        if connected_ip not in open("files/hosts.txt", "r").read():
            toapp.write(connected_ip + ":8080")



        ##copy current hosts file to WebServer Dir for download
        copyfile("files/hosts.txt", "scripts/WebServer/hosts.txt")


        # Send response status code
        self.send_response(200)
        getpath = self.path ##dont think this is in http.server documentation, probs in BaseHttpServer, find requested path

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # open file
        try:
            message = open("scripts/WebServer/" + getpath,'rb')

        except:
            try:
                disdownload.download(getpath)
                message = open("scripts/WebServer/" + getpath,'rb')
            except:
                message = open("scripts/WebServer/404.html", 'rb')


        # Write content as bytes
        self.wfile.write(message.read())
        message.close()

        return


def run():
  print('starting server...')

  server_address = ('127.0.0.1', 8081) ##used 8081 as no elevated perm is required
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
