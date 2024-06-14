def read_number():
    while True:
        number = input("Enter a 4-digit number where no digit repeats more than twice: ")
        if len(number) == 4 and number.isdigit() and valid_number(number):
            return number
        else:
            print("Invalid input. Please ensure the number is 4 digits long and no digit repeats more than twice.")

def valid_number(number):
    counts = {str(digit): number.count(str(digit)) for digit in range(10)}
    return all(count <= 2 for count in counts.values())

def process_number(number,count=0):
    while True:
        # Sort digits in decreasing order
        decreasing = ''.join(sorted(number, reverse=True))
        
        # Sort digits in increasing order
        increasing = ''.join(sorted(number))
        
        # Convert to integers
        num_decreasing = int(decreasing)
        num_increasing = int(increasing)
        
        # Calculate the difference
        difference = num_decreasing - num_increasing
        
        print(f"{num_decreasing} - {num_increasing} = {difference}")
        
        # Use the difference as the new number
        number = str(difference).zfill(4)
        
        count+=1
        print(f'No of iterations are ->>{count}')
        
        if number == '6174':
            print("No of total iterations it has done is ->",count)
            break

if __name__ == "__main__":
    number = read_number()
    process_number(number)
