my_list=[1,5,6,3,1,2,3,7,8,9]
def frekans(list):
    list1={}
    for i in range(len(list)):
        c=0
        for j in range(len(list)):
            if i==list[j]:
                c+=1
        if c!=0:
            list1[i]= c
    return list1
    
    
print(frekans(my_list))