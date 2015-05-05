#filter.py
#coding:utf-8

def is_odd(n):
	return n % 2 == 1

ls = [1,2,3,4,5,6,7,8,9]
print filter(is_odd, ls)
