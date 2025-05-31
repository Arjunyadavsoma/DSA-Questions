def binarySearch(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        middle=(left+right)//2
        element=array[middle]
        if target==element:
            return middle
            break
        elif target<element:
            right=middle-1
        else:
            left=middle+1
    return -1

array = [1, 3, 5, 7, 9]
target = 0
# Expected output: None
value=binarySearch(array,target)
print(value)