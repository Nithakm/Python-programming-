n=(input("Enter a string which has replaced words"))
print("the orginal string is",n)
k="$"
res=n[0]+n[1:].replace(n[0],k)
print("replaced sring is:",[res])
