arr = [1,2,3,4,5,6,7,8,9]
arr.reverse()
print("Reversed array is:", arr)
# its time complexity is O(n) why?
# Because we need to iterate through half of the array to swap the elements.

# is there any other method to reverse an array?
# Yes, we can use slicing to reverse an array in Python.
arr2 = [1,2,3,4,5,6,7,8,9]
reversed_arr = arr2[::-1]
print("Reversed array using slicing is:", reversed_arr)
# its time complexity is also O(n) because slicing creates a new array and iterates through the original array.
# its space complexity is O(n) because it creates a new array to store the reversed elements.
# Both methods effectively reverse the array, but the first method modifies the original array in place.

# Another method to reverse an array is to use a loop to swap elements from the start and end moving towards the center.
def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
arr3 = [1,2,3,4,5,6,7,8,9]
reversed_arr3 = reverse_array(arr3)
print("Reversed array using custom function is:", reversed_arr3)
# its time complexity is O(n) because we need to iterate through half of the array to swap the elements.
# its space complexity is O(1) because it reverses the array in place without using any extra space.
# All three methods effectively reverse the array, but they differ in terms of space complexity and whether they modify the original array or create a new one.

#can we reduce the time complexity further?
# No, we cannot reduce the time complexity further than O(n) for reversing an array because we need to access each element at least once to reverse the order.
# Thus, O(n) is the optimal time complexity for this operation.