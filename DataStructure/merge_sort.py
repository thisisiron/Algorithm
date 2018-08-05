x_list = [27,10,12,20,25,13,15,22]
sorted_list = [0 for _ in range(len(x_list))]

def mergeSort(p_list, left, right):
    
    if left < right:
        mid = int((left+right)/2)
        print("left",left,' mid',mid," right",right)
        mergeSort(p_list, left, mid)
        mergeSort(p_list, mid+1, right)
        merge(p_list, left, mid, right)

def merge(p_list, left, mid, right):

    i = left
    j = mid+1
    k = left

    while i <= mid and j<=right:
        if p_list[i] < p_list[j]:
            sorted_list[k] = p_list[i]
            i+=1
            k+=1
        else:
            sorted_list[k] = p_list[j]
            j+=1
            k+=1
    
    if i>mid:
        while j<=right:
            sorted_list[k] = p_list[j]
            j+=1
            k+=1
    else:
        while i<=mid:
            sorted_list[k] = p_list[i]
            i+=1
            k+=1

    l = left
    while l<=right:
        p_list[l] = sorted_list[l]
        l+=1
    print('plist', p_list)

mergeSort(x_list, 0, len(x_list)-1)