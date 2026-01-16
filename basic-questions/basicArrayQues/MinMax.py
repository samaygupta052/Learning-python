arr = [3,4,7,9,4,7,2,0,1,6]
arr.sort()
min_value = arr[0]
max_value = arr[-1]
print(f"Minimum value in the array is: {min_value}")
print(f"Maximum value in the array is: {max_value}")
# Time complexity of this approach is O(n log n) due to the sorting step.

# Is there a more efficient way to find min and max?
# Yes, we can find both min and max in a single pass through the array with O(n) time complexity.
def find_min_max(arr):
    if len(arr) == 0:
        return None
    min_value = arr[0]
    max_value = arr[0]
    for i in arr:
        if i < min_value:
            min_value = i
        elif i > max_value:
            max_value = i
    return min_value, max_value
min_val, max_val = find_min_max(arr)
print(f"Minimum value using single pass: {min_val}")
print(f"Maximum value using single pass: {max_val}")
# Time complexity of this approach is O(n) because we only traverse the array once.
# Space complexity is O(1) since we are using a constant amount of extra space.

# Can we reduce the time complexity further?
# No, we cannot reduce the time complexity further than O(n) for finding both min and max because we need to examine each element at least once to determine the minimum and maximum values.
# Thus, O(n) is the optimal time complexity for this operation.