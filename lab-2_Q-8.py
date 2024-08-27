a = int(input("Enter the 1st side of the triangle : "))
b = int(input("Enter the 2nd side of the triangle : "))
c = int(input("Enter the 3rd side of the triangle : "))

ct = 0
if((a*a)+(b*b)==(c*c)):
    ct=ct+1
if((a*a)+(c*c)==(b*b)):
    ct=ct+1
if((c*c)+(b*b)==(a*a)):
    ct=ct+1

if(ct==0):
    print("The given triangle is not a right triangle.")
if(ct!=0):
    print("The given triangle is a right triangle.")