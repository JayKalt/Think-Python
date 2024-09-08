# Extend the above program so that the sides can be given to the function in any order.

print("Enter the sides of a triangle: ")
side_a = int(input("Side a: "))
side_b = int(input("Side b: "))
side_c = int(input("Side c: "))

if((side_a ** 2 + side_b ** 2 == side_c) ** 2 or (side_a ** 2 + side_c ** 2 == side_b ** 2) or (side_b ** 2 + side_c ** 2 == side_a ** 2)):
        print("True")
else:
        print("False")
