"""read the size of matrix 
read the elements of the matrix display matrix 
spiral matrix 
"""
def CompressedString(s):
    n=len(s)
    i=0
    while i < n-1:
        count=1
        while (i < n -1 and s[i] == s[i+1]):
            count+=1
            i+=1
        i+=1
        print(s[i-1],count,end=" ")


def decompress_rle(s: str) -> str:
    decompressed = []
    count = ""
    
    for char in s:
        if char.isdigit():
            count += char
        else:
            if count:
                decompressed.append(prev_char * int(count))
                count = ""
            prev_char = char
    
    if count:
        decompressed.append(prev_char * int(count))
    
    return ''.join(decompressed)

while(1):
    choose=int(input("Enter the choice\n1. Compress\n2. Decompress\n"))
    if choose==1:
        s=input("Enter the string\n")
        print(CompressedString(s))
    elif choose==2:
        s=input("Enter the string\n")
        print(decompress_rle(s))
    else:
        print("Invalid choice")


