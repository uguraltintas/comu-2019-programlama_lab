def my_vector_inner_product(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    
    for i in range(size):
        my_result[i]=v[i]*w[i]

    t=0
    for i in range(size):
        t=t+my_result[i]

    return t

def topla(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m1[0])):
            result[row].append(m1[row][column]+m2[row][column])
    return result        

def cikar(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m1[0])):
            result[row].append(m1[row][column]-m2[row][column])
    return result      

def  skaler_carp(m1,alpha):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m1[0])):
            result[row].append(m1[row][column]*alpha)
    return result     

def f1(m1,i):
    return m1[i]
def f2(m1,j):
    my_j_th_col=[]
    for row in m1:
        for indis in range(len(row)):
            if(indis==j):
                my_j_th_col.append(row[indis])
    return my_j_th_col

def carp(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m2[0])):
            a=f1(m1,row)
            b=f2(m2,column)
            c=my_vector_inner_product(a,b)
            result[row].append(c)
    return result     

def det2by2(m1):
    s1=m1[0][0]*m1[1][1]
    s2=m1[0][1]*m1[1][0]
    s3=s1-s2
    return s3

def sil(m1,m,n):
    result=[]
    size_1=len((m1))
    size_2=len((m1[0]))
    for i in range(size_1):
        if(i==m):
            continue
        row1=[]
        for j in range(size_2):
            if(j==n):
                continue
            row1.append(m1[i][j])
        result.append(row1)
    return result
            
def  det3by3(m1):
    a1=m1[0][0]
    a2=sil(m1,0,0)
    a3=det2by2(a2)
    a4=a1*a3

    b1=m1[0][1]
    b2=sil(m1,0,1)
    b3=det2by2(b2)
    b4=b1*b3

    c1=m1[0][2]
    c2=sil(m1,0,2)
    c3=det2by2(c2)
    c4=c1*c3

    return a4-b4+c4

def  det4by4(m1):
    a1=m1[0][0]
    a2=sil(m1,0,0)
    a3=det3by3(a2)
    a4=a1*a3

    b1=m1[0][1]
    b2=sil(m1,0,1)
    b3=det3by3(b2)
    b4=b1*b3

    c1=m1[0][2]
    c2=sil(m1,0,2)
    c3=det3by3(c2)
    c4=c1*c3

    d1=m1[0][3]
    d2=sil(m1,0,3)
    d3=det3by3(d2)
    d4=d1*d3

    return a4-b4+c4-d4