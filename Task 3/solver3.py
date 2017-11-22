def solve(word):
    Dict={}
    for i in word:
        if i in Dict:
            Dict[i]+=1
        else:
            Dict[i]=1
    mx=0;mx_key=word[0]
    for i in Dict:
        if Dict[i]>mx:
            mx=Dict[i];mx_key=i
    return mx_key
        


file=open("out_task3.txt","w+")
with open("task3.txt") as task:
    T=int(task.readline())
    for cc in range(T):
        word=task.readline().strip()
        file.write(solve(word)+"\n")
file.close()
