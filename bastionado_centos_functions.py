import os

res = False
res2 = False
oki = "All is OK"

//1.1.1.1
def cramfs_filesys():
	
	retvalue = "".join(os.popen("modprobe -n -v cramfs").readlines())
	retvalue2 = "".join(os.popen("lsmod | grep cramfs").readlines())

	if retvalue == "install /bin/true":
		res = True
	if retvalue2 == '':
		res2 = True

	if (res == False || res2 == False):

		if os.path.exists('/etc/modprobe.d/CIS.conf'):
			aux = open('/etc/modprobe.d/CIS.conf','a')
			aux.write("install cramfs /bin/true \n")
		

		else:
			aux = open('/etc/modprobe.d/CIS.conf','w')
			aux.write("install cramfs /bin/true \n")
			aux.close()

	else:
		return oki

//1.1.1.2
def freevcfs_disble():
	retvalue = "".join(os.popen("modprobe -n -v freevxfs").readlines())
	retvalue2 = "".join(os.popen("lsmod | grep freevxfs").readlines())
	
	if retvalue == "install /bin/true":
		res = True
	if retvalue2 == '':
		res2 = True

	if (res == False || res2 == False):
		if os.path.exists('/etc/modprobe.d/CIS.conf'):
			aux = open('/etc/modprobe.d/CIS.conf \n','a')
			aux.write("install freevxfs /bin/true")

		else:
			aux = open('/etc/modprobe.d/CIS.conf','w')
			aux.write("install freevxfs /bin/true \n")
			aux.close()

	else:
		return oki

//1.1.1.3
def jffs2_disable():
	retvalue = "".join(os.popen("modprobe -n -v jffs2").readlines())
	retvalue2 = "".join(os.popen("lsmod | grep jffs2").readlines())

	if retvalue == "install /bin/true":
		res = True
	if retvalue2 == '':
		res2 = True

	if (res == False || res2 == False):
		if os.path.exists('/etc/modprobe.d/CIS.conf'):
			aux = open('/etc/modprobe.d/CIS.conf \n','a')
			aux.write("install jffs2 /bin/true")

		else:
			aux = open('/etc/modprobe.d/CIS.conf','w')
			aux.write("install jffs2 /bin/true \n")
			aux.close()

	else:
		return oki


if __name__=='__main__':
	
	print cramfs_filesys()
	