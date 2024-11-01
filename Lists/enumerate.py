students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
attendance = [True, False, True, False, True]

for roll_number, (student, is_present) in enumerate(zip(students, attendance), start=1):#((alice,true),(bob,f),(char,t),(david,f),(eve,t))
    if not is_present:
        print(f"Roll Number {roll_number}: {student} is absent")

# enumerate(iterable,start="")

# l=['a','b','c']
# for i,value in enumerate(l):
#     print(i,value)