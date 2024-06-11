def Binary_Search(list):
    min=list[0]
    for i in list:
        for j in list:
            if list[i]<=list[j]:
                list[i]=list[j]
    print(list) 

list=[23,44 , 12,  9,   3,   31,  23,    17,  29]
Binary_Search(list)
        