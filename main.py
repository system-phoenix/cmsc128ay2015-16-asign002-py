#!/usr/bin/python

import bioLibrary

#Test cases for getHammingDistance
print("getHammingDistance(AACCTT, GGCCTT): ", bioLibrary.getHammingDistance("AACCTT", "GGCCTT"))						#2
print("getHammingDistance(TCGGA, AAAAT): ", bioLibrary.getHammingDistance("TCGGA", "AAAAT"))							#5
print("getHammingDistance(A, AG): ", bioLibrary.getHammingDistance("A", "AG"))											#Error: Strins are not equal

#Test cases for countSubstrPattern
print("countSubstrPattern(AATATATAGG, GG): ", bioLibrary.countSubstrPattern("AATATATAGG", "GG"))						#1
print("countSubstrPattern(AATATATAGG, ATA): ", bioLibrary.countSubstrPattern("AATATATAGG", "ATA"))						#3
print("countSubstrPattern(AATATATAGG, ACTGACTGACTG): ", bioLibrary.countSubstrPattern("AATATATAGG", "ACTGACTGACTG")) 	#0

#Test cases for isValidString
print("isValidString(AAGGCTATGC, ACGT): ", bioLibrary.isValidString("AAGGCTATGC", "ACGT"))								#true
print("isValidString(AAGGCTATGa, ACGT): ", bioLibrary.isValidString("AAGGCTATGa", "ACGT"))								#false
print("isValidString(ACGT, ACGT): ", bioLibrary.isValidString("ACGT", "ACGT"))											#true
print("isValidString(ACGT101_, ACGT): ", bioLibrary.isValidString("ACGT101_", "ACGT"))									#false
print("isValidString(091212345, 0123456789): ", bioLibrary.isValidString("091212345", "0123456789"))					#true

#Test cases for getSkew
print("getSkew(GGCCAC, 1):", bioLibrary.getSkew("GGCCAC", 1))															#1
print("getSkew(GGCCAC, 2):", bioLibrary.getSkew("GGCCAC", 2))															#2
print("getSkew(GGCCAC, 3):", bioLibrary.getSkew("GGCCAC", 3))															#1
print("getSkew(GGCCAC, 4):", bioLibrary.getSkew("GGCCAC", 4))															#0
print("getSkew(GGCCAC, 5):", bioLibrary.getSkew("GGCCAC", 5))															#0

#Test cases for getMaxSkewN
print("getMaxSkewN(GGCCAC, 1): ", bioLibrary.getMaxSkewN("GGCCAC", 1))													#1
print("getMaxSkewN(GGCCAC, 2): ", bioLibrary.getMaxSkewN("GGCCAC", 2))													#2
print("getMaxSkewN(GGCCAC, 3): ", bioLibrary.getMaxSkewN("GGCCAC", 3))													#2
print("getMaxSkewN(GGCCAC, 4): ", bioLibrary.getMaxSkewN("GGCCAC", 4))													#2
print("getMaxSkewN(GGCCAC, 5): ", bioLibrary.getMaxSkewN("GGCCAC", 5))													#2