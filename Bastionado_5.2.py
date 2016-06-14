#!/usr/bin/python

import subprocess
import re



check_list = dict()

test_file="/etc/ssh/sshd_config" #"test_ssh_config"

def check_5_2_1(check_list):
	result=None

	command = "stat"
	path_to_check="/etc/ssh/ssh_config"
	stdout = subprocess.check_output([command, path_to_check])

	check_string ="(0600/-rw-------)  Uid: (    0/    root)   Gid: (    0/    root)"
	searching_result=stdout.find(check_string)
	if (searching_result == -1):
		result = True
	else:
		result = False
	#print('Salida:', stdout)
	check_list.update({check_5_2_1.func_name:result})
	return;

def check_5_2_2_v2(check_list):
	
	check1 = check_regex('^[^#].*Protocol.*$',"Protocol 1",test_file)
	check2 = check_regex('^Protocol.*$',"Protocol 1",test_file)

	if (check1):
		check_list.update({check_5_2_2_v2.func_name:True})
	elif (check2):
		check_list.update({check_5_2_2_v2.func_name:True})
	else:
		check_list.update({check_5_2_2_v2.func_name:False})		
	return;

def check_5_2_3_v2(check_list):
	
	check1 = check_regex('^[^#].*LogLevel.*$',"INFO",test_file)
	check2 = check_regex('^LogLevel.*$',"INFO",test_file)
	

	if (check1):
		check_list.update({check_5_2_3_v2.func_name:False})
	elif (check2):
		check_list.update({check_5_2_3_v2.func_name:False})
	else:
		check_list.update({check_5_2_3_v2.func_name:True})
	return;

def check_5_2_4(check_list):
	
	check1 = check_regex('^[^#].*X11Forwarding.*$',"yes",test_file)
	check2 = check_regex('^X11Forwarding.*$',"yes",test_file) 

	if (check1):
		check_list.update({check_5_2_4.func_name:True})
	elif (check2):
		check_list.update({check_5_2_4.func_name:True})
	else:
		check_list.update({check_5_2_4.func_name:False})
	return;

def check_5_2_5(check_list):

	file = open(test_file,"r")
	regex = re.compile('^[^#].*MaxAuthTries.*$')
	regex2 = re.compile('^MaxAuthTries.*$')
	for line in file:
		found_pattern = regex.findall(line)
		for pattern_content in found_pattern:
			match = re.search('(?P<Flag>.*) (?P<Value>.*)',pattern_content)
			if (int(match.group('Value')) < 5):	
				check_list.update({check_5_2_5.func_name:False})
			else:
				check_list.update({check_5_2_5.func_name:True})
		found_pattern = regex2.findall(line)
		for pattern_content in found_pattern:
			match = re.search('(?P<Flag>.*) (?P<Value>.*)',pattern_content)
			if (int(match.group('Value')) < 5):	
				check_list.update({check_5_2_5.func_name:False})
			else:
				check_list.update({check_5_2_5.func_name:True})

	file.close()
	return;			

def check_5_2_6(check_list):
	
	check1 = check_regex('^[^#].*IgnoreRhosts.*$',"no",test_file)
	check2 = check_regex('^IgnoreRhosts.*$',"no",test_file) 

	if (check1):
		check_list.update({check_5_2_6.func_name:True})
	elif (check2):
		check_list.update({check_5_2_6.func_name:True})
	else:
		check_list.update({check_5_2_6.func_name:False})
	return;

def check_5_2_7(check_list):
	
	check1 = check_regex('^[^#].*HostbasedAuthentication.*$',"yes",test_file)
	check2 = check_regex('^HostbasedAuthentication.*$',"yes",test_file) 

	if (check1):
		check_list.update({check_5_2_7.func_name:True})
	elif (check2):
		check_list.update({check_5_2_7.func_name:True})
	else:
		check_list.update({check_5_2_7.func_name:False})
	return;

def check_5_2_8(check_list):
	
	check1 = check_regex('^[^#].*PermitRootLogin.*$',"yes",test_file)
	check2 = check_regex('^PermitRootLogin.*$',"yes",test_file) 

	if (check1):
		check_list.update({check_5_2_8.func_name:True})
	elif (check2):
		check_list.update({check_5_2_8.func_name:True})
	else:
		check_list.update({check_5_2_8.func_name:False})
	return;

