#!/usr/bin/python3.6
# Simple search with JSON output
import os
from configparser import ConfigParser
from ldap3 import Server, Connection, SUBTREE, ALL

HOME = os.getenv('HOME')
CFG = HOME + '/etc/admin.ini'

config = ConfigParser()
config.read(CFG)

dirhost = config.get('ldap','ldap1_host')
diruser = config.get('ldap','ldap_user')
dirpass = config.get('ldap','ldap_pass')
dirport = 389
basedn = "dc=example,dc=com"
query = "(objectclass=*)"
attrs = ['uid', 'givenname', 'sn', 'displayname', 'street',
        'l', 'st', 'c', 'postalcode', 'mail', 'mobile', 'cn', 'ou']

server = Server(dirhost, port=dirport)
conn = Connection(server, user=diruser, password=dirpass, auto_bind=True)

result = conn.search(search_base=basedn,
         search_filter=query,
         search_scope=SUBTREE,
         attributes=attrs
         )

output = conn.response_to_json()
print(output)

