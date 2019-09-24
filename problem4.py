a=[]
n=input("enter the number of elememts in list")
for x in range(0,n):
	element=input("enter elements")
	a.append(element)
b=set()
unique=[]
for x in a:
	if x not in b:
		unique.append(x)
		b.add(x)
print("non-duplicate")
print(unique)