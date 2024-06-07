#program to count number of odd digit in a number 
# count the number of composite digits in a number (other than prime numbers are composite number )
# // integer division
# / floating point division


def TocheckOdd(a):
    try: 
        count=0

        for i in range(0,a):
            var=a%10
            a=a//10
            if var%2==1:
                count+=1
            else:
                pass
        return count
    except ValueError:
        print("Enter the Integer Number")

a=int(input("Enter the Number"))
print(TocheckOdd(a))