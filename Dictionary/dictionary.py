#create list my_dict
my_dict={'name':'Daya','age':20,'city':'Chennai'}

print(my_dict['id'])
print(my_dict.get('id'))

#Looping in dict

#Using keys
for i in my_dict:
    print(i,end=" ")

#Using Values
for value in my_dict.values():
    print(value,end=" ")

#Using Key-Value Pairs
for key,value in my_dict.items():
    print(key,value)
