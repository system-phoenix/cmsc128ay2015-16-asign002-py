#!/usr/bin/python

def getHammingDistance(string1, string2):
	if len(string1) <= 0 | len(string2) <= 0:
		return("Error: Either or both of the strings are empty")
	else :
		if len(string1) == len(string2):
			string1 = list(string1)
			string2 = list(string2)
			diff = 0
			for i in range(len(string1)):
				if(string1[i] != string2[i]):
					diff += 1
			return(diff)
		else :
			return("Error: String lengths are not equal.")

def countSubstrPattern(original, pattern):
	original = list(original)
	pattern = list(patter)

	if(len(original) < len(pattern)) : return 0