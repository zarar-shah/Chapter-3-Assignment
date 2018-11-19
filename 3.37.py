print("Name: Zarar Ali Shah")
print("Roll #: 18B-075-CS (A)")
print("Assignment")

print("\n Exercise 3.37\n")

def points(x1,y1,x2,y2):
    if x1==x2:
        print("The slope is infinity ",end=" ")
    else:
        slope = float((y2-y1)/(x2-x1))
        print("The slope is", str(slope),end=" ")

    import math
    distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    print("and the distance is", str(distance))

x1 = float(input("Please enter x1 coordinates :"))
y1 = float(input("Please enter y1 coordinates :"))
x2 = float(input("Please enter x2 coordinates :"))
y2 = float(input("Please enter y2 coordinates :"))

points(x1,y1,x2,y2)
