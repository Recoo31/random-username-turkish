
from http.server import BaseHTTPRequestHandler
from os.path import join
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        with open(join('data', 'adlar.txt'), 'r') as ad:
            ad = ad.readlines()
        with open(join('data', 'soy.txt'), 'r') as soy:
            soy = soy.readlines()

        user1 = random.choice(ad)
        soy1 = random.choice(soy)

        olasilik = ['-','_']
         

        o1 = user1 +soy1 #adbudesem
        o2 = user1 #abdu
        o3 = user1+str(random.randint(0,81))#abdu31
        o4 = user1+random.choice(olasilik) +soy1#abdu-desem

        olasilik2 =[o1,o2,o3,o4]

        username1= random.choice(olasilik2)
        username2 = username1.replace("\n","")
        self.wfile.write(username2.encode())
        return
