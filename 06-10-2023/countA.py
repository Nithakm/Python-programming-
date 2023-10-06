lst=["apple","banana","orange","cherry"]
count=0
print(lst)
a=input("Enter the letter required:")
for n in lst:
    for f in n:
        if f==a:
            count+=1
print("The number of",a,"is to",count)
