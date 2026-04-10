n=int(input("enter no. of students: "))
stu={}
for i in range(1,n+1):
    print("Enter details of student", i)
    roll_no=int(input("Roll no."))
    name= input("name")
    mrks=float(input("marks"))
    d={"roll no":roll_no,"name":name,"marks":mrks}
    key="stu"+ str(i)
    stu[key]=d
print ("Students above 75:")
for i in range (1,n+1):
    key="stu"+str(i)
    if stu[key]["marks"]>=75:
        print (stu[key])
    
