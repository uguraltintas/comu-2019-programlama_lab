
# coding: utf-8

# In[15]:

def fibo_rec(n):
    if(n<2):
        return n
    else:
        return fibo_rec(n-2)+fibo_rec(n-1)


# In[ ]:

def fibo(n):
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return a


# In[17]:

def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s     


# In[35]:

def fact_rec(n):
    if(n==1):
        return n
    else:
        return n*fact_rec(n-1)


# In[40]:

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
    


# In[41]:

def power_rec(m,n):
    if(n==0):
        return 1

    else:
        return m * power_rec(m,n-1)
power_rec(10,2)


# In[ ]:



