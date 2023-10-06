a=str(input("enter the sentence:"))
b=str(input("enter the word you want to count:"))
lst=a.split()
count=0
for n in lst:
    if n==b:
        count=count+1
print("number of",n,"is",count)
