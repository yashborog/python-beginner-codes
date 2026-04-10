a=int(input("enter first no: "))
b=int(input("enter second no: "))
c=int(input("enter third no: "))
print("original numbers: ",a,b,c)
a,b,c=a,a+b,a+c+b
print("after swaping:", a,b,c)
