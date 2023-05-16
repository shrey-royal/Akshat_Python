# 2. Python Program to swap two elements in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list: ", numbers)

i = int(input("Enter the index of first element: "))
n = int(input("Enter the index of second element: "))

numbers[i], numbers[n] = numbers[n], numbers[i]

print("After swapping first and last element: ", numbers)