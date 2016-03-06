#!/usr/bin/python

def getHammingDistance(string1, string2):
	if len(string1) <= 0 | len(string2) <= 0:							#case that the either of the strings are empty
		return("Error: Either or both of the strings are empty")
	else :
		if len(string1) == len(string2):								#next, check if the strings are of equal length
			string1 = list(string1)										#convert both strings to list or array of characters
			string2 = list(string2)
			diff = 0
			for i in range(len(string1)):
				if(string1[i] != string2[i]):							#check if the characters at the same index of both strings are not equal
					diff += 1											#increment the difference variable if true
			return(diff)
		else :
			return("Error: String lengths are not equal.")

def countSubstrPattern(original, pattern):
	original = list(original)											#convert the original and pattern strings to array of characters
	pattern = list(pattern)
	same = 0															#initialize the pattern counter to 0

	if(len(original) < len(pattern)) : return same						#return right away if the length of pattern to be found is greater than the actual length of the string
	for i in range(len(original)):
		if(original[i] == pattern[0]):									#check if the current letter being checked is equal to the first letter of the pattern
			match = 0
			for j in range(len(pattern)):
				if(i + j >= len(original)):								#check if the index of original string will suffice
					return same
				if(original[i + j] == pattern[j]):						#check for the next characters after the first match of the pattern and current character
					match += 1
			if(match == len(pattern)):									#check if the counter exhausted all the letters in the pattern
				same += 1												#increment the pattern counter if it did
	return same

def isValidString(string, alphabet):
	string = list(string)												#convert strings
	alphabet = list(alphabet)

	for i in range(len(string)):
		match = "false"													#set checker to false
		for j in range(len(alphabet)):
			if(string[i] == alphabet[j]):								#find the cracter in the alphabet
				match = "true"											#if found, set checker to true, then break
				break
			else :
				continue
		if(match == "false"):											#check if the alphabet was exhausted
			return "false"
	return "true"

def getSkew(string, n):
	string = list(string)												#convert string to character array

	if(len(string) == 0):
		return "Error: String is empty"									#check if the string is empty

	newString = getFirstN(string, n)									#get the first n characters

	g = 0																#set counters to 0
	c = 0
	for i in range(len(newString)):
		if(newString[i] == 'G'):										#case that the character is G
			g += 1
		elif(newString[i] == 'C'):										#case that the character is C
			c += 1
		else :															#continue if the character did not match C or G
			continue
	return(g - c)														#return the difference of G and C

def getMaxSkewN(string, n):
	string = list(string)												#convert string to character array

	if(len(string) == 0):
		return "Error: String is empty"

	newString = getFirstN(string, n)

	g = 0
	for i in range(len(newString)):
		if(newString[i] == 'G'):										#count only the Gs
			g += 1
	return g

def getMinSkewN(string, n):
	string = list(string)												#convert string to character array

	if(len(string) == 0):
		return "Error: String is empty"

	newString = getFirstN(string, n)
	g = 0
	c = 0
	minG = 1

	for i in range(len(newString)):
		if(newString[i] == 'G'):										#count the Gs and the Cs
			g += 1
		elif(newString[i] == 'C'):
			c += 1
		else:
			continue

		if(minG > g - c):												#see if the minimum G value can be changed
			minG = g - c

	return minG


#- - - - - - - - - - - - - - - - - - - - -
#Function that gets the first n characters
#- - - - - - - - - - - - - - - - - - - - -
def getFirstN(l, n):
	newString = []
	for i in range(len(l)):					#given a list l and a number n
		if(i >= n):
			break
		else :
			newString.extend([l[i]])		#get all the characters from the list until n
	return newString