def sum(l1,l2):
    l3=[]
    l1.reverse()
    l2.reverse()
    carry=0
    sum=0
    for i in range(0,len(l1),1):
        sum=l1[i]+l2[i]+carry
        print(sum)
        if sum <= 9:
            l3.append(sum)
            carry=0
        else:
            l3.append(int(sum%10))
            carry=int(sum/10)
            print(carry)
    if carry!=0:
        l3.append(carry)
    l3.reverse()
    print(l3)
if __name__ == '__main__':
    l1=[9,8,7]
    l2=[5,4,9]
    sum(l1,l2)