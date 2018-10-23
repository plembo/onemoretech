# Download all my github gists into pwd.
# Code from https://stackoverflow.com/questions/6724490/pull-all-gists-from-github.

import json
import urllib
from subprocess import call
from urllib import urlopen
import os
import math
# USER = os.environ['USER']
USER = 'plembo'

perpage=30.0
userurl = urlopen('https://api.github.com/users/' + USER)
public_gists = json.load(userurl)
gistcount = public_gists['public_gists']
print "Found gists : " + str(gistcount)
pages = int(math.ceil(float(gistcount)/perpage))
print "Found pages : " + str(pages)

f=open('./contents.txt', 'w+')

for page in range(pages):
    pageNumber = str(page + 1)
    print "Processing page number " + pageNumber
    pageUrl = 'https://api.github.com/users/' + USER  + '/gists?page=' + pageNumber + '&per_page=' + str(int(perpage))
    u = urlopen (pageUrl)
    gists = json.load(u)
    startd = os.getcwd()
    for gist in gists:
        gistd = gist['id']
        gistUrl = 'git://gist.github.com/' + gistd + '.git' 
        if os.path.isdir(gistd):
            os.chdir(gistd)
            call(['git', 'pull', gistUrl])
            os.chdir(startd)
        else:
            call(['git', 'clone', gistUrl])
