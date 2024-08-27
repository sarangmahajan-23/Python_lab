num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
def cal_lcm(x, y):
 if x > y:
        greater = x
 else:
        greater = y
 while(True):
    if((greater%x == 0) and (greater%y == 0)):
        lcm = greater
        break
    greater += 1
 return lcm
print("The L.C.M. is", cal_lcm(num1, num2))
def cal_gcd(x,y):
    if y==0:
        return x
    return cal_gcd(y,x%y)
print("The G.C.D. is", cal_gcd(num1, num2))