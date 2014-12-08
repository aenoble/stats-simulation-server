import BaseHTTPServer
import sys, os, random


class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/scoreboard': 
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.send_header('Access-Control-Allow-Origin','*')
            self.end_headers()
            contents = self.get_random_scoreboard_data()
            self.wfile.write(contents)
            return
        else:
            self.send_error(404)

    def get_random_scoreboard_data(self):
        json_dir = 'JSON'
        file_name = random.choice(os.listdir(json_dir))
        open_file = open(json_dir + '/' +file_name)
        contents = open_file.read()
        open_file.close()
        return contents
        

try:
    server = BaseHTTPServer.HTTPServer(('97.107.137.56',8017), WebRequestHandler)    
    server.serve_forever()
except KeyboardInterrupt:
    print 'Buble has ended his set.'
    server.socket.close()
