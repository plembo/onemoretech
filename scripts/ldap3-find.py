#!/usr/bin/python3.6
# Pages search with LDIF output
import os
from configparser import ConfigParser
from ldap3 import Server, Connection, SUBTREE

HOME = os.getenv('HOME')
CFGPATH = HOME + '/etc/admin.ini'

config = ConfigParser()
config.read(CFGPATH)

dirhost = config.get('ldap','ldap1_host')
diruser = config.get('ldap','ldap_user')
dirpass = config.get('ldap','ldap_pass')

dirport = 636
basedn = "dc=example,dc=com"
query = "(objectclass=*)"
attrs = ['*']

server = Server(dirhost, port=dirport, use_ssl=True)
c = Connection(server, user=diruser, password=dirpass, auto_bind=True)

total_entries = 0
entry_generator = c.extend.standard.paged_search(
    search_base=basedn,
    search_filter=query,
    search_scope=SUBTREE,
    attributes=attrs,
    paged_size = 100,
    generator = False
)
for entry in entry_generator:
    total_entries += 1

    ldif_output = c.response_to_ldif()

    print(ldif_output)

