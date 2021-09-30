list=[]
for i in range(5):
    numbers = int(input("Enter the numbers:"))
    list.append(numbers)
sumofnumbers=sum(list)
print("sum is :",sumofnumbers)
print("average is",sumofnumbers/5)