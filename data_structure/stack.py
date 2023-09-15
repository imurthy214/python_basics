def mystack():
    s=list()
    max_stack_size=5
    while True:
        print("0 for add")
        print("1 for remove")
        print("2 for display")
        print("3 for quit")
        choice=int(input("please enter a choice from above"))
        if choice==0:
            element=int(input("enter an integer to add to stack"))
            if len(s)==max_stack_size:
                print("error: max stack size reached")
            else:
                s.append(element)
        elif choice==1:
            if len(s)==0:
                print("error: min stack size reached")
            else:
                removed_element=s.pop()
                print(f"removed element {removed_element}")
        elif choice==2:
            print(s)
        else:
            return

if __name__ == '__main__':
    mystack()