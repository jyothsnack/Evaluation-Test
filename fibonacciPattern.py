str_input = raw_input('Enter string : ')
str_input = str_input.replace(' ','').replace('\t', '')
int_len = len(str_input)
num1 = 0
num2 = 1
lst_output = []
if int_len:
	lst_output.append(str_input[num1])

while num2 < int_len:
	lst_output.append(str_input[num2])
	num3 = num1 + num2
	num1 = num2
	num2 = num3
str_output = ('*_*').join(lst_output)
str_output = str_output.upper()
print str_output