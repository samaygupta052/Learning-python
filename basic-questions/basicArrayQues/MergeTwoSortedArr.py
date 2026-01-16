# we have to merge two sorted arrays in a sorted manner
#we wil go from the brute force approach to optimal approach

#1. Brute Force Approach
def MergeSortedArray(a,b):
    merged_arr = a + b
    merged_arr.sort()
    return merged_arr

a = [1,3,5,7]
b = [2,4,6,8]
print(MergeSortedArray(a,b))
#time complexity of this code is O((n+m) log(n+m)) where n and m are the sizes of the two arrays
#space complexity of this code is O(n+m) for the merged array   

#2. Optimal Approach using two pointers
def MergeSortedArrayOptimal(a,b):
    merged_array = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged_array.append(a[i])
            i += 1
        else:
            merged_array.append(b[j])
            j += 1

    merged_array.extend(a[i:])
    merged_array.extend(b[j:])
    return merged_array

a = [1,3,5,7]
b = [2,4,6,8]
print(MergeSortedArrayOptimal(a,b))
#time complexity of this code is O(n+m) where n and m are the sizes of the two arrays
#space complexity of this code is O(n+m) for the merged array

# can we further reduce the time complexity or space complexity?
# no, we cannot reduce the time complexity or space complexity further
# because we have to look at all the elements of both arrays to merge them
# and we need to store all the elements in the merged array
# hence the time complexity is O(n+m) and space complexity is O(n+m)
# but if we are allowed to modify one of the input arrays, we can reduce the space complexity to O(1)

a = [1,3,5,7, 0,0,0,0] # assuming b has 4 elements
b = [2,4,6,8]

def MergeSortedArrayInPlace(a,b):
    m = len(a) - len(b)  # number of elements in a
    n = len(b)          # number of elements in b
    i = m - 1           # last index of a's elements
    j = n - 1           # last index of b
    k = m + n - 1       # last index of merged array

    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -= 1
        k -= 1

    while j >= 0:
        a[k] = b[j]
        j -= 1
        k -= 1

    return a
print(MergeSortedArrayInPlace(a,b))
#time complexity of this code is O(n+m) where n and m are the sizes of the two arrays
#space complexity of this code is O(1) as we are not using any extra space