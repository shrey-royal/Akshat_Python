# 1. Python Program to interchange first and last elements in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list: ", numbers)

first_ele = numbers[0]
numbers[0] = numbers[-1]
numbers[-1] = first_ele

print("After swapping first and last element: ", numbers)