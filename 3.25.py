print ("Name: Zarar Ali Shah")
print("Roll #: 18B-075-CS(A)")
print("Assignment")

print("\n\n  Exercise # 3.25")

list = []
for x in range(6):
    a = input("Enter the names of the students"+str(x+1)+":")
    list.append(a)

for x in range(6):
    if list[x][:1]not in ('n','N','o','O','p','P','Q','q','r','R','s','S','t','T','u','U','v','V','x','X','y','Y','z','Z'):
        print(list[x])
