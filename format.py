# coding: utf-8

import os
import glob
import io
import getopt
import sys

root_path = None

def print_usage():
	print('Usage: -r[root path]')
	
opts,args = getopt.getopt(sys.argv[1:], 'r:', ['help'])
for name, value in opts:
	if name in ['--help']:
		print_usage()
		exit(1)
	elif name in ['-r']:
		root_path = value
		
if root_path is None:
	print_usage()
	exit(1)
	
print("Root path: {}".format(root_path))

for subdir, dirs, files in os.walk(root_path):
	for filename in files:
		filepath = subdir + os.sep + filename
		if filepath.endswith(".h") or filepath.endswith(".cpp") or filepath.endswith(".inl"):
			print("Formating " + filepath)
			os.system("clang-format -i {}".format(filepath))

print("Finish formating")