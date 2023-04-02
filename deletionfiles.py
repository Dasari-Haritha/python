from array import*
a=array("i",[1,4,2,3,5])
print("old array Values")
print(a)
print("delMenu\n1.First\n2.Last\n3.Delany\n.Enterchoice[1..3]:")
ch=eval(input())
if (ch==1):
    a.pop(0)
    print("new values of array")
    for i in a:
        print(i,end=" ")
elif (ch==2):
    a.pop()
    print("new values of array")
    for i in a:
        print(i,end=" ")
    
elif (ch==3):
    x=eval(input("enter del pos:"))
    a.pop(x)
    print("new values of array")
    for i in a:
        print(i,end=" ")
else:
    print("invalid choice")
    
           