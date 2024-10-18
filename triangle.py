import math 

ang1 = float(input("Enter Angle 1: "))
ang2 = float(input("Enter Angle 2: "))
ang3 = float(input("Enter Angle 3: "))

c1 = float(input(" Enter x coordinate:"))
c2 = float(input(" Enter y coordinate:"))

tri = 0 
if ang1 == ang2 == ang3:
    print(" Triangle: Equilateral Triangle")
elif ang1 == ang2 or ang2 == ang3 or ang3 == ang1:
    print("Triangle: Isosceles Triangle ")
elif ang1 == 90 or ang2 == 90 or ang3 == 90:
    print(" Triangle: Right Triangle ")
elif ang1 + ang2 +ang3 != 180:
    print(" Triangle: Not a triangle")
else: 
    print(" Triangle: Scalene Triangle ")

if c1 > 0 and c2 > 0:
    print(" Point located: Quadrant I")
elif c1 > 0 and c2 < 0:
    print( " Point located: Quadrant IV")
elif c1 < 0 and c2 < 0:
    print( " Point Located: Quadrant III")
else:
    print(" Point located: Quadrant II")


length = math.sqrt ((math.pow(c1,2))+(math.pow(c2,2)))
print(f" Length Side 3 : The third side is {length} units ")