a={1,3,5,8,3,2}
b={0,False,1,5}
print(a)
print(b)
print(len(a))
print(type(a))
print(len(b))
print(type(b))
a.add(10)
print(a)
a.remove(8)
print(a)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a & b)
for x in a:
    print(x)
    if 3 in a:
        print("3 is present")
        
