print ("Name: Zarar Ali Shah")
print("Roll #: 18B-075-CS(A)")
print("Assignment")
#3.17 Using eval function to evaluate the folowing strings.
print("\n  Exercise 3.17")

print("\nPart A")
a = eval('2 * 3 + 1')
print("Part a will be evaluated as", a)

print("\nPart B")
b = eval("'hello'") #Here was an error
print("In Part B, in the question there were no inverted commas which means that the 'hello' string was not defined, so the evaluated funciton will be shown as", b)

print("\nPart C")
c = eval("'hello' + '' + 'world!'")
print("Part c will be evauated as", c)

print("\nPart D")
d = eval("'ASCII'.count('I')")
print("Part d will be evaluated as", d)

print("\nPart E")
e = eval("'x = 5'") #Here was an error
print("In Part e there was also the same error which was occured above in part B, so the evaluated function will be shown as", e)
