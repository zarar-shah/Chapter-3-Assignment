print("Name: Zarar Ali Shah")
print("Roll #: 18B-075-CS (A)")
print("Assignment")

print("\n Exercise 3.42\n")

def avg(x):
    print("\n\n")
    for a in range(len(grade)):
        total=0
        avg=0
        for b in range(len(grade[a])):
            total+= grade[a][b]
        avg=total/len(grade[a])
        print("The average grade of Student",a+1,":",avg)
        
grade=[]
st_num = int(input("How many students?:"))
grade=[[] for row in range(st_num)] 
for x in range(st_num):
    st_sub = int(input("How many subject of student"+str(x+1)+":"))
    for y in range(st_sub):
        m = int(input("Please enter marks of Student"+str(x+1)+" Subject"+str(y+1)+":"))
        grade[x].append(m)
avg(grade)
