print ("Name: Zarar Ali Shah")
print("Roll #: 18B-075-CS(A)")
print("Assignment")

print("\n\n  Exercise # 3.24")

list = []
for x in range(5):
    s = input("Enter the word "+str(x+1)+":")
    list.append(s)

for x in range(5):
    if list[x]!='secret':
        print(list[x])
                
