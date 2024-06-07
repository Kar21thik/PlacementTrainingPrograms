"""given the  avg score of the student , print the result as follows   
0 - 49 as fail
50 - 74 as SC 
75 - 90 as FC
91 - 100 as Distinction 
"""

while(1):
    a = int(input("\nEnter the marks\n"))

    if a>=0 and a <50:
            print(f'{a}-> Report Is Fail')
    elif a>= 50 and a< 74:
            print(f'{a}-> Report Is Second Class')
        
    elif a >= 75 and a<90:
            print(f'{a}-> Report Is First Class')
        
    elif a >100 or a <0:
            print("Invalid please enter the number in the range")
            break
    else:
            print("Distinction")
      
    
        
    
