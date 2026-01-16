arr = [1,2,3,5,6]
sum1 = sum(arr)
n = 6
sum2 =0
for i in range(1,7):
    sum2 = sum2 + i
    missing_number = sum2 - sum1

print("The missing number is:", missing_number)

# the time complexity of this code is O(n)
# the space complexity of this code is O(1)

# we can also use the formula n(n+1)/2 to find the sum of first n natural numbers
# sum2 = n*(n+1)//2
# missing_number = sum2 - sum1
#the time complexity of this code is O(n)
#the space complexity of this code is O(1)

# we can also use the XOR method to find the missing number
xor_all = 0

for i in range(1, n + 1):
        xor_all ^= i    # XOR of all numbers from 1 to n
        

for num in arr:
        xor_all ^= num  # XOR of all numbers in the array
        
missing_num = xor_all
print("The missing number is:", missing_num)
# explanation of XOR method:
# XOR of a number with itself is 0
# XOR of a number with 0 is the number itself
#time complexity of this code is O(n)
#space complexity of this code is O(1)

#can we futher reduce the time complexity to O(log n) or O(1)?
#no, we cannot reduce the time complexity to O(log n) or O(1)

