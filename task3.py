print("Please enter N:");
N=input();
Q="0"
result=""
true=0;
special=0;
while true == 0:
	#global Q
	check_Q=int(Q);
	check = check_Q / N;
	if check > 1000:
		print("-1");
		special=1;
		break;
	else:
		composition=1
		for i in range(len(Q)):
			#global composition
			#global N
			composition=composition*int(Q[i]);
		if N == composition:
	        	#global result
	        	result=Q;
	        	break;
		#print(composition);
		help_number=int(Q);
		help_number=help_number+1;
		Q=str(help_number);
		#print(Q);
if special != 1:
	super_number=int(result);
	print(super_number);
