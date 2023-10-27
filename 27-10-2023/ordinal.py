a = input("Enter the word \n")
for i in a:
    print(ord(i),"\n")

Tuple
t=(1,2,3,4,5)
print(t)
l=list(t)
a=int(input("Enter item to add \n"))
l.append(a)
t=tuple(l)
print(t)
