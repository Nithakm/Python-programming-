n=int(input("enter a total number: "))
sum=0
for i in range(n):
    x=int(input("enter a number: "))
    sum=sum+x
print("sum:",sum)
avg=sum/n
print("average:",avg)
