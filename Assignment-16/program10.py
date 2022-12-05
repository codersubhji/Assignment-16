"""10. Write a python program to change the first item (22) of a list within the following tuple
to 222.
tuple1 = (11, [22, 33], 44, 55)"""
tuple1 = (11, [22, 33], 44, 55)
l1=list(tuple1)
l1[1][0]=222
t2=tuple(l1)
print(t2)
