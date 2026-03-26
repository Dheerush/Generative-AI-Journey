# ======================================================= List/Arrays ===================================================================
# 1. Lists in Python are the most flexible and commonly used data structure for sequential storage. 
# 2. They are similar to arrays in other languages but with several key differences:
#    - Dynamic Typing:  Python lists can hold elements of different types in the same list. 
#    - Dynamic Resizing: Lists are dynamically resized, meaning you can add or remove elements without declaring the size of the list upfront.
#    - Built-in Methods: Python lists come with numerous built-in methods that allow for easy manipulation of the elements within them, including methods for appending, removing, sorting and reversing elements.



# Ways to initiliaze an array
arr1 = ['a', False, True, None, 10.33, 23]
arr2= []
arr3= [0]*5
arr4= list((1,3,4))

print("arr1: ", arr1)
print("arr2: ", arr2)
print("arr3: ", arr3)
print("arr4: ", arr4)

print("                        ")


# Loops: Traversal in arrays

#                JS Concept                        |              Python Equivalent
#--------------------------------------------------------------------------------------------------
#               for loop	                       |               for i in range()
#               for...of	                       |               for x in arr
#               forEach	                           |               enumerate()
#               while	                           |               while
#               map	                               |               list comprehension



num1= [10,20,30,40,50,60,70,80]
print("Using the for loop")
for x in num1:
    print(x)


print("Using the index")
for i in range(len(num1)):
    print(i, num1[i])


print("Using the while")
index = 0
while index<len(num1):
    print(index, num1[index])
    index=index+1

print("Using the enumerate")
for i, val in enumerate(num1):
    print(i,val)




#Exercise

numArr1= [10,21,30,43,50,60]; 
#1  Find sum of array
totalSum=0
for x in numArr1:
    totalSum= totalSum + x

print("Sum of all numbers in the array: ",totalSum)

#2. Count numbers > 10
count = 0
for x in numArr1:
    if x>10:
        count=count+1
    else:
        continue

print("Count of numbers >10: ", count)

#3. Print all the even numbers
for x in numArr1:
    if x % 2==0:
        print(x)
  




# Arrays built-in methods
# Method                 | Functionality
# ---------------------------------------------------------
# 1. append(x)           | Add element at end
# 2. insert(i, x)        | Insert at specific index
# 3. extend(iterable)    | Add multiple elements
# 4. pop([i])            | Remove & return element (default: last)
# 5. remove(x)           | Remove first occurrence of value
# 6. clear()             | Remove all elements
# 7. index(x)            | Get index of first occurrence
# 8. count(x)            | Count occurrences of value
# 9. sort()              | Sort list (ascending by default)
# 10. reverse()          | Reverse list (in-place)
# 11. copy()             | Create shallow copy

# NOTE : There are other built-in methods of python (not just array). For example:
# 1. len(arr)     → length
# 2. sum(arr)     → sum of elements
# 3. max(arr)     → maximum value
# 4. min(arr)     → minimum value
# 5. sorted(arr)  → returns new sorted list

# ====================== INITIAL LIST ======================
nums = [10, 20, 30, 40, 10, 50]
print("Original:", nums)


# ====================== LIST METHODS ======================

# append()
nums.append(60)
print("After append:", nums)

# insert()
nums.insert(2, 99)
print("After insert:", nums)

# extend()
nums.extend([70, 80])
print("After extend:", nums)

# pop()
nums.pop()        # removes last
nums.pop(1)       # removes index 1
print("After pop:", nums)

# remove()
nums.remove(10)   # removes first occurrence
print("After remove:", nums)

# count()
print("Count of 10:", nums.count(10))

# index()
print("Index of 30:", nums.index(30))

# copy()
nums_copy = nums.copy()
print("Copy:", nums_copy)

# reverse()
nums.reverse()
print("After reverse:", nums)

# sort()
nums.sort()
print("After sort:", nums)

# clear()
temp = nums.copy()
temp.clear()
print("After clear:", temp)


# ====================== BUILT-IN FUNCTIONS ======================

print("Length:", len(nums))
print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))

# sorted() → returns new list
sorted_nums = sorted(nums, reverse=True)
print("Sorted (new):", sorted_nums)


# ====================== TRAVERSAL ======================

print("\nTraversal (for):")
for x in nums:
    print(x)

print("\nTraversal (index):")
for i in range(len(nums)):
    print(i, nums[i])

print("\nTraversal (enumerate):")
for i, val in enumerate(nums):
    print(i, val)


# ====================== CONDITIONS ======================

print("\nNumbers > 30:")
for x in nums:
    if x > 30:
        print(x)


# ====================== LIST COMPREHENSION ======================

# map equivalent
doubled = [x * 2 for x in nums]
print("Doubled:", doubled)

# filter equivalent
greater_than_30 = [x for x in nums if x > 30]
print("Filtered (>30):", greater_than_30)

# combined
combined = [x * 2 for x in nums if x > 30]
print("Combined:", combined)


# ====================== MAP ======================

mapped = list(map(lambda x: x * 2, nums))
print("map result:", mapped)


# ====================== FILTER ======================

filtered = list(filter(lambda x: x > 30, nums))
print("filter result:", filtered)


# ====================== REVERSE (NEW LIST) ======================

rev = nums[::-1]
print("Reversed (new):", rev)


# ====================== FINAL ======================
print("\nFinal nums:", nums)




# ==================================== 2-D Arrays/Matrix =======================================================
# To be done later































