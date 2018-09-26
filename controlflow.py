#!/usr/bin/env python3


a = 10
b = 20

if (a == b): 
	print('A is equal to b')
elif ( a > b):
	print('A is greater than b')
else:
	print('A is less than b')


while (a < b):
	a = a + 1
else:
	print('Value of a is ',a)

L = [1,2,3,4,5,6,7,8,9]

for i in L:
	print(i) 

try:
	a /= 0
	print('All is good')

except:
	print('Got the division error')

finally:
	print('value of a',a)


print('Program continues to work')

with (open ('filename')) as f:
	f.read()

 
