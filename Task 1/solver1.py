def solve(arr,n,k):
    assert k<n,"k must be less than n"
    arr.sort()
    a=str(arr[k-1])
    return a+" "+str(arr[~k])+"\n"


file=open("out_task1.txt","w+")
with open("task1.txt") as task:
    T=int(task.readline())
    for cc in range(T):
        n,k=[int(i) for i in map(int,task.readline().split())]
        arr=[int(i) for i in map(int,task.readline().split())]
        file.write(solve(arr,n,k))
        
    

file.close()
