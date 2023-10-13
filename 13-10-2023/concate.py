dict1={4:7,7:9}
dict2={5:9,2:5}
dict3={}
print("the first dictionary is")
print(dict1)
print("the second dictionary is")
print(dict2)
for dict in (dict1,dict2):dict3.update(dict)
print("the concatenate dictionary is:")
print(dict3)
