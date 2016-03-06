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
	pattern = list(pattern)
	same = 0

	if(len(original) < len(pattern)) : return same
	for i in range(len(original)):
		if(original[i] == pattern[0]):
			match = 0
			for j in range(len(pattern)):
				if(i + j >= len(original)):
					return same
				if(original[i + j] == pattern[j]):
					match += 1
			if(match == len(pattern)):
				same += 1
	return same

def isValidString(string, alphabet):
	string = list(string)
	alphabet = list(alphabet)

	for i in range(len(string)):
		match = "false"
		for j in range(len(alphabet)):
			if(string[i] == alphabet[j]):
				match = "true"
			else :
				continue
		if(match == "false"):
			return "false"
	return "true"

def getSkew(string, n):
	string = list(string)
	newString = []

	for i in range(len(string)):
		if(i >= n):
			break
		else :
			newString.extend([string[i]])

	g = 0
	c = 0
	for i in range(len(newString)):
		if(newString[i] == 'G'):
			g += 1
		elif(newString[i] == 'C'):
			c += 1
		else :
			continue
	return(g - c)