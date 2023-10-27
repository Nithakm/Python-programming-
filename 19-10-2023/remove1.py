list=[17,12,53,20,46,32]
print("orginal list")
print(list)
for i in list:
    if i%2==0:
        list.remove(i)
print("list after removing even number")
print(list)
