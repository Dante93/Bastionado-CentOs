import os

def cramfs_filesys():
	retvalue = os.popen("modprobe -n -v cramfs").readlines()
	retvalue2 = os.popen("lsmod | grep cramfs").readlines()
	return (retvalue,retvalue2)

if __name__=='__main__':
	
	print cramfs_filesys()
	print 'hola'