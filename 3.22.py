print ("Name: Zarar Ali Shah")
print("Roll #: 18B-075-CS(A)")
print("Assignment")

print("\n\n  Exercise # 3.22")
list = []
for x in range(8):
    a=int(input("Enter the number "+str(x+1)+":"))
    list.append(a)

for a in range(8):
    y = list[a]
    sq = y**2
    if sq%8==0:
        print(y)
