import os

def split(ifName, ofName, delim):
	if(not os.path.isfile(ifName)):
		return False
	ofile = open(ofName, 'w+')
	with open(ifName) as file:
		contents = file.read()
		for entry in contents.split(delim):
			ofile.write(entry)
			ofile.write('\n')
	ofile.close()
	file.close()
	return True
