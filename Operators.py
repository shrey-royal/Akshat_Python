'''
In Python we have the following operators:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators

1. Arithmetic Operators -> +, -, *, /, %, ** (power), // (floor division)

base**exponent -> base to the power of exponent
** -> 2**3 = 8
ex:- 2**3 = 2*2*2 = 8

floor division -> // -> 9//2 = 4
ex:- 9//2 = 9/2 = 4.5 -> 4
12//5 = 12/5 = 2.4 -> 2
18//7 = 18/7 = 2.57 -> 2

2. Assignment Operators -> =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=

3. Comparison Operators -> ==, !=, >, <, >=, <=

4. Logical Operators -> and(&&), or(||), not(!)

5. Identity Operators -> is, is not

6. Membership Operators -> in, not in

7. Bitwise Operators -> &, |, ^, ~, <<, >>

^ -> XOR
ex: 
0 ^ 0 -> 0
0 ^ 1 -> 1
1 ^ 0 -> 1
1 ^ 1 -> 0

~ -> NOT
ex:
~0 -> 1
~1 -> 0





'''

# print(2 ** 3)
# print(9 // 2)
# print(12 // 5)
# print(18 // 7)

# base = 2
# exponent = 3

# print(base, exponent)   
# base **= exponent   #
# print(base, exponent)

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print(not True)
# print(not False)

# identity operators

# print(5 is 50)   # True -> it checks the value

# print(5 is 50)
# a = 5
# b = 5

# print(id(a), id(b), sep = "\t")
# print(a is b)   # True -> it checks the value and the memory location of the variable

# print("Hello" is not "Hello_")

# membership operators

# print("Hello" in "Hello World") # it checks if the value is present in the string or not

# print("Hello" not in "Hello World") # it checks if the value is not present in the string or not


# print(0 ^ 0)
# print(0 ^ 1)
# print(1 ^ 0)
# print(1 ^ 1)

# print(~0)   # it gives the 2's complement of the number
# print(~1)   # it gives the 2's complement of the number