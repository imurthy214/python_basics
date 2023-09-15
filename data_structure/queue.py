def myqueue():
    q=list()
    max_queue_size=5
    while True:
        print("0 for add")
        print("1 for remove")
        print("2 for display")
        print("3 for quit")
        choice=int(input("please enter a choice from above"))
        if choice==0:
            element=int(input("enter an integer to add to stack"))
            if len(q)==max_queue_size:
                print("error: max queue size reached")
            else:
                q.append(element)
        elif choice==1:
            if len(q)==0:
                print("error: min queue size reached")
            else:
                removed_element=q.pop(0)
                print(f"removed element {removed_element}")
        elif choice==2:
            print(q)
        else:
            return

if __name__ == '__main__':
    myqueue()