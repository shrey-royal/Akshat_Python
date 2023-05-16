# 3. Swap elements in a String list

names = ["John", "Jane", "Jack", "Jill", "Joe"]
print("Original list: ", names)

i = int(input("Enter the index of first element: "))
n = int(input("Enter the index of second element: "))

names[i], names[n] = names[n], names[i]

print("After swapping first and last element: ", names)
