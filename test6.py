import pickle
myfile = open('Emp.dat','wb')
emp={}
ans = 'y'
while ans.lower()=='y':
    e_number = int(input('Enter employee number: '))
    e_name = input('Enter employee name: ')
    emp[e_number] = e_name
    ans = input("Do you want to continue(y): ")
pickle.dump(emp,myfile)
myfile.close()
myfile = open('Emp.dat','rb')
emp = pickle.load(myfile)
print(emp)
myfile.close()