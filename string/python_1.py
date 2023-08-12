def fun1():
    name = "ishan"
    print(name)
    name = "murthy"
    print(name)


def fun2():
    name = "ishan murthy"
    fname_lname = name.split()
    print("my first name is : " + fname_lname[0])
    print("my last name is : " + fname_lname[1])


def fun3():
    details = "ishan murthy 11th CupertinoHighSchool"
    mydetails = details.split()
    print("my first name is " + mydetails[0])
    print("my last name is " + mydetails[1])
    print("I am in " + mydetails[2] + " grade")
    print("I am in " + mydetails[3])


def fun4():
    details = "ishan murthy 11th CupertinoHighSchool"
    mydetails = details.split()
    print(f"my first name is {mydetails[0]}")
    print(f"my last name is {mydetails[1]}")
    print(f"I am in {mydetails[2]} grade")
    print(f"I am in {mydetails[3]}")


def fun5():
    a = "100 20 30 40 50"
    a_vals = a.split()
    print(a_vals)
    print(type(a_vals))
    for s in a_vals:
        print(s)
        print(type(s))
    print("-------------")
    for i in range(0,len(a_vals)):
        print(a_vals[i])
        print(type(a_vals[i]))

def fun6():
    a = "100 20 30 40 50"
    a_vals = a.split()
    sum_no_conversion=a_vals[0]+a_vals[1]+a_vals[2]+a_vals[3]+a_vals[4]
    print(f"sum is equal to {sum_no_conversion}")
    sum_conversion=int(a_vals[0])+int(a_vals[1])+int(a_vals[2])+int(a_vals[3])+int(a_vals[4])
    print(f"sum is equal to {sum_conversion}")

def fun7():
    a = "100 20 30 40 50"
    a_vals = a.split()
    res=""
    for s in a_vals:
        res=res+s
        print(f"inside :sum is equal to {res}")

    print(f"final result :sum is equal to {res}")
    print("convert string to integer")
    res=0
    for s in a_vals:
        res=res+int(s)
        print(f"after converting string to integer {res}")
    print(f"final result after conversion {res}")

if __name__ == '__main__':
    # fun2()
    # fun1()
    # fun3()
    # fun4()
    fun7()
