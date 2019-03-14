def carpan(a):
    carpanlar=[]
    asal=[]
    asalmı=False
    for i in range(2,int(a/2),1):
        for j in range(2,i,1):
            if(i%j!=0):
                asalmı=True
            else:
                asalmı=False
                break
        if(asalmı==True):
            asal.append(i)    
    while(a%2==0):
        a/=2
        carpanlar.append(2)
    for k in range(len(asal)):
       while(a%asal[k]==0):
           a/=asal[k]
           carpanlar.append(asal[k])
    return carpanlar


def toplama(a):
    sonuc=[]
    toplam=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for k in range(i,j+1):
                toplam+=a[k]
            sonuc.append(toplam)
            toplam=0

    buyuk=0
    for l in range(len(sonuc)):
        if(sonuc[l]>buyuk):
            buyuk=sonuc[l]
    return buyuk

liste=[4,-3,2,-1,-2,6,-5]
print(toplama(liste))