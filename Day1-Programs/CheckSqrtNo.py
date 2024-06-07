# Program to check if the number is a Perfect Square. The number is positive and Discrete

# inputNum= float(input("Enter the number"))
# root = inputNum ** 0.5
# root = float( root)

# if root * root == inputNum:   
#     print(f'{inputNum} is a Perfect square')
# else:
#     print("Not a perfect sqaure",inputNum)

import math
a= int(input("Enter the number"))     
sqrtno=math.sqrt(a)
sqrtno= sqrtno*sqrtno
print(sqrtno)
if a==sqrtno:
    print(f'{a} is a sqaure number')
else:
    print(f'{a} is not a sqaure number')

    