# name.py
# coding:utf-8
#import pdb

#def regular(inStr):
#	pdb.set_trace()
#	strTemp1 = inStr.upper()
#	strTemp2 = "%s" % (inStr[:2].upper() + inStr[2:])
#	strTemp = "%s" % (inStr[:1].upper() + inStr[1:])
#	pdb.set_trace()
#	return "%s" % (inStr[:2].upper() + inStr[2:])

def regular(v):
#    print len(v)
    #	return v.title()
    str = ''
    for i in range(0, len(v)):
        if 0 == i:
            str += v[i].upper()
        else:
            str += v[i].lower()
    return str

#	num = len(v)
#	print num
#	while x < num:
#		if 1 == x:
#			v[x].upper()
#		else:
#			v[x].lower()
#
#	return v

ls = ['AdM','xuebIng','BAldwin']
s = ''
s = raw_input()
#for x in xrange(0, 3):
#    s = raw_input()
    #	print s
#    ls.append(s)
print ls
print map(regular, ls)
#print ls