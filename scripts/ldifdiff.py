#!/usr/bin/python3.6
# Fork of https://github.com/norihiro/ldifdiff to run under
# python 3. Modified 2018/01/11 by P Lembo

import base64
flag_binary=0

class EOFException(Exception):
	pass

def read_line(file):
	while True:
		line = file.readline()
		if not line:
			raise EOFException
		if line[0]!='#':
			return line.rstrip('\n')

def parse_line(line):
	if line[0]==' ':
		return (None, line[1:])
	pos = line.find(':')
	if pos:
		if flag_binary and line[pos+1] == ':':
			return (line[:pos], ": "+base64.standard_b64decode(line[pos+2:]))
		else:
			return (line[:pos], line[pos:])
	else:
		raise ValueError

def read_dn(file):
	line_dn = read_line(file)
	if not line_dn:
		return read_dn(file)
	dn = parse_line(line_dn);
	d = list()
	try:
		while True:
			line = read_line(file)
			if not line: break
			pair = parse_line(line)
			if pair[0]:
				d.append(pair)
			else:
				kv = d[-1]
				d[-1] = (kv[0], kv[1]+pair[1])
	except EOFException:
		pass
	d.sort()
	return (dn[1], d)

def read_ldif(file):
	d = dict()
	try:
		while True:
			entry = read_dn(file)
			d[entry[0]] = entry[1]
	except EOFException:
		pass
	return d

def count_key(kv):
	d = dict()
	for k,v in kv:
		if k in d:
			d[k] += 1
		else:
			d[k] = 1
	return d

def makeldif_modify(dn, kv1, kv2):
	keycount1 = count_key(kv1)
	keycount2 = count_key(kv2)
	s = 'changetype: modify\n'
	i, j = 0, 0
	def _add(kv):
		return 'add: %s\n%s%s\n-\n'%(kv[0], kv[0], kv[1])
	def _del(kv):
		return 'delete: %s\n%s%s\n-\n'%(kv[0], kv[0], kv[1])
	def _replace(kv1, kv2):
		return 'replace: %s\n%s%s\n-\n'%(kv1[0], kv2[0], kv2[1])
		return kv2[0]+kv2[1]+'\n'
	while i<len(kv1) or j<len(kv2):
		if i==len(kv1):
			s += _add(kv2[j])
			j += 1
		elif j==len(kv2):
			s += _del(kv1[i])
			i += 1
		elif kv1[i] == kv2[j]:
			i, j = i+1, j+1
		elif kv1[i][0] < kv2[j][0]:
			s += _del(kv1[i])
			i += 1
		elif kv2[j][0] < kv1[i][0]:
			s += _add(kv2[j])
			j += 1
			# now kv1[i][0] = kv2[j][0]
		elif keycount1[kv1[i][0]]==1 and keycount2[kv2[j][0]]==1:
			s += _replace(kv1[i], kv2[j])
			i, j = i+1, j+1
		elif kv1[i] < kv2[j]:
			s += _del(kv1[i])
			i += 1
		elif kv2[j] < kv1[i]:
			s += _add(kv2[j])
			j += 1
	if s:
		return '\ndn%s\n%s\n'%(dn, s)
	else:
		return ''

def makeldif_delete(dn, kv):
	s = 'changetype: delete\n'
	return '\ndn%s\n%s\n'%(dn, s)

def makeldif_add(dn, kv):
	s = 'changetype: add\n'
	for x in kv:
		s += '%s%s\n'%x
	return '\ndn%s\n%s\n'%(dn, s)

def compare(ldif1, ldif2, file):
	seen = set()
	for dn, kv in ldif2.items():
		if dn in ldif1:
			kv1 = ldif1[dn]
			if kv1 != kv:
				s = makeldif_modify(dn, ldif1[dn], kv)
				file.write(s)
		else:
			s = makeldif_add(dn, kv)
			file.write(s)
		seen.add(dn)
	for dn, kv in ldif1.items():
		if not (dn in seen):
			s = makeldif_delete(dn, kv)
			file.write(s)

if __name__=='__main__':
	import sys
	i=1; n=0
	while i < len(sys.argv):
		ai = sys.argv[i]
		i += 1
		if ai=='-b':
			flag_binary = 1
		elif n==0:
			f1 = ai
			n += 1
		elif n==1:
			f2 = ai
			n += 1
		else:
			sys.stderr.write('error: too many arguments: "%s"\n'%ai)
			sys.exit(1)
	ldif1 = read_ldif(open(f1))
	ldif2 = read_ldif(open(f2))
	compare(ldif1, ldif2, sys.stdout)

