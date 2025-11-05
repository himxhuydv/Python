#  append function 
# used to add in the lasrt place without removing any elemt 

l1=[1,2,3,4,5,6,7,8,9,82,22,44,223,66,64]

print(l1)
l1.append("10")

print(l1)

# reverse function
# used for the reverse print of the lsit element 
l1.reverse()
print(l1)

# sort function 
#  used for the sorting in a list so sort aslo do not retrun anything so if u write in result(l1.)
l1.sort()
print(l1)


#  pop function 
#  used for the poping of the list removal of the any element and they return it mean it can be print like this()
result=l1.pop(2)
print(result)


# insert opeation 
# insertion on any point eith index and respecteed value is consider first right the index u  want to change then write the value u want to enter 
l1.insert(2,22)
print(l1)

# remove function 
# this is used to remove any element ffrom the list 
l1.remove(223)
print(l1)
# now the 223  is removed successfully from the list 