process=[eval(x) for x in input("Enter the id:").split()]
pro=[eval(x) for x in input("Enter the profits:").split()]
dl=[eval(x) for x in input("Enter the deadlines:").split()]
n=len(pro)
job=[]
tp=0
for i in range(n):
    job.append([process[i],pro[i],dl[i]])
job.sort(key=lambda x:x[1],reverse=True)

m=max(dl)
l=[0]*m
for i in job:
    ind=i[2]
    while(ind!=0):
        if(l[ind-1]==0):
            l[ind-1]=i[0]
            tp=tp+i[1]
            break
        else:
            ind-=1
print(l)
print(tp)