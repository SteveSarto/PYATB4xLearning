#Write a program that classifies a triangle based on its side lengths.

#Given three input values representing the lengths of the sides,

#determine if the triangle is equilateral (all sides are equal),

#isosceles (exactly two sides are equal), or scalene (no sides are equal).

#Use an if-else statement to classify the triangle.

l1 = int(input("enter length1"))
l2 = int(input("enter length2"))
l3 = int(input("enter length3"))

if l1 == l2 == l3:
    print("it is equilateral triangle")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("it is an isosceles triangle")
else:
    print("scalene triangle")