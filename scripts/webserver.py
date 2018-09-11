from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # open file
        message = open("scripts/WebServer/index.html",'r')

        # Write content as utf-8 data
        self.wfile.write(bytes(message.read(), "utf8"))
        return


def run():
  print('starting server...')

  server_address = ('127.0.0.1', 8080) ##used 8080 as no root is required
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
