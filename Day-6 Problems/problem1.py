def count_p_elements(n, array, x, y):
    
    
    # Sort the array
    array.sort()
    
    # Calculate p
    p = array[y] - array[y-1] - 1

    return p

# Example usage:
n = 11
array=[11,22,33,44,55,66,77,88,99,111,121]
x = [11,22,33,44]
y = [55,66,77,88,99,111,121]
result = count_p_elements(n, array, x, y)
print(result)
