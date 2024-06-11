def partitionArray(array,low,high):
    j=low
    pivot=array[high]
    for i in range(low,high):
        if(array[i]<pivot):
            array[i],array[j]=array[j],array[i]
            j+=1
    array[high],array[j]=array[j],array[high]
    return j #index of the pivot element 

def quickSort(array,low,high):
    if low<high:
        indexOfPivot = partitionArray(array, low, high)
        quickSort(array,low,indexOfPivot-1)
        quickSort(array,indexOfPivot+1,high)

inputSize = int(input("Enter the size of the array: "))
array = []
print(f'Enter {inputSize} elements of array: ')
for i in range(inputSize):
    element = int(input(""))
    array.append(element)
print("User given elements are \n",array)
quickSort(array,0,len(array)-1)
print("Partitioned array elements are \n",array)