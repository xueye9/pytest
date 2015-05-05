#reduce
#coding:utf-8

ls = range(1,11)
def f(x, y):
	return x + y

print reduce(f, ls)