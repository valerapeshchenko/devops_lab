#!/usr/bin/python
n = input();
m = input();
listA=[];
listB=[];

print("put words of group A:");
for i in range(n):
	#global listA
	word=input();
	listA.append(word);

print("put words of group B:");
for y in range(m):
	#global listB
        word = input();
        listB.append(str(word));

print("listA:");
print(listA);

print("listB:");
print(listB);

#for i in range(len(new_list)):
#	print(get_key(new_list[i]));
#listA=['a','a','c','c','b','d','e','b','b','e','a','a','a','e','b','e','d','d'];
#listB=['a','e','c','d','b'];
c={}
for g in range(len(listB)):
        for i in range(len(listA)):
                #global listA 
                #global listB
                #global c
                if listA[i] == listB[g]:                   
                        c[i]=str(listA[i]);

for i in c.items():
    print i
keys=[];
keys.append(c.keys());
print(keys[0]);
new_list=c.values();

jump=0;
print(new_list);
i=0;
cycle=len(new_list)-1;
old_string=c.values();
countB=0;
while i < cycle:
	#if i >= cycle:
	#	break;
	#global c
	stop=0
	jump=0;
	outPutString=str(keys[0][i]);
	for g in range(i + 1,len(new_list)):
		#global stop
		#global jump
		if new_list[i] != new_list[g]:
			stop=1
		if stop == 0:
			jump += 1;
		if new_list[i] == new_list[g]:	
			outPutString += " ";		
			outPutString += str(keys[0][g]);
			outPutString += " ";	
	i += jump;
	i += 1;
	if countB < len(listB):
		countB += 1;	
		print(outPutString);











