#!/usr/bin/python3.6
# Paged search, select output to LDIF formatted file
import os
from configparser import ConfigParser     
from ldap3 import Server, Connection, SUBTREE, ALL
from ldap3 import ObjectDef, AttrDef, Reader, Entry, Attribute

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
attrs = ['uid', 'displayname', 'mail', 'telephonenumber', 'mobile', 'street', 'l', 'st', 'postalcode', 'c', 'cn', 'ou']

server = Server(dirhost, port=dirport, use_ssl=True, get_info=ALL)
conn = Connection(server, user=diruser, password=dirpass, auto_bind=True, check_names=True)

total_entries = 0
searchParms = {
    'search_base': basedn,
    'search_filter': query,
    'search_scope': SUBTREE,
    'attributes': attrs,
    'paged_size': 100,
}

while True:
    conn.search (**searchParms)
    for entry in conn.entries:
        userdn = entry.entry_dn
        uid = entry.uid
        displayname = entry.displayname
        mail = entry.mail
        mobile = entry.mobile
        country = entry.c

        print('dn: ', userdn)
        print('uid: ', uid)
        print('displayname: ', displayname)
        print('mail: ', mail)
        print('mobile: ', mobile)
        print()
 
        total_entries += 1
    cookie = conn.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
    if cookie:
        searchParms['paged_cookie'] = cookie
    else:
        break
    

print(total_entries)
conn.unbind()

