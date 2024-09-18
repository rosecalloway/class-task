a = input("enter a: ")
b= input("enter b: ")
print(a,type(a))
a=int(a)
b=int(b)
print(a,type(a))
x = lambda a,b: a * b
print(x(a,b))
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
e = [2, 7, 10, 15, 8]
newlist = [x for x in e if x in [7, 15]]
print(newlist)
def myfun(kiki):
  return len(kiki)
x = map(myfun,('eren','rose','shinbou'))
print(x)
print(list(x))

def square(n):
  return n**2
x = map(square,(5,6,7))
print(x)
print(list(x))  
arr = [[1,2,3], [4,5,6], [7,8,9]]
for row in arr:
  for col in row:
    print(col, end=" ")
  print()  