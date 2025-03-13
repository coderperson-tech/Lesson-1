set1 = {1,2,3,4,5,6,7,8}
print(set1)
set1.add(9)
print(set1)

set2 = {"apple","banana","cherry"}
set3 = {"google","microsoft","apple"}
set4 = set2.union(set3)

print("union of sets", set4)

set4 = set2.intersection(set3)
print("intersection of sets", set4)

set4 = set2.difference(set3)
print("difference of sets", set4)


set4 = set2.symmetric_difference(set3)
print("symmetric difference", set4)