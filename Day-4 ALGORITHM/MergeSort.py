"""
19  23  7   2   5   11  3   17  29

19  23  7   2       5   11  3   17  29

19  23      7   2       5   11  3   17  29


19    23      7   2       5   11  3   17  29

19  23      7   2       5      11     3    17   29


merging all the way to one 

mergeSort ( array, low , high)
if low < high:
    mid=(low+high)//2
    mergeSort(array,low,mid)
    mergeSort(array,mid+1,high)
    merge(array,low,mid,high)
merge(array,low,mid,high):


"""

def merged(nums1,nums2):
    nums1+=nums2
    nums1.sort()
    return nums1[len(nums1)//2]

nums1=[1,3]
nums2=[2]
ans=merged(nums1,nums2)
print(f'{ans}.00000')