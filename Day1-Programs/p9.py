def Hollow_Sqaure(n: int):
    for i in range(1,n+1):
        if i==1 or i==n:
            for j in range(n):
                print("*",end=" ")
        else:
            print("*",end=" ")
            for j in range(1,n-1):
                print(" ",end=" ")
            print("*",end=" ")
        print()

# Example usage:
n=int(input("Enter the number: "))
print(Hollow_Sqaure(n))