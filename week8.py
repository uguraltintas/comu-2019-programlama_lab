import random
def hasholustur(N): 
    tablo=[]
    for i in range(N):
        tablo.append(0)
    return tablo

def hashim(size,sayi):
    return sayi%size
    
def hashekle(tablo,sayi):
    çarpışma=False
    index=hashim(len(tablo),sayi)
    if(tablo[index]==1):
        çarpışma=True
    else:
        tablo[index]=1
    return çarpışma

def test(tablo,sayi):
    tekrarcount=0
    hash1=hasholustur(tablo)
    for s in range(sayi):
        r1=random.randint(0,1000)
        if(hashekle(hash1,r1)==True):
            tekrarcount+=1
    print(hash1)
    return tekrarcount