#Bubble sort
def bubble_sort(arr):
  
  for n in range(len(arr) - 1, 0, -1):
    
    swapped = False
    
    for i in range(n):
      if arr[i] > arr[i + 1]:
        
        swapped = True
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
      
      if not swapped:
        return

#merge sort
def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	i = 0	 
	j = 0	 
	k = l	 

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1



def mergeSort(arr, l, r):
	if l < r:

		m = l+(r-l)//2

		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)
		
#selection sort
def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			if array[j] < array[min_index]:
				min_index = j
		(array[ind], array[min_index]) = (array[min_index], array[ind])


#insertionsort
def insertionSort(arr):
	n = len(arr) 
	
	if n <= 1:
		return 

	for i in range(1, n):
		key = arr[i] 
		j = i-1
		while j >= 0 and key < arr[j]: 
			arr[j+1] = arr[j] 
			j -= 1
		arr[j+1] = key 


  





print("Enter the operation to perform :")
print("1.bubble sort\n2.Merge Sort\n3. Selection Sort\n 4.Insertion Sort")
no=int(input("Enter the choice :"))
arr = [39, 12, 18, 85, 72, 10, 2, 18]

if(no==1):
	
	bubble_sort(arr)
	print(arr)
elif(no==2):
	mergeSort(arr,0,len(arr)-1)
	print(arr)
elif(no==3):
	selectionSort(arr,len(arr))
	print(arr)
else:
	insertionSort(arr)
	print(arr)