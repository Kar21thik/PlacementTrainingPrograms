"""Selection Sort"""
def SelectionSort(lst):
    for i in range(len(lst)):
        min=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[min]:
                min=j
        lst[i],lst[min]=lst[min],lst[i]
        
lst=list(map(int,input("Enter the elements").split(",")))
SelectionSort(lst)
print(lst)