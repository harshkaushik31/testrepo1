import pickle
myfile = open('student.dat','wb')
student = []
ans = "y"
while ans == "y" or ans == "Y":
    roll_number = int(input("Enter roll number: "))
    name = input("Enter name: ")
    student.append([roll_number,name])
    ans = input("Do you want to continue(y):")
pickle.dump(student,myfile)
myfile.close()
myfile = open('student.dat','rb')
student = pickle.load(myfile)
ans = "y"
while ans.lower() == 'y':
    found = False
    n = int(input("Enter roll number to search for: "))
    for i in student:
        if i[0] == n:
            print(" The name is: ", i[1])
            found = True
            break
    if found == False:
        print("Roll number not found!")
    ans = input("Do you want to search more(y)")
myfile.close()