print("Name: Zarar Ali Shah")
print("Roll #: 18B-075-CS (A)")
print("Assignment")

print("\n Exercise 3.40\n")

list = []
for x in range(5):
    a = input("Please enter Soccer Player "+str(x+1)+" Name:")
    list.append(a)

for x in range(5):
    if list[x][:1]not in ('n','N','o','O','p','P','Q','q','r','R','s','S','t','T','u','U','v','V','x','X','y','Y','z','Z'):
        print(list[x])


