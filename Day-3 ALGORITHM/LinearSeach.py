""" My Approach"""

def linear_search(arr, target):
   
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

arr=list(map(int,input("Enter the elements").split(",")))
target=int(input("Enter the target"))
print(linear_search(arr, target))
if linear_search(arr, target) == -1:
    print("Target not found")
else:
    print("Target found") 






