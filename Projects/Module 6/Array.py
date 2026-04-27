#array tests

#creating an array
my_array = [1, 2, 3, 4, 5]
print(my_array)
#accessing elements
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 3 

#modifying elements
my_array[1] = 10
print(my_array)  # Output: [1, 10, 3, 4, 5] 
#adding elements
my_array.append(6)
print(my_array)  # Output: [1, 10, 3, 4, 5, 6]
#removing elements
my_array.remove(10)
print(my_array)  # Output: [1, 3, 4, 5, 6]
#slicing arrays
print(my_array[1:4])  # Output: [3, 4, 5]
#length of array
print(len(my_array))  # Output: 5
#iterating through an array
for element in my_array:
    print(element)
# Output:
# 1
# 3
# 4
# 5
# 6

