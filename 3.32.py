print("Name: Zarar Ali Shah")
print("Roll #: 18B-075-CS (A)")
print("Assignment")

print("\n Exercise 3.32\n")

number = int(input("Please enter a 4-digit number:"))
a = []
for x in range(4):
    y = int(number%10)
    a.insert(0,y)
    number = number/10

for x in range(4):
    print(a[x])


