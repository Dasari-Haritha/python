from array import*
a=array("i",[])
ln=int(input("enter array size:"))
for i in range(ln):
    b=int(input("enter values"))
    a.append(b)
for i in range(a[0],a[i]+1):
    for j in range(1,14):
        print(i,"*",j,"=",i*j)
    print(i)
    