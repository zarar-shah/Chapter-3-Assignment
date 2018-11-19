print("Name: Zarar Ali Shah")
print("Roll #: 18B-075-CS (A)")
print("Assignment")

print("\n Exercise 3.43\n")

def hit(x1,y1,r,x2,y2):
    import math
    dist = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    if dist<=r:
        print("Its a Hit!")
    else:
        print("Missed it!")

x1 = float(input("Please enter Centre x coordinates:"))
y1 = float(input("Please enter Centre y coordinates:"))
r = float(input("Please enter Radius              :"))
x2 = float(input("Please enter Hit x coordinates   :"))
y2 = float(input("Please enter Hit y coordinates   :"))

hit(x1,y1,r,x2,y2)
