

def Twosum(a,target):
    i,j=0,0
    for i in a:
        for j in a:
            a[j]==target-a[i]
    return [i,j]

a= list(map(int,input("").split(",")))
target=int(input("Enter the target number"))
Twosum(a,target)