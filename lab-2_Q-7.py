a = 20
print("The prime numbers less than 20 are : ")
for num in range(1,21):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break

        else:
            print (num)