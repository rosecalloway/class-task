list1 = [1,3,7,8,2]
sum=0
for i in range(len(list1)): 
    if i%2!=0: 
        sum+=list1[i]
print(sum)