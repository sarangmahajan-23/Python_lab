a = int(input("Enter the marks for test1 : "))
b = int(input("Enter the marks for test2 : "))
c = int(input("Enter the marks for test3 : "))

if(a<b):
    if(a<c):
        print("Average of best two test marks out of three test’s marks is :",(b+c)/2)
    if(a>c):
        print("Average of best two test marks out of three test’s marks is :",(b+a)/2)
if(a>b):
    if(b<c):
        print("Average of best two test marks out of three test’s marks is :",(a+c)/2)