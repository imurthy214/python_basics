def list_sum(lst):
    sum=0
    for e in lst:
        sum=sum+e
    print(sum)

def list_sum_v2(lst):
    sum=0
    for i in range(0,len(lst),1):
        sum=sum+lst[i]
        print(f"{i}:{lst[i]}")
    print(sum)

def list_sum_v3(lst):
    sum=0
    for i in range(0, len(lst), 2):
        sum = sum + lst[i]
        print(f"{i}:{lst[i]}")
    print(f"even index sum {sum}")

def list_sum_v4(lst):
    sum=0
    for i in range(1, len(lst), 2):
        sum = sum + lst[i]
        print(f"{i}:{lst[i]}")
    print(f"odd index sum {sum}")

def sum_two_list(l1,l2):
    l3=[]
    for i in range(0,len(l1),1):
        l3.append(l1[i]+l2[i])
    print(l3)

def sum_2_list_v2(l1,l2):
    l3=[]
    for i in range(0, len(l1),2):
        l3.append(l1[i]+l2[i])
    print(l3)
    l4=[]
    for i in range(1, len(l1), 2):
        l4.append(l1[i]+l2[i])
        l3.append(l1[i]+l2[i])
    print(l4)
    print(l3)



if __name__ == '__main__':
    #a = 10
    #print(type(a))
    #a = "ishan"
    #print(type(a))
    #a = True
    #print(type(a))
    input=[100,200,300,400,500]
    input2=[10,20,30,40,50]
    #list_sum(input)
    #list_sum_v2(input)
    #list_sum_v3(input)
    #list_sum_v4(input)
    sum_two_list(input,input2)
    sum_2_list_v2(input,input2)