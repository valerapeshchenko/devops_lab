#!/usr/bin/python
a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
c=a.copy();
c.clear();
for i in range(len(a)):
	for g in range(len(b)):
		#global a 
		#global b
		#global c
		if a[i] == b[g]:
			if a[i] in c:
				continue;
			c.append(a[i]);
print(c);
