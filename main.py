#!/usr/bin/python

import bioLibrary

#Test cases for getHammingDistance
print("getHammingDistance(AACCTT, GGCCTT): ", bioLibrary.getHammingDistance("AACCTT", "GGCCTT"))
print("getHammingDistance(TCGGA, AAAAT): ", bioLibrary.getHammingDistance("TCGGA", "AAAAT"))
print("getHammingDistance(A, AG): ", bioLibrary.getHammingDistance("A", "AG"))

#Test cases for countSubstrPattern
print("countSubstrPattern(AATATATAGG, GG): ", bioLibrary.countSubstrPattern("AATATATAGG", "GG"))
print("countSubstrPattern(AATATATAGG, ATA): ", bioLibrary.countSubstrPattern("AATATATAGG", "ATA"))
print("countSubstrPattern(AATATATAGG, ACTGACTGACTG): ", bioLibrary.countSubstrPattern("AATATATAGG", "ACTGACTGACTG"))

#Test cases for isValidString
print("isValidString(AAGGCTATGC, ACGT): ", bioLibrary.isValidString("AAGGCTATGC", "ACGT"))
print("isValidString(AAGGCTATGa, ACGT): ", bioLibrary.isValidString("AAGGCTATGa", "ACGT"))
print("isValidString(ACGT, ACGT): ", bioLibrary.isValidString("ACGT", "ACGT"))
print("isValidString(ACGT101_, ACGT): ", bioLibrary.isValidString("ACGT101_", "ACGT"))
print("isValidString(091212345, 0123456789): ", bioLibrary.isValidString("091212345", "0123456789"))