# implementation of merge sort

def merge(a1,a2):
    if len(a1) == 0: return a2 
    if len(a2) == 0: return a1

    res = []
    i = j = 0
    while i < len(a1) and j < len(a2):
        val1,val2 = a1[i], a2[j]

        if val1 < val2:
            res.append(val1)
            i+=1
        else:
            res.append(val2)
            j+=1
    
    while i < len(a1):
        res.append(a1[i])
        i +=1
    while j < len(a2):
        res.append(a2[j])
        j +=1
    
    return res 

def merge_sort(arr):
    # base case
    if len(arr) == 1:
        return arr 
    mid = len(arr) // 2
    left_merge = merge_sort(arr[:mid])
    right_merge = merge_sort(arr[mid:])

    return merge(left_merge,right_merge)

arr = [38, 27, 43, 3, 9, 82, 10]

print(merge_sort(arr))

