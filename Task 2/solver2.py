def solve(arr):
    res=False,""
    for i in range(len(arr)):
        check="".join([arr[j] for j in range(len(arr)) if j!=i])
        res=arr[i]
        for j in arr[i]:
            if j not in check:
                break
        else:
            res=True,arr[i]
    return res
        


file=open("out_task2.txt","w+")
with open("task2.txt") as task:
    T=int(task.readline())
    for cc in range(T):
        arr=task.readline().split()
        res=solve(arr)
        if res[0]:
            file.write(res[1]+"\n")
        else:
            file.write("NO MATCH"+"\n")
        
file.close()
