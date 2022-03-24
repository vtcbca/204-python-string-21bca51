#Write a script to enter five string in a list and check and print string wohse length has even number of character without any string function.
l=[]
count=0
def createList(l):
    for i in range(5):
        s=input('Enter any string : ')
        l.append(s)
    print(l)
createList(l)
for i in l:
    for j in i:
        count=count+1
    if(count%2==0):
        print('The list is {} and its length is {}.'.format(l[i],count))
    print(i)

