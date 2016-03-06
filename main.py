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