import pickle

data={"Name":"Daya","Age":20,"Area":"Chennai"}

with open('data.pkl','wb') as file:
    pickle.dump(data,file)#Pickling - Converts Python object into Byte Stream

with open('data.pkl','rb') as file:
    data=pickle.load("data.pkl")

print(data)

