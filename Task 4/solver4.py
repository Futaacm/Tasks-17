from math import factorial as fac
def solve(word):
    
    return fac(len(word))
        
file=open("out_task4.txt","w+")
with open("task4.txt") as task:
    T=int(task.readline())
    for cc in range(T):
        word=task.readline().strip()
        res=str(solve(word))+"\n"
        file.write(res)
        
        
file.close()
