#!/usr/bin/python
some_number=input();
bit_number=bin(some_number);
if len(bit_number) > 32:
	print("number not 32 bits!");
else:
	bit_number=~some_number;
	#result_number=bin(bit_number);
	print(bit_number);
