a=[[1,2],[3,4]]
def merge(a):
    if len(a)>1:
        left=a[:len(a)//2]
        right=a[len(a)//2:]
        merge(left)
        merge(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i][1]>right[j][1]:
                a[k]=left[i]
                i=i+1
                k=k+1
            else:
                a[k]=right[j]
                j=j+1
                k=k+1
        while i<len(left):
            a[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            a[k]=right[j]
            j=j+1
            k=k+1
merge(a)
print(a)