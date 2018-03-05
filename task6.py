import re;
#string='16*454=7264';
print("Please, enter statement with qutes:");
string=input();
if len(string) > 100:
	print("More than 100 chars!");
else:
	result = re.search(r'([0-9]{1,4}|[1-2]\d{4}|30000)[-\*\+\/]([0-9]{1,4}|[1-2]\d{4}|30000)=[0-9]{1,6}', string);
	result_number=0;

	if result:
		#global string
		#global result_number
		#print('Yes!');
		string_number=re.findall(r'[0-9]{1,4}', string);
		list_operation=re.findall(r'[-\*\+\/]', string);
		#print string_number
		number1=string_number[0];
		number2=string_number[1];
		number3=string_number[2];
		operation=list_operation[0];
		#print(operation);
		#print(number1);
		#print(number2);
		#print(number3);
		if operation == '*':
			result_number = int(number1) * int(number2);
		if operation == '+':
			result_number = int(number1) + int(number2);
		if operation == '-':
			result_number = int(number1) - int(number2);
		if operation == '/':
          		result_number = int(number1) / int(number2);
		#print(result_number);
		if int(number3) != result_number:
			print("NO");
		else:
			print("YES!");
	else:
	    print('ERROR');
