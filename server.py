import BaseHTTPServer
import sys, os, random


class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    vcr_counter = 0

    def do_GET(self):
        if self.path == '/scoreboard': 
            self.set_headers()
            contents = self.get_random_data('scoreboard')
            self.wfile.write(contents)
            return
        elif self.path == '/scoreboard/ticats':
            self.set_headers()
            contents = self.get_random_data('ticats_scoreboard')
            self.wfile.write(contents)
            return
        elif self.path == '/scoreboard/corrupted':
            self.set_headers()
            contents = self.get_corrupted_data('scoreboard')
            self.wfile.write(contents)
            return
        elif self.path == '/scoreboard/vcr':
            self.set_headers()
            contents = self.get_vcr_data('scoreboard')
            self.wfile.write(contents)
            return
        else:
            self.send_error(404)

    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()

    def get_random_data(self, module_json_dir_name):
        json_dir = 'JSON/' + module_json_dir_name
        file_name = random.choice(os.listdir(json_dir))
        open_file = open(json_dir + '/' +file_name)
        contents = open_file.read()
        open_file.close()
        return contents

    def get_corrupted_data(self, module_json_dir_name):
        json_dir = 'CORRUPTED_JSON/' + module_json_dir_name
        file_name = random.choice(os.listdir(json_dir))
        open_file = open(json_dir + '/' +file_name)
        contents = open_file.read()
        open_file.close()
        return contents

    def get_vcr_data(self, module_json_dir_name):
        json_dir = 'JSON/' + module_json_dir_name + '_vcr'
        files = sorted(os.listdir(json_dir))
        file_name = files[self.vcr_counter % len(files)]
        WebRequestHandler.vcr_counter = WebRequestHandler.vcr_counter + 1

        print("Buble's singing a tune: " + file_name)

        open_file = open(json_dir + '/' +file_name)
        contents = open_file.read()
        open_file.close()
        return contents
        

try:
    server = BaseHTTPServer.HTTPServer(('localhost',8017), WebRequestHandler)    
    print 'Buble starts singing his sweet stats songs.'
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
    print 'Buble has ended his set.'
