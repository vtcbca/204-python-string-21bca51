#write a script to create two list student and address which contain the name of student and their respective addresss.Print student name with it's address.

student=[]
address=[]
count=0
def createList():
    for i in range(5):
        l=input('Enter name of the student : ')
        s=input('Enter address of the student : ')
        student.append(l)
        address.append(s)
    for i in range(5):
        print(' {} --> {} .'.format(student[i],address[i]))    
createList()
