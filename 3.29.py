print("Name: Zarar Ali Shah")
print("Roll #: 18B-075-CS (A)")
print("Assignment")

print("\n Exercise 3.29\n")

pos_integer = int(input("Please enter a positive integer number:"))
for x in range(1,pos_integer+1):
    if pos_integer%x == 0:
        print(x)
