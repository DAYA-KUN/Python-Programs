dict1={1:"Daya",2:"Ebi",3:"Shar"}

#1st method
reversed_dict={}

for key,value in dict1.items():
    reversed_dict[value]=key

print(reversed_dict)

#2nd method
reversed_dict={v:k for k,v in reversed_dict.items()}
print(reversed_dict)