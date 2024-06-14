from collections import Counter

def missing_numbers(arr, brr):
    
    count_arr = Counter(arr)
    count_brr = Counter(brr)
    
    
    missing = []
    
    
    for num in count_arr:
        
        if count_arr[num] > count_brr.get(num, 0):
            
            missing.append(num)
    
    
    missing.sort()
    
    return missing

arr = list(map(int,input("Enter the elements of first array").split(",")))
brr = list(map(int,input("Enter the elements of second array").split(",")))

result = missing_numbers(arr, brr)
print(result)  


