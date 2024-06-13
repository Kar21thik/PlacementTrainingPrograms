"""b=[2,5,7]
g=[1,3,4]
i=len(b)-1
j=len(g)-1
k=0"""
def merge(nums1, nums2):
    k = (len(nums1)+len(nums2))-1
    i, j = len(nums1)-1, len(nums2)- 1
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Driver code to test the merge function
if __name__ == "__main__":
    nums1 = [2, 5, 7]

    nums2 = [1, 3, 4]


    merge(nums1, nums2)

    print("Merged array:", nums1)
