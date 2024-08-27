a = int(input("Enter 1 to convert Celsius into Fahrenheit.\nEnter 2 to convert Fahrenheit into Celsius :"))
deg = 0
if(a==1):
    deg = int(input("Enter your temperature in Celsius : "))
if(a==2):
    deg = int(input("Enter your temperature in Fahrenheit : "))

if(a==1):
    ans = ((deg*9)/5)+32
    print("Temperature in Fahrenheit is : ",ans)
if(a==2):
    ans = ((deg-32)/9)*5
    print("Temperature in Celsius is : ",ans)