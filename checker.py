file_a=open("","r+")
file_b=open("","r+")
N=100
def main():
    for i in range(100):
        if file_a.readline()!=file_b.readline():
            return False
    return True


file_a.close()
file_b.close()
