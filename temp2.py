
FAR = 0
FRR = 149
total = 1007

dFAR = FAR * 100 / total
dFRR = FRR * 100 / total

dAccuracy = 100.0 - (dFAR + dFRR)

print(dFAR)
print(dFRR)
print(dAccuracy)
