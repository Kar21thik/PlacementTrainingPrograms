# Draw the pattern the square 
def print_square(n: int):
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()

# Example usage:
n=int(input("Enter the number: "))
print(print_square(n))

        

