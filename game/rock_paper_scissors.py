
import random
def game():

    while (True):
        print("__________")
        print("1-->rock ")
        print("2-->paper ")
        print("3-->scissors ")
        print("0 to end ")
        c = int(input("enter above choice "))
        random_number = random.randint(1, 3)
        print(random_number)
        if c == random_number:
            print("draw ")
        elif c == 1 and random_number == 2:
            print("computer wins ")
        elif c == 1 and random_number == 3:
            print("player wins ")
        elif c == 2 and random_number == 1:
            print("player wins ")
        elif c == 2 and random_number == 3:
            print("computer wins ")
        elif c == 3 and random_number == 1:
            print("computer wins ")
        elif c == 3 and random_number == 2:
            print("player wins ")
        elif c == 0:
            return
        else:
            print("invalid choice")

    print("this statement will only be executed if break is selected")


if __name__ == '__main__':
    game()