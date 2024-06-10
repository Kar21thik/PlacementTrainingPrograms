"""def InsertionSort(array):
    j=0
    for i in range(1,len(array)):
        element = array[i]
        j=i-1
        while j>= 0 and element< array[i]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=element
    
arr=list(map(int,input("Enter the elements").split(",")))
InsertionSort(arr)
print(arr)"""


def insertionSort(array):
    n = len(array)  
      
    if n <= 1:
        return  
 
    for i in range(1, n):  
        element = arr[i]  
        j = i-1
        while j >= 0 and element < arr[j]:  
            array[j+1] = arr[j]  
            j -= 1
        arr[j+1] = element
  

arr = list(map(int,input("Enter the elements").split(",")))
insertionSort(arr)
print(arr)