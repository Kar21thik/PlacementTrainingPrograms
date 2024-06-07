# program to find the lucky digit from the user  where the lucky digit is single digit number found after finding  sum of the digit of the given number repeatly untill single digit number is found 

"""Example 
N= 789
lucky digit is 6
7 +8+ 9 = 24  2+4=6
"""

def luckyNumber(a):
        for i in range(0,a):
            sum=0
            for i in range(0,a):
                digit = a % 10
                sum = sum + digit
                a = a // 10
            a = sum
        return a

a= int ( input("Enter the number : "))
print(luckyNumber(a))