def check_5_2_9(check_list):
	
	check1 = check_regex('^[^#].*PermitEmptyPasswords.*$',"yes",test_file)
	check2 = check_regex('^PermitEmptyPasswords.*$',"yes",test_file) 

	if (check1):
		check_list.update({check_5_2_8.func_name:True})
	elif (check2):
		check_list.update({check_5_2_8.func_name:True})
	else:
		check_list.update({check_5_2_8.func_name:False})
	return;

def check_5_2_10(check_list):
	
	check1 = check_regex('^[^#].*PermitUserEnvironment.*$',"yes",test_file)
	check2 = check_regex('^PermitUserEnvironment.*$',"yes",test_file) 

	if (check1):
		check_list.update({check_5_2_8.func_name:True})
	elif (check2):
		check_list.update({check_5_2_8.func_name:True})
	else:
		check_list.update({check_5_2_8.func_name:False})
	return;

def check_5_2_13(check_list):

	first_check = False
	second_check = False
	file = open(test_file,"r")
	regex = re.compile('^[^#].*ClientAliveInterval.*$')
	regex2 = re.compile('^ClientAliveInterval.*$')
	regex3 = re.compile('^[^#].*ClientAliveCountMax.*$')
	regex4 = re.compile('^ClientAliveCountMax.*$')
	
	for line in file:
		found_pattern = regex.findall(line)
		for pattern_content in found_pattern:
			match = re.search('(?P<Flag>.*) (?P<Value>.*)',pattern_content)
			if (int(match.group('Value')) > 300):	
				first_check = True
			
		found_pattern = regex2.findall(line)
		for pattern_content in found_pattern:
			match = re.search('(?P<Flag>.*) (?P<Value>.*)',pattern_content)
			if (int(match.group('Value')) > 300):	
				first_check = True 

		found_pattern = regex3.findall(line)
		for pattern_content in found_pattern:
			match = re.search('(?P<Flag>.*) (?P<Value>.*)',pattern_content)
			if (int(match.group('Value')) > 3):	
				first_check = True 

		found_pattern = regex2.findall(line)
		for pattern_content in found_pattern:
			match = re.search('(?P<Flag>.*) (?P<Value>.*)',pattern_content)
			if (int(match.group('Value')) > 3):	
				first_check = True 

	if (first_check or second_check):
		check_list.update({check_5_2_13.func_name:True})


	file.close()
	return;		

def check_5_2_14(check_list):

	file = open(test_file,"r")
	regex = re.compile('^[^#].*LoginGraceTime.*$')
	regex2 = re.compile('^LoginGraceTime.*$')
	for line in file:
		found_pattern = regex.findall(line)
		for pattern_content in found_pattern:
			match = re.search('(?P<Flag>.*) (?P<Value>.*)',pattern_content)
			if (int(match.group('Value')) < 5):	
				check_list.update({check_5_2_5.func_name:False})
			else:
				check_list.update({check_5_2_5.func_name:True})
		found_pattern = regex2.findall(line)
		for pattern_content in found_pattern:
			match = re.search('(?P<Flag>.*) (?P<Value>.*)',pattern_content)
			if (int(match.group('Value')) < 5):	
				check_list.update({check_5_2_5.func_name:False})
			else:
				check_list.update({check_5_2_5.func_name:True})

	file.close()
	return;			

#TODO
def get_value(regular_expresion, file_to_check):
	file = open(file_to_check, 'r')
	content = file.read()
	match = re.search('(?P<Flag>.*) (?P<Value>.*)',content)
	print (match.group('Flag'))
	return;
    
def check_regex(regular_expression, looked_output, file_to_check):
	file = open(file_to_check,"r")
	regex = re.compile(regular_expression)
	for line in file:
		found_pattern = regex.findall(line)
		for pattern_content in found_pattern:
			#print(pattern_content)
			if(pattern_content.find(looked_output)>-1):

				file.close()
				return True

	file.close()				
	return False


#check_5_2_1(check_list)
check_5_2_2_v2(check_list)
check_5_2_3_v2(check_list)
check_5_2_4(check_list)
check_5_2_5(check_list)
check_5_2_6(check_list)
check_5_2_7(check_list)
check_5_2_8(check_list)
#get_value("r",test_file)
print check_list





