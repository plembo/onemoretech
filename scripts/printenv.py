#!/usr/bin/env python3
import sys
import os

print("Content-Type: text/html")
print()
for var in os.environ.keys():
    print ("{} = {}".format(var, os.environ[var]))
    print ("<br />")
