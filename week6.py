class item(object):
    def __init__(self,n,v,w,v_w):
        self.name=n
        self.value=v
        self.weight=w
        self.v_w=v_w
def get_items():
    items=[]
    items.append(item("clock",175,10,17.5)) 
    items.append(item("painting",90,9,10))
    items.append(item("radio",20,4,5))
    items.append(item("vase",50,2,25))
    items.append(item("book",10,1,10))
    items.append(item("computer",200,20,10))

    return items
def print_items(items):
    for item in items:
        print(item.name,item.value)
def test():
    items=get_items()
    print_items(items)
    print("------sorted items------")
    print(sort_items(items))
def sort_items(items):
    return sorted(items,key=lambda item:item.name,reverse=True)
def get_list_for_burglar(items,maxW):
        result=[]
        totalV,totalW=0,0
        for i in range(len(items)):
                if(totalW+items[i].weight<=maxW):
                        result.append(items[i])
                        totalW+=items[i].weight
                        totalV+=items[i].value
        return (result,totalV)
def print_result(item2):
        for item1 in item2[0]:
                print(item1.name)
        print(item2[1])