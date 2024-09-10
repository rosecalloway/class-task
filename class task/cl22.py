#Multiplication
num=int(input("Enter a number:"))
def multiplication(num):
    for i in range(1,11):

        if i ==6:

            continue

        if i ==9:

            break

        print(f"{num}*{i} = {num*i}")

multiplication(num)
