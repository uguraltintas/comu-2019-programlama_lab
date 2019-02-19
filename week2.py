
def mySearchSelection(my_array):
    for i in range(len(my_array)-1,0,-1):
        maxIndex=0
        for j in range (1,i+1):
            if(my_array[j]>my_array[maxIndex]):
                maxIndex=j
        temp=my_array[j]
        my_array[j]=my_array[maxIndex]
        my_array[maxIndex]=temp
    return

def binarySearch(sortedarray,item):
    first=0
    last=len(sortedarray)-1
    found=False
    s=0
    while first<=last and not found:
        midpoint=(first+last)//2
        print("first - last",first,last)
        if(sortedarray[midpoint]==item):
            found=True
        else:
            if(item<sortedarray[midpoint]):
                last=midpoint-1
            else:
                first=midpoint+1
                s=s+1
    return found,midpoint,s

my_arr=[11,27,7,98,55,9,8,31,69,77,34]


def fibo_rec(n):
    if(n<2):
        return n
    else:
        return fibo_rec(n-2)+fibo_rec(n-1)

def fibo(n):
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return a


def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s     




def fact_rec(n):
    if(n==1):
        return n
    else:
        return n*fact_rec(n-1)




def power(m,n):
    if(n==0):
        return 1
    elif(n==1):
        return m
    else:
        for i in range(1,n):
            m*=m
    return m
print(power(10,2))
    




def power_rec(m,n):
    if(n==0):
        return 1

    else:
        return m * power_rec(m,n-1)
