import BaseHTTPServer
import sys, os, random, re


class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    vcr_counter = 0
    linescore_counter = 0
    leaders_counter = 0
    headtohead_counter = 0
    playbyplay_counter = 0
    teamplayerstats_counter = 0

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
        elif self.path == '/scoreboard/ticats/mugsy':
            self.set_headers()
            contents = self.get_vcr_data('mugsy_ticats_scoreboard')
            self.wfile.write(contents)
            return
        elif self.path == '/scoreboard/ticats/real':
            self.set_headers()
            contents = self.get_vcr_data('real_ticats_scoreboard')
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
        elif self.path == '/boxscore/linescore':
            self.set_headers()
            contents = self.get_vcr_data('line_score', self.linescore_counter)
            WebRequestHandler.linescore_counter = WebRequestHandler.linescore_counter + 1
            self.wfile.write(contents)
            return
        elif self.path == '/boxscore/leaders':
            self.set_headers()
            contents = self.get_vcr_data('game_leaders', self.leaders_counter)
            WebRequestHandler.leaders_counter = WebRequestHandler.leaders_counter + 1
            self.wfile.write(contents)
            return
        elif self.path == '/boxscore/head_to_head':
            self.set_headers()
            contents = self.get_vcr_data('head_to_head',
                    self.headtohead_counter)
            WebRequestHandler.headtohead_counter = WebRequestHandler.headtohead_counter + 1
            self.wfile.write(contents)
            return
        elif self.path == '/boxscore/play_by_play':
            self.set_headers()
            contents = self.get_vcr_data('play_by_play',
                    self.playbyplay_counter)
            WebRequestHandler.playbyplay_counter = WebRequestHandler.playbyplay_counter + 1
            self.wfile.write(contents)
            return
        elif self.path == '/boxscore/team_player_stats':
            self.set_headers()
            contents = self.get_vcr_data('team_player_stats', self.teamplayerstats_counter)
            WebRequestHandler.teamplayerstats_counter = WebRequestHandler.teamplayerstats_counter + 1
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

    def get_vcr_data(self, module_json_dir_name, counter):
        json_dir = 'JSON/' + module_json_dir_name + '_vcr'
        files = self.natural_sort(os.listdir(json_dir))

        if counter:
            file_name = files[counter % len(files)]
        else:
            file_name = files[self.vcr_counter % len(files)] 
            WebRequestHandler.vcr_counter = WebRequestHandler.vcr_counter + 1

        print("Buble's singing a tune: " + file_name)

        open_file = open(json_dir + '/' +file_name)
        contents = open_file.read()
        open_file.close()
        return contents

    #http://stackoverflow.com/questions/4836710/does-python-have-a-built-in-function-for-string-natural-sort
    @staticmethod
    def natural_sort(l): 
        convert = lambda text: int(text) if text.isdigit() else text.lower() 
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
        return sorted(l, key = alphanum_key)

        

try:
    server = BaseHTTPServer.HTTPServer(('localhost',8017), WebRequestHandler)    
    print 'Buble starts singing his sweet stats songs.'
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
    print 'Buble has ended his set.'
