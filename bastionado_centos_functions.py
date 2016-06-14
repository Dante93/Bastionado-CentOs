import os

res = False
res2 = False
oki = "All is OK"
estado = {}

#######################################################################
def check_cramf_filesys():
	
	retvalue = "".join(os.popen("modprobe -n -v cramfs").readlines())
	retvalue2 = "".join(os.popen("lsmod | grep cramfs").readlines())

	if retvalue == "install /bin/true":
		res = True
	if retvalue2 == '':
		res2 = True

	if (res == False || res2 == False):
		estado["1.1.1.1"] = False
		#return estado
	else:
		estado["1.1.1.1"] = True
		#return estado

#########################################################################
//1.1.1.2
def check_freevcfs_disble():
	retvalue = "".join(os.popen("modprobe -n -v freevxfs").readlines())
	retvalue2 = "".join(os.popen("lsmod | grep freevxfs").readlines())
	
	if retvalue == "install /bin/true":
		res = True
	if retvalue2 == '':
		res2 = True

	if (res == False || res2 == False):
		estado["1.1.1.2"] = False
		#return estado
	else:
		estado["1.1.1.2"] = True
		#return estado
##########################################################################
//1.1.1.3
def check_jffs2_disable():
	retvalue = "".join(os.popen("modprobe -n -v jffs2").readlines())
	retvalue2 = "".join(os.popen("lsmod | grep jffs2").readlines())

	if retvalue == "install /bin/true":
		res = True
	if retvalue2 == '':
		res2 = True

	if (res == False || res2 == False):
		estado["1.1.1.3"] = False
		#return estado
	else:
		estado["1.1.1.3"] = True
		#return estado
##########################################################################
//1.1.1.4
def check_hfs_disable():

	retvalue = "".join(os.popen("modprobe -n -v hfs").readlines())
	retvalue2 = "".join(os.popen("lsmod | grep hfs").readlines())

	if retvalue == "install /bin/true":
		res = True
	if retvalue2 == '':
		res2 = True

	if (res == False || res2 == False):
		estado["1.1.1.4"] = False
		#return estado
	else:
		estado["1.1.1.4"] = True
		#return estado
##########################################################################
//1.1.1.5
def check_hfsplus_disable():
	retvalue = "".join(os.popen("modprobe -n -v hfsplus").readlines())
	retvalue2 = "".join(os.popen("lsmod | grep hfsplus").readlines())

	if retvalue == "install /bin/true":
		res = True
	if retvalue2 == '':
		res2 = True

	if (res == False || res2 == False):
		estado["1.1.1.5"] = False
		#return estado
	else:
		estado["1.1.1.5"] = True
		#return estado
###########################################################################
//1.1.1.6
def check_squashfs_disable():
	retvalue = "".join(os.popen("modprobe -n -v squashfs").readlines())
	retvalue2 = "".join(os.popen("lsmod | grep squashfs").readlines())

	if retvalue == "install /bin/true":
		res = True
	if retvalue2 == '':
		res2 = True

	if (res == False || res2 == False):
		estado["1.1.1.6"] = False
		#return estado
	else:
		estado["1.1.1.6"] = True
		#return estado
###########################################################################
//1.1.1.7
def check_udf_disable():
	retvalue = "".join(os.popen("modprobe -n -v udf").readlines())
	retvalue2 = "".join(os.popen("lsmod | grep udf").readlines())

	if retvalue == "install /bin/true":
		res = True
	if retvalue2 == '':
		res2 = True

	if (res == False || res2 == False):
		estado["1.1.1.7"] = False
		#return estado
	else:
		estado["1.1.1.7"] = True
		#return estado
###########################################################################
//1.1.1.7
def check_fat_disable():
	retvalue = "".join(os.popen("modprobe -n -v vfat").readlines())
	retvalue2 = "".join(os.popen("lsmod | grep vfat").readlines())

	if retvalue == "install /bin/true":
		res = True
	if retvalue2 == '':
		res2 = True

	if (res == False || res2 == False):
		estado["1.1.1.8"] = False
		#return estado
	else:
		estado["1.1.1.8"] = True
		#return estado


if __name__=='__main__':
	
	print cramfs_filesys()
	
