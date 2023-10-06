a=int(input("enter the number of limit:"))
lst=[]
v="over"
for i in range(0,a):
    n=int(input("enter the elements:"))
    if n<99:
        lst.append(n)
    else:
        lst.append(v)
print(lst)
    
    
