w=[eval(x) for x in input("Enter weights:").split()]
p=[eval(x) for x in input("Enter profits:").split()]
m=int(input("max capacity:"))
n=len(w)
l=[]
tw=0
tp=0
sol=[0]*n
for i in range(n):
    l.append((i,p[i],w[i],p[i]/w[i]))
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
            if left[i][3]>right[j][3]:
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

for j in range(n):
    if l[j][2]<=m-tw:
        tw=tw+l[j][2]
        tp=tp+l[j][1]
        sol[l[j][0]]=1
    else:
        if(m-tw!=0):
            tp=tp+l[j][1]*((m-tw)/l[j][2])
            sol[l[j][0]]=(m-tw)/l[j][2]
            tw=m
print(sol,tp)