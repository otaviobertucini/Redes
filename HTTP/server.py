# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
from socketserver import ThreadingMixIn
import threading
import time

hostName = "localhost"
serverPort = 8001

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):

        print('THREAD: ' + threading.currentThread().getName())

        # time.sleep(4)
        if('image.jpg' in self.path):

            self.send_response(200)
            self.send_header("Content-Type", "image/png")
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            f = open("image.jpg", "rb")
            self.wfile.write(f.read())

            return None

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        content = ''
        filename = 'error.html'
        if('index.html' in self.path):
            filename = 'index.html'
        with open(filename) as file:
            content = ''.join(file.readlines())

        self.wfile.write(bytes(str(content), "utf8"))


if __name__ == "__main__":
    webServer = ThreadedHTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")