# to draw the equvilateral traingle 
a= int ( input("Enter the number"))

for i in range(0,a):
    for j in range(0,a-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*", end=" ")
    print()

    
    
    