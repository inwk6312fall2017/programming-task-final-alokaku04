book1=open("Book1.txt","r")
y1=book1.read()
x1=y1.split()
max1=max(x1,key=len)
book2=open("Book2.txt","r")
y2=book1.read()
x2=y2.split()
max2=max(x2,key=len)


book3=open("Book3.txt","r")
y3=book3.read()
x3=y3.split()
max3=max(x3,key=len)
r=[max1,max2,max3]
print(max(r,key=len))