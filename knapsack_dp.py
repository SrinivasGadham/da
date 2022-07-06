
p=[eval(x) for x in input().split()]
wt=[eval(x) for x in input().split()]
m=int(input("Enter max capacity:"))
n=len(p)
k=[[0 for i in range(m+1)]for j in range(n+1)]

sol=[0]*n
for i in range(n+1):
    for w in range(m+1):
        if(i==0 or w==0):
            k[i][w]=0
        elif(wt[i-1]<=w):
            k[i][w]=max(p[i-1]+k[i-1][w-wt[i-1]],k[i-1][w])
        else:
            k[i][w]=k[i-1][w]

print(k[n][w])
i,j=n,m
while(i>0 and j>0):
    if(k[i][j]!=k[i-1][j]):
        sol[i-1]=1
        j=j-wt[i-1]
        i=i-1
    else:
        i=i-1
print(sol)