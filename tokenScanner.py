#!/usr/bin/python3

# Developer By Abdulrahman Kamel
# Github: github.com/Abdulrahman-Kamel

from colorama import Fore
from sys import stdin, exit , argv 
from yaml import load, FullLoader
from re import match as match_re

arg_1 = argv[1] if len(argv) > 1 else 'empty'

def readYaml(file):
	return load(open(file), Loader=FullLoader)

class main():
	def __init__(self):
		self.tokenScan()
	
	def tokenScan(self):
		complete = []
		for part,data in readYaml('regex.yaml').items():
			title 	= data['title']

			if 'exploit' in data:
				exploit = data['exploit']

			regex 	= data['regex']

			match  = match_re(regex, arg_1)
			
			if match:
				print(arg_1)
				print(Fore.GREEN+"what is: "+Fore.RESET,title)
				if 'exploit' in data:
					print(Fore.RED+"exploit: "+Fore.RESET,exploit)
				exit(1)

		print(Fore.YELLOW+"Sory unknown this token"+Fore.RESET)

if __name__ == '__main__':
	
	# check token arg
	if arg_1 == 'empty':
		print('Please enter token => python3 tool.py <token>'); exit(1)

	main()
