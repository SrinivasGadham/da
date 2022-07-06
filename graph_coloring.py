n = int(input("no of subjects: "))
sub = []
for i in range(n):
    print("Enter subject_code and subject_name for ",i+1)
    l = list(map(str, input().split()))
    sub.append(l)
print(sub)

x = [0 for x in range(n)]
G = [[0 for i in range(n)] for i in range(n)]
# print(G)
for i in range(n):
    print("Enter clashes for subject ",i+1)
    l = list(map(int, input().split()))

    for j in l:
        G[i][j - 1] = 1
print(G)


def TimeScheduling(k, i):
    while (i == True):
        NextValue(k)
        if (x[k] == 0):
            return
        if (k == n - 1):
            # print(*sub)
            print("Time line schedule seqquence is : ", *x)
            # solution = True
            exit(0)
            # i = False
        else:
            TimeScheduling(k + 1, i)


def NextValue(k):
    while (True):
        x[k] = (x[k] + 1) % (m + 1)
        if (x[k] == 0):
            return
        for j in range(n):
            if (G[k][j] != 0 and x[k] == x[j]):
                break
        if (j == n - 1):
            return


for m in range(1, n + 1):
    TimeScheduling(0, True)
# TimeScheduling(0,True)