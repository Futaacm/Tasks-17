from random import random

with open("task1.txt","w+") as task:
    task.write("100\n")
    for cc in range(100):
        N=int(random()*1000)
        K=int(random()*1000)
        while K>=N:
            K=int(random()*1000)
        task.write(str(N)+" "+str(K)+"\n")
        List=[int(random()*100) for i in range(N)]
        LIST=""
        for i in range(N):
            LIST+=str(List[i])+" "
        task.write(str(LIST)+"\n")
        
        
