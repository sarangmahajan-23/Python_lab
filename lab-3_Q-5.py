import statistics
arr = []

n = int(input("Enter number of elements : "))
print("Enter n elements : ")
sum = 0
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
    sum+=ele

print("Given list is : ")
print(arr)
print("mean : ",sum/n)
print("Median : ",statistics.median(arr))
print("Mode : ",statistics.mode(arr))