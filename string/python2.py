def sum(a,b):
    val=a+b
    print(f"sum of {a} and {b} equals {val}")

def sub(a,b):
    val=a-b
    print(f"difference of {a} and {b} equals {val}")

def mult(a,b):
    val=a*b
    print(f"product of {a} and {b} equals {val}")

def div(a,b):
    if b==0:
        print(f"invalid {b}")
        return
    val=a/b
    print(f"quotient of {a} and {b} equals {val}")

if __name__ == '__main__':
    #sum(2,3)
    #sub(2,3)
    #mult(2,3)
    #div(2,0)
    #sum("2","3")
    #a=int(input("enter a value for a "))
    #b=int(input("enter a value for b "))
    #sum(a,b)
    while(True):
        a=int(input("enter a value for a "))
        b=int(input("enter a value for b "))
        print("1-->addition ")
        print("2-->subtraction ")
        print("3-->multiplication ")
        print("4-->division ")
        print("0 to end")
        c=int(input("enter above choice "))

        if c==1:
            sum(a,b)
        elif c==2:
            sub(a,b)
        elif c==3:
            mult(a,b)
        elif c==4:
            div(a,b)
        elif c==0:
            print("STOP")
            break
        else:
            print("invalid choice ")