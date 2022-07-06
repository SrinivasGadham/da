def place(row,col):
    for i in range(row):
        if(x[i]==col or abs(i-row)==abs(x[i]-col)):
            return False
    return True





def nqueens(row,n):
    for i in range(n):
        if place(row,i):
            x[row]=i
            if row==n-1:
                print(x)
                break
            else:
                nqueens(row+1,n)



n=int(input("Enter the no.of queens"))
x=[-1]*n
nqueens(0,n)