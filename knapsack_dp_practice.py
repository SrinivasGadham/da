p=list(map(int,input("Enter the profits").split()))
wt=list(map(int,input("Enter the weights").split()))
n=len(p)
m=int(input("enter the max capacity"))
sol=[0]*n
k=[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n+1):
    for w in range(m+1):
        if i==0 or w==0:
            k[i][w]=0
        elif wt[i-1]<=w:
            k[i][w]=max(k[i-1][w],p[i-1]+k[i-1][w-wt[i-1]])
        else:
            k[i][w]=k[i-1][w]
print(k[n][w])
i,j=n,m
while i>0 and j>0:
    if k[i-1][j]!=k[i][j]:
        sol[i-1]=1
        j=j-wt[i-1]
        i=i-1
    else:
        i=i-1
print(sol)