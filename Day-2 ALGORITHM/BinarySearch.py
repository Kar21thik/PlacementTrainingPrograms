"""
MyApproach
You have to use the Array itself (contigious Memory location)
Elements in the data structure to be sorted 
"""

def binary_search(array,element):
    low,high= 0, len(array)-1
    while low<=high:
        mid=(low + high) // 2
        if array[mid]==element:
            return mid
        elif array[mid]<element:
            low= mid+1
        else:
            high= mid-1
    return -1        
array= list(map(int, input("Enter the array elements ").split(",")))
key=int(input("Enter the key element"))
ans=binary_search(array,key)
print(ans)

if ans==-1:
    print(f'{key}element not found')
else:
    print(f'{key} element found at the position of {ans+1}')









"""


def binary_search(array, element):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr=list(map(int,input("Enter the elements").split(",")))
target=int(input("Enter the target"))
print(binary_search(arr, target))
ans=binary_search(arr, target)
if ans == -1:
    print("Target not found")
else:
    print("Target found") 
"""