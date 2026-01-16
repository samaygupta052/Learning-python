
Access Operations
| Operation    | Example      | Time     | Space | Notes                |
| ------------ | ------------ | -------- | ----- | -------------------- |
| Index access |  arr[i]      |   O(1)   | O(1)  | Direct memory access |
| Update value |  arr[i] = x  |   O(1)   | O(1)  | Overwrites element   |
| Length       |  len(arr)    |   O(1)   | O(1)  | Stored internally    |



Insertion Operations
| Method             | Example             | Time               | Space    | Why                |
| ------------------ | ------------------- | ------------------ | -------- | ------------------ |
|  append(x)         |  arr.append(10)     |   O(1) amortized   | O(1)     | Occasional resize  |
|  insert(i, x)      |  arr.insert(0, 5)   |   O(n)             | O(1)     | Shift elements     |
|  extend(iterable)  |  arr.extend([1,2])  |   O(k)             | O(1)     | k = added elements |
| Concatenation      |  arr + arr2         |   O(n + m)         | O(n + m) | New list created   |



Deletion Operations
| Method         | Example         | Time     | Space | Why             |
| -------------- | --------------- | -------- | ----- | --------------- |
|  pop()  (last) |  arr.pop()      |   O(1)   | O(1)  | No shifting     |
|  pop(i)        |  arr.pop(0)     |   O(n)   | O(1)  | Shift elements  |
|  remove(x)     |  arr.remove(5)  |   O(n)   | O(1)  | Search + shift  |
|  clear()       |  arr.clear()    |   O(n)   | O(1)  | Dereference all |



Search & Membership
| Method     | Example        | Time     | Space | Notes            |
| ---------- | -------------- | -------- | ----- | ---------------- |
| Membership |  x in arr      |   O(n)   | O(1)  | Linear scan      |
|  index(x)  |  arr.index(5)  |   O(n)   | O(1)  | First occurrence |
|  count(x)  |  arr.count(5)  |   O(n)   | O(1)  | Full scan        |



Ordering & Rearrangement
| Method        | Example         | Time           | Space        | Notes        |
| ------------- | --------------- | -------------- | ------------ | ------------ |
|  sort()       |  arr.sort()     |   O(n log n)   |   O(log n)   | Timsort      |
|  sorted(arr)  |  sorted(arr)    |   O(n log n)   |   O(n)       | New list     |
|  reverse()    |  arr.reverse()  |   O(n)         | O(1)         | In-place     |
| Slicing       |  arr[::-1]      |   O(n)         |   O(n)       | Copy created |



Copying
| Method       | Example      | Time     | Space    |
| ------------ | ------------ | -------- | -------- |
| Shallow copy |  arr.copy()  |   O(n)   |   O(n)   |
| Slice copy   |  arr[:]      |   O(n)   |   O(n)   |
|  list(arr)   |  list(arr)   |   O(n)   |   O(n)   |



Aggregation Functions
| Function   | Example    | Time     | Space |
| ---------- | ---------- | -------- | ----- |
|  min(arr)  |  min(arr)  |   O(n)   | O(1)  |
|  max(arr)  |  max(arr)  |   O(n)   | O(1)  |
|  sum(arr)  |  sum(arr)  |   O(n)   | O(1)  |
|  any(arr)  |  any(arr)  |   O(n)   | O(1)  |
|  all(arr)  |  all(arr)  |   O(n)   | O(1)  |



Comparison
| Operation     | Example        | Time     | Space |
| ------------- | -------------- | -------- | ----- |
| Equality      |  arr1 == arr2  |   O(n)   | O(1)  |
| Lexicographic |  arr1 < arr2   |   O(n)   | O(1)  |
