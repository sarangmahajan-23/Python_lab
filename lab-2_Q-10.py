num=int(input("Enter a number:"))
reversenum=0
n=num
while n>0:
    t=n%10
    reversenum=(reversenum*10)+t
    n=n//10

if(num==reversenum):
    print("Given number is a palindrome.")
if(num!=reversenum):
    print("Given number is a not a palindrome.")

for i in range(0,11): 
    ct = 0
    a = num
    while(a!=0):  
     if(a%10==i):
        ct+=1
        a = a//10
    if(ct>0):
       print("The number of occurences of digit ",i,"are :",ct)