def reverse(s):
    s=s.split(",")
    s=s[::-1]
    return " ,".join(s)
    
    
    
s=['abd','kholi','rohit']
ans=reverse(s)
print(ans)