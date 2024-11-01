
with open('./File handling/daya.txt', 'r') as file:
    content1 = file.readline()
    print(content1)
    content2 = file.readlines()
    print(content2)

