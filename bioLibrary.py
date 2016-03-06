#!/usr/bin/python

def getHammingDistance(string1, string2):
	if len(string1) <= 0 | len(string2) <= 0:
		print("Error: Either or both of the strings are empty")
	else :
		if len(string1) == len(string2):
			string1 = list(string1)
			string2 = list(string2)
			diff = 0
			for i in range(len(string1)):
				if(string1[i] != string2[i]):
					diff += 1
			print(diff)
		else :
			print("Error: String lengths are not equal.")