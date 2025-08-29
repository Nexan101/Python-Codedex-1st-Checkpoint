from math import pi

area = 0
side = 0
base = 0
height = 0
length = 0
width = 0


while True:
    print("=================")
    print("Nevan's Calculate")
    print("=================\n")
    print("1. Square \n2. Rectangle \n3. Triangle \n4. Circle \n5. Quit \n")        
        
    choice = input("Which Shape: ")
    if choice == "1":
        side = int(input("What is the sides measurements ? "))
        area = (side ** 2)
        print(f"The area is {area}")
    elif choice == "2": 
        length = int(input("Length: "))
        width = int(input("Width: "))
        area = (length * width)
        print(f"The area is {area}")
    elif choice == "3":           
        height = int(input("Height: "))
        base = int(input("Base: "))
        area = (height * base) / 2
        print(f"The area is {area}")
    elif choice == "4":
        radius = int(input("Radius: "))
        area = pi * (radius ** 2)
        print(f"The area is {area}")
    elif choice == "5": 
        break
    else: 
        print("Invalid try again!")