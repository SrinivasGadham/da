l=[[1,2,3,4],[5,2,9,8]]
def merge(l):
    if len(l)>1:
        left=l[:len(l)//2]
        right=l[len(l)//2:]
        merge(left)
        merge(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i][0]>right[j][0]:
                l[k]=left[i]
                i=i+1
                k=k+1
            else:
                l[k]=right[j]
                j=j+1
                k=k+1
        while i<len(left):
            l[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            l[k]=right[i]
            j=j+1
            k=k+1
merge(l)

