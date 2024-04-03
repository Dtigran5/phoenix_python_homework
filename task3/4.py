set1 = {1,2,3,4,5,6}
set2 = {7,8,9,1,2,3}

set12 = set1.difference(set2)
set21 = set2.difference(set1)

print(f"this is set that are in set1 and not in set2", set12)
print(f"this is set that are in set2 and not in set1", set21)
