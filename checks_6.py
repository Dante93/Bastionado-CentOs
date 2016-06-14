import os

check_list = dict()

def check_6_1_1(check_list):
	result=None

	retvalue = "".join(os.popen("rpm -Va --nomtime --nosize --nomd5 --nolinkto").readlines())

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_1_1.func_name:result})


def check_6_1_2(check_list):

	retvalue = "".join(os.popen("stat /etc/passwd").readlines())

	res = retvalue.find("(0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)")
	
	if retvalue != -1:
		result=False
	else:
		result=True

	check_list.update({check_6_1_2.func_name:result})

def check_6_1_3(check_list):

	retvalue = "".join(os.popen("stat /etc/shadow").readlines())

	res = retvalue.find("(0000/----------)  Uid: (    0/    root)   Gid: (    0/    root)")
	
	if retvalue != -1:
		result=False
	else:
		result=True

	check_list.update({check_6_1_3.func_name:result})

def check_6_1_4(check_list):

	retvalue = "".join(os.popen("stat /etc/group").readlines())

	res = retvalue.find("(0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)")
	
	if retvalue != -1:
		result=False
	else:
		result=True

	check_list.update({check_6_1_4.func_name:result})

def check_6_1_5(check_list):

	retvalue = "".join(os.popen("stat /etc/gshadow").readlines())

	res = retvalue.find("(0600/-rw-------)  Uid: (    0/    root)   Gid: (    0/    root)")
	
	if retvalue != -1:
		result=False										#ERRATA EN EL PDF????????????
	else:
		result=True

	check_list.update({check_6_1_5.func_name:result})

def check_6_1_6(check_list):

	retvalue = "".join(os.popen("stat /etc/passwd-").readlines())

	res = retvalue.find("(0600/-rw-------)  Uid: (    0/    root)   Gid: (    0/    root)")
	
	if retvalue != -1:
		result=False
	else:
		result=True

	check_list.update({check_6_1_6.func_name:result})

def check_6_1_7(check_list):

	retvalue = "".join(os.popen("stat /etc/shadow-").readlines())

	res = retvalue.find("(0600/-rw-------)  Uid: (    0/    root)   Gid: (    0/    root)")
	
	if retvalue != -1:
		result=False
	else:
		result=True

	check_list.update({check_6_1_7.func_name:result})

def check_6_1_8(check_list):

	retvalue = "".join(os.popen("stat /etc/group-").readlines())

	res = retvalue.find("(0600/-rw-------)  Uid: (    0/    root)   Gid: (    0/    root)")
	
	if retvalue != -1:
		result=False
	else:
		result=True

	check_list.update({check_6_1_8.func_name:result})

def check_6_1_9(check_list):

	retvalue = "".join(os.popen("stat /etc/gshadow-").readlines())

	res = retvalue.find("(0600/-rw-------)  Uid: (    0/    root)   Gid: (    0/    root)")
	
	if retvalue != -1:
		result=False
	else:
		result=True

	check_list.update({check_6_1_9.func_name:result})

def check_6_1_10(check_list):

	retvalue = "".join(os.popen("df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type f").readlines())
	
	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_1_10.func_name:result})

def check_6_1_11(check_list):

	retvalue = "".join(os.popen("df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -nouser").readlines())
	
	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_1_11.func_name:result})

def check_6_1_12(check_list):

	retvalue = "".join(os.popen("df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -nogroup").readlines())
	
	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_1_12.func_name:result})

def check_6_1_13(check_list):

	retvalue = "".join(os.popen("df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type f -perm -4000").readlines())
	
	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_1_13.func_name:result})

def check_6_1_14(check_list):

	retvalue = "".join(os.popen("df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type f -perm -2000").readlines())
	
	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_1_14.func_name:result})

	res = "".join(os.popen("cat /etc/shadow | awk -F: '($2 == \"\" ) { print $1 \" does not have a password \"}'").readlines())

# CHECKs 6.2.x

def check_6_2_1(check_list):

	retvalue = "".join(os.popen("cat /etc/shadow | awk -F: '($2 == \"\" ) { print $1 \" does not have a password \"}'").readlines())

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_1.func_name:result})

def check_6_2_2(check_list):

	retvalue = "".join(os.popen("grep '^+:' /etc/passwd").readlines())

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_2.func_name:result})

def check_6_2_3(check_list):

	retvalue = "".join(os.popen("grep '^+:' /etc/shadow").readlines())

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_3.func_name:result})

def check_6_2_4(check_list):

	retvalue = "".join(os.popen("grep '^+:' /etc/group").readlines())

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_4.func_name:result})

def check_6_2_5(check_list):

	retvalue = "".join(os.popen("cat /etc/passwd | awk -F: '($3 == 0) { print $1 }'").readlines())

	if retvalue == "root\n":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_5.func_name:result})

def check_6_2_6(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_6.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_6.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_6.func_name:result})

def check_6_2_7(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_7.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_7.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_7.func_name:result})

def check_6_2_8(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_8.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_8.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_8.func_name:result})


def check_6_2_9(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_9.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_9.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_9.func_name:result})

def check_6_2_10(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_10.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_9.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_10.func_name:result})

def check_6_2_11(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_11.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_9.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_11.func_name:result})

def check_6_2_12(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_12.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_9.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_12.func_name:result})

def check_6_2_13(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_13.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_9.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_13.func_name:result})

def check_6_2_14(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_14.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_9.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_14.func_name:result})

def check_6_2_15(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_15.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_9.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_15.func_name:result})

def check_6_2_16(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_16.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_9.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_16.func_name:result})

def check_6_2_17(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_17.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_9.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_17.func_name:result})

def check_6_2_18(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_18.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_9.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_18.func_name:result})

def check_6_2_19(check_list):

	retvalue = "".join(os.popen("sh checks_6_2/check_6_2_19.sh").readlines())  				#  NECESITA EL SCRIPT check_6_2_9.sh EN LA MISMA CARPETA 

	if retvalue == "":
		result=False
	else:
		result=True
		
	check_list.update({check_6_2_19.func_name:result})