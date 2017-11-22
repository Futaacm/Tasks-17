from random import random
alphabets="abcdefghijklmnopqrstuvwxyz"

with open("task2.txt","w+") as task:
    task.write("100\n")
    for cc in range(100):
        N=int(random()*50)
        List=[]
        for i in range(N):
            k=(int(random()*10)%10)+4
            List.append("".join([alphabets[int(random()*26)%26] for i in range(k)]))
        List=" ".join(List)
        task.write(str(List)+"\n")
        
        
