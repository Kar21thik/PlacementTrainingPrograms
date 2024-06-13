from collections import Counter

def missing_numbers(arr, brr):
    # Count the frequency of each number in both arrays
    count_arr = Counter(arr)
    count_brr = Counter(brr)
    
    # List to store missing numbers
    missing = []
    
    # Iterate over the items in count_brr
    for num in count_brr:
        # If the count of num in brr is greater than in arr
        if count_brr[num] > count_arr.get(num, 0):
            # Add the number to the missing list
            missing.append(num)
    
    # Sort the missing numbers list before returning
    missing.sort()
    
    return missing

# Example usage:
arr = [7, 2, 5, 3, 5, 3]
brr = [7, 2, 5, 4, 6, 3, 5, 3]

result = missing_numbers(arr, brr)
print(result)  


