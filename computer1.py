def start():

    print("1: dell(20000)  2:toshiva(25000)  3:mac(40000) ")
    select_option = input("enter 1 for dell , enter 2 for toshiva , enter 3 for mac:")
    if select_option == "1":
        dell()
    elif select_option == "2":
        toshiva()
    elif select_option == "3":
        mac()



    else:
        print("invalid")
        start()


def dell():
    x=20000
    quantity = int(input("how many quantiity do you want:"))
    delivary = input("enter \n 1 for home delivary(1000) \n 2 for pickup(free)")
    if delivary=="1":
        x=(x*quantity)+1000
        print(x)
    else:
        y=x
    packing = input("enter \n 1 for plastic bag(500) \n 2 for nice bag(1000) \n 3 for gift_wrap \n 4 for nothing")
    location = input("enter your location:")
    if location == "ktm":
        ktm()
    elif location == "ltp":
        ltp()
    elif location=="bkt":
        bkt()
    else:
        print("invalid location")
        dell()


def toshiva():
    y=25000
    quantity = input("how many quantiity do you want:")
    delivary = input("enter \n 1 for home delivary(1000) \n 2 for pickup(free)")
    packing = input("enter \n 1 for plastic bag(500) \n 2 for nice bag(1000) \n 3 for gift_wrap \n 4 for nothing")
    location = input("enter your location:")
    if location == "ktm":
        ktm()
    elif location == "ltp":
        ltp()
    elif location=="bkt":
        bkt()
    else:
        print("invalid")
        toshiva()


def mac():
    z=40000
    quantity = input("how many quantiity do you want:")
    delivary = input("enter \n 1 for home delivary(1000) \n 2 for pickup(free)")
    packing = input("enter \n 1 for plastic bag(500) \n 2 for nice bag(1000) \n 3 for gift_wrap \n 4 for nothing")
    location = input("enter your location:")
    if location == "ktm":
        ktm()
    elif location == "bkt":
        bkt()
    else:
        print("invalid")
        mac()


def ktm():
    print("hi")


def ltp():
    print("hi")



def bkt():
    print("hi")


start()
