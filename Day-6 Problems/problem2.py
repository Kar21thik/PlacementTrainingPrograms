from collections import Counter

def missing_numbers(arr, brr):
    # Count the frequency of each number in both arrays
    count_arr = Counter(arr)
    count_brr = Counter(brr)
    
    # List to store missing numbers
    missing = []
    
    # Iterate over the items in count_brr
    for num in count_arr:
        # If the count of num in brr is greater than in arr
        if count_arr[num] > count_brr.get(num, 0):
            # Add the number to the missing list
            missing.append(num)
    
    # Sort the missing numbers list before returning
    missing.sort()
    
    return missing

# Example usage:
arr = list(map(int,input("Enter the elements of first array").split(",")))
brr = list(map(int,input("Enter the elements of second array").split(",")))

result = missing_numbers(arr, brr)
print(result)  


