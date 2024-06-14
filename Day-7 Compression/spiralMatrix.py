"""n= int(input("Enter the size of matrix"))
a=[["0" for i in range(n)]for i in range(n)]
count=1
for i in range(n):
    for j in range(n):
        a[i][j]=str(count)
        count+=1
        print(a[i][j],end=" ")
    print("")"""
n=int(input("Enter the size of matrix"))
matrix = [[0 for _ in range(n)] for _ in range(n)]
count=1
for i in range(n):
    for j in range(n):
        matrix[i][j]=count
        count+=1
lst=[]
columns = [[row[j] for row in matrix] for j in range(n)]


for i in matrix:
    for j in i:
        print(j,end=" ")
    print("")
# Step 5: Print the column elements
for idx, col in enumerate(columns):
    print(f"elements: {col}")