print("Name: Zarar Ali Shah")
print("Roll #: 18B-075-CS (A)")
print("Assignment")
print("Exercise # 3.20")

user_str=[]
for x in range(5):
    a = input("Please enter word"+str(x+1)+":")
    user_str.append(a)

for x in range(5):
    print(user_str[x][:3])
