#!/usr/bin/python

from googletrans import Translator
import argparse
import json
from files import cb
#translate
class tran:
    def __init__(self,inp,cod):
        self.trans = Translator()
        self.have = self.trans.translate(inp, dest=cod).text
        print (self.have)


#parse
parser = argparse.ArgumentParser(description="•Google translator• ketik -h untuk melihat cara")
parser.add_argument('-i', type=str, help='input your translate', metavar="[word]")
parser.add_argument('-c', type=str, help='input code language', metavar='[word]')
parser.add_argument('-s', help='show code language', metavar='[show]')
args = parser.parse_args()

if args.i:
    if args.c:
        tran(args.i,args.c)
    else:
        pass

elif args.s:
    load = json.loads(cb.bahasa().retr())
    print ('[code] : [asal]')
    for x in load:
        print (f'''
[{x}] : [{load[x].upper()}]''')

else:
    pass
