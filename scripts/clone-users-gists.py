#!/usr/bin/env python3
""" Download all a user's github gists into pwd.
Code by Fedir RYKHTIK and saranicole, on
https://stackoverflow.com/questions/6724490/pull-all-gists-from-github.
Syntax updated to Python 3; take username from command line;
"""

import json
from subprocess import call
from urllib.request import urlopen
import os
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("user", help="Github user name")
args = parser.parse_args()
if args.user:
    gituser = args.user

perpage = 10.0
userurl = urlopen('https://api.github.com/users/' + gituser)
public_gists = json.load(userurl)
gistcount = public_gists['public_gists']
print("Found gists : " + str(gistcount))
pages = int(math.ceil(float(gistcount)/perpage))
print("Found pages : " + str(pages))

f = open('./contents.txt', 'w')

for page in range(pages):
    pageNumber = str(page + 1)
    print("Processing page number " + pageNumber)
    pageUrl = 'https://api.github.com/users/' + gituser  + '/gists?page=' \
    + pageNumber + '&per_page=' + str(int(perpage))
    u = urlopen(pageUrl)
    gists = json.load(u)
    startd = os.getcwd()
    for gist in gists:
        gistid = gist['id']
        gistdesc = gist['description']
        f.write(str(gistid) + ' ' + str(gistdesc) + '\n')
        gistUrl = 'git://gist.github.com/' + gistid + '.git'
        if os.path.isdir(gistid):
            os.chdir(gistid)
            call(['git', 'pull', gistUrl])
            os.chdir(startd)

        else:
            call(['git', 'clone', gistUrl])

f.close()

