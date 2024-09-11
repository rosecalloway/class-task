Employee={
    "name":"A",
    "age":40,
    "type":{"developer":["ios","android"]},
    "permanent": False,
    "salary":30000,
    100:(1,2,3),
    4.5:{6,5,True,7},
    True:1,
}
print(len(Employee))
print(type(Employee))
print(Employee["type"])
print(Employee["type"]["developer"][1])
print(Employee[4.5])
print(Employee.update({"permanent":True}))
Employee["gender"] = "male"
print(Employee)
Employee.pop("age")
print(Employee)
for x in Employee.keys():
  print(x)
for x in Employee.values():
  print(x)
for x in Employee.items():
  print(x)  


