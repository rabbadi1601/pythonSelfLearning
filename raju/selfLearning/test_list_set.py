l1=[2,4,5,2,1,6,4,3,2,1,1,1]

a=set()
i=0
for i in range(len(l1)):
    a.add(l1[i])

l1.append(55)
print("aaa",a)

a1=set()
for i in l1:
    a1.add(i)
print(a1)

# Tuple
b=(20,)
print(type(b))

print(b)

x=list(b)
x.append(67)
x.append(44)
x.append(66)
x.sort()
b=tuple(x)
print(b)
