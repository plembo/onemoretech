#!/usr/bin/env python3
""" 
Download all a user's github gists into pwd.
Code by Fedir RYKHTIK and saranicole, on
https://stackoverflow.com/questions/6724490/pull-all-gists-from-github.
Syntax updated to Python 3; take username from command line; fix
logging to file (include id and description)
Refactored by P Lembo 2019/03/31
"""

import json
from subprocess import call
from urllib.request import urlopen
import os
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--user", help="Github user name")
parser.add_argument("--path", default=".", help="Output path")
args = parser.parse_args()
if args.user:
    gituser = args.user
if args.path:
    outpath = args.path

perpage = 75.0
userurl = urlopen('https://api.github.com/users/' + gituser)
public_gists = json.load(userurl)
gistcount = public_gists['public_gists']
print("Found gists : " + str(gistcount))
pages = int(math.ceil(float(gistcount)/perpage))
print("Found pages : " + str(pages))

if os.path.isdir(outpath):
    os.chdir(outpath)
else:
    try:
        os.mkdir(outpath)
        os.chdir(outpath)
    except OSError:
        print("Creation of directory %s failed" % outpath)

f = open('contents.txt', 'w')

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
