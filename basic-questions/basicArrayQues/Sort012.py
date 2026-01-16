arr = [2,0,1,0,2,1,1,0,0,2]
arr.sort()
print(arr)
#time complexity of this code is O(n log n)
#space complexity of this code is O(1) if we ignore the space taken by the sorting algorithm

#2. Optimal Approach using counting
def sort012(a):
    count0 = 0
    count1 = 0
    count2 = 0

    for i in arr:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        else:
            count2 += 1
    
    index = 0

    for i in range(count0):
        a[index] = 0
        index += 1
    for i in range(count1):
        a[index] = 1
        index += 1
    for i in range(count2):
        a[index] = 2
        index += 1
    return a

a = [2,0,1,0,2,1,1,0,0,2]
print(sort012(a))
#time complexity of this code is O(n) and space complexity is O(1)

#3. Optimal Approach using Dutch National Flag Algorithm
def sort012Dutch(a):
    low = 0
    mid = 0
    high = len(a) - 1

    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a
ar = [2,0,1,0,2,1,1,0,0,2]
print(sort012Dutch(ar))
#time complexity of this code is O(n) and space complexity is O(1)  
# explain dutch national flag algorithm:
# we maintain three pointers low, mid and high 
# all elements before low are 0s
# all elements between low and mid are 1s   
# all elements after high are 2s
# we traverse the array with mid pointer
# if we encounter 0, we swap it with the element at low pointer and increment both low and mid pointers
# if we encounter 1, we just increment the mid pointer
# if we encounter 2, we swap it with the element at high pointer and decrement the high pointer
# we continue this process until mid pointer crosses high pointer
