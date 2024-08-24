# Exploring Python List Methods

### Python List Methods

**append()**

**Description:** Adds an element to the end of the list. **Syntax:** `list.append(element)` **Return Type:** None

```Python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```
**extend()**

**Description:** Appends the elements of another iterable to the end of the list.**Syntax:** `list.extend(iterable)`**Return Type:** None

```Python

my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```
**insert()**

**Description:** Inserts an element at a specified index.**Syntax:** `list.insert(index, element)`**Return Type:** None

```Python

my_list = [1, 2, 3]
my_list.insert(1, 0)
print(my_list)  # Output: [1, 0, 2, 3]
```
**remove()**

**Description:** Removes the first occurrence of a specified element from the list.**Syntax:** `list.remove(element)`**Return Type:** None

```Python

my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]
```
**pop()**

**Description:** Removes and returns the element at a specified index. If no index is provided, removes and returns the last element.**Syntax:** `list.pop(index=None)`**Return Type:** The removed element

```Python

my_list = [1, 2, 3]
removed_element = my_list.pop(1)
print(my_list)  # Output: [1, 3]
print(removed_element)  # Output: 2
```
**clear()**

**Description:** Removes all elements from the list.**Syntax:** `list.clear()`**ReturnType:** None

```Python

my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
```
**index()**

**Description:** Returns the index of the first occurrence of a specified element.**Syntax:** `list.index(element, start=0, end=None)`**Return Type:** The index of the element

```Python

my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1
```
**count()**

**Description:** Returns the number of occurrences of a specified element in the list.**Syntax:** `list.count(element)`**Return Type:** The number of occurrences
```Python
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2
```
**sort()**

**Description:** Sorts the elements of the list in ascending order.**Syntax:** `list.sort(key=None, reverse=False)`**Return Type:** None
```Python
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]
```
**reverse()**

**Description:** Reverses the elements of the list.**Syntax:** `list.reverse()`**Return Type:** None
```Python
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]
```
**copy()**

**Description:** Returns a shallow copy of the list.**Syntax:** `list.copy()`**Return Type:** A new list
```Python
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]
```

**Slicing**

1. `list[start:stop:step]`: Extracts a sublist from the original list, starting at `start` (inclusive), ending at `stop` (exclusive), and taking every `step`th element.
```Python
my_list = [1, 2, 3, 4, 5]
sublist = my_list[1:4:2]  # Extracts elements at indices 1 and 3
print(sublist)  # Output: [2, 4]
```
**Membership Testing**
1. `in`: Checks if an element is present in the list.
2. `not in`: Checks if an element is not present in the list.

```Python 
my_list = [1, 2, 3]
if 2 in my_list:
    print("2 is in the list")
```
**List Comprehension**
1. A concise way to create new lists based on existing lists or other iterables.
2. Can be used to perform operations on each element of the list and create a new list.
```Python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```
**Built-in Functions**
1. `len(list)`: Returns the length of the list.
2. `max(list)`: Returns the maximum element in the list.
3. `min(list)`: Returns the minimum element in the list.
4. `sum(list)`: Returns the sum of all elements in the list.
```Python
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
max_value = max(my_list)
min_value = min(my_list)
sum_value = sum(my_list)
```