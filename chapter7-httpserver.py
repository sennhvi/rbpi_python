import http.server
import os

os.chdir("/home/sennhvi/RaspberryPi/RbPi_Python/LearnPythonRbPi")
httpd = http.server.HTTPServer(('127.0.0.1', 8444),
                               http.server.SimpleHTTPRequestHandler)
httpd.serve_forever()
