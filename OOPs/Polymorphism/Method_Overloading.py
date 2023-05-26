"""
Method Overloading: The assignment of more than one behavior to a particular method is called method overloading.
"""

class Calculator:    
    def add(self, a, b, c=0, d=0):
        return a + b + c + d
    

obj = Calculator()
print(obj.add(1, 2))
print(obj.add(1, 2, 3))
print(obj.add(1, 2, 3, 4))




"""
1. Banking System:
   Problem Statement: Implement a banking system where customers can perform various transactions such as deposit, withdrawal, and transfer. The system should support different methods for each transaction type, allowing flexibility in parameter types. For example, the deposit method should accept an account number and either a single amount or a list of amounts to be deposited.

2. E-commerce Website:
   Problem Statement: Develop an e-commerce website where users can place orders for products. Implement a checkout process that can handle different types of payments, such as credit cards, PayPal, and gift cards. Use method overloading to create separate methods for processing each payment type, accepting different parameter types based on the specific payment method.

3. Shape Calculator:
   Problem Statement: Build a shape calculator that can calculate the area and perimeter of various shapes, such as rectangles, circles, and triangles. Implement method overloading to handle different parameter types for each shape. For example, the rectangle method should accept either the length and width or just the length for calculating area and perimeter.

4. File Handler:
   Problem Statement: Create a file handling module that can read and write data to different file formats, such as CSV, JSON, and XML. Use method overloading to define separate methods for reading and writing data to each file format, allowing different parameter types based on the format being used. For instance, the write method should accept a file path and either a dictionary or a list of dictionaries for writing data to a JSON file.

5. Image Processing:
   Problem Statement: Develop an image processing library that can perform various operations on images, such as resizing, cropping, and applying filters. Implement method overloading to handle different parameter types for each operation. For example, the resize method should accept either a scaling factor or specific width and height dimensions to resize the image.
"""