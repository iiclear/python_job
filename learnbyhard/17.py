from sys import argv
from os.path import exists

script,fromfile,tofile = argv
in_file = open(fromfile)
indata = in_file.read()
out_file = open(tofile,'w')
out_file.write(indata)
out_file.close()
in_file.close()
