# there are three methods to create an array in python
# 1. using list
# 2. using array module
# 3. using numpy module
# in numpy we don't neet to specify the typecode
#val = array([1,2,3,4]) we can also write char,float with in the array


import array
# from array import *
# import array as arr

# it acts like a dynamic array 
val = array.array('i', [10, 20, 30, 40, 50])
for i in range(0,5):   # or range (0,len(val))
    print(val[i], end=" " )
print('\n')

# enhanced for loop
for x in val:
    print(x, end=" ")

print('\n')

# to print the typecode of array
print(val.typecode)

#to print the reverse of array
val.reverse()
for x in val:
    print(x, end=" ")
print('\n')

#to insert new element
#no element is replaced, the elements are shifted to right
val.insert(2, 25)
for x in val:
    print(x, end=" ")
print('\n')

#to append new element at the end
val.append(60)
for x in val:   
    print(x, end=" ")
print('\n')

#to remove an element
val.remove(30)
for x in val:       
    print(x, end=" ")
print('\n')

#to copy one array to another
newArray = array.array(val.typecode, (a for a in val))
for x in newArray:
    print(x, end=" ")
print('\n')

#deleting an array using pop
#val.pop(3)   #removes element at index 3
# if u write without the index, it will pop the last element
# use remove if u know the element snd pop when u know the index

# sciling of array
#abc = val[1:4]    from index 1 to index 3
# to print in reverse order 
#abc = val[::-1]

# to find index of an element
#index = val.index(25)