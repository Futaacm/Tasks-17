from random import random
alphabets="abcdefghijklmnopqrstuvwxyz"

with open("task4.txt","w+") as task:
    task.write("100\n")
    for cc in range(100):
            k=(int(random()*10)%10)+4
            task.write("".join([alphabets[int(random()*26)%26] for i in range(k)])+"\n")
        
