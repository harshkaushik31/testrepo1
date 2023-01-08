import pickle
myfile = open('student.dat','wb')
student = []
ans = 'y'
while ans.lower() == 'y':
    roll = int(input("Enter roll number: "))
    name = input("Enter name of the student: ")
    marks = int(input("Enter marks: "))
    student.append([roll,name,marks])
    ans = input("Do you want to continue(y): ")
pickle.dump(student,myfile)
myfile.close()
myfile = open('student.dat','rb')
student = pickle.load(myfile)
print(student)
myfile.close()