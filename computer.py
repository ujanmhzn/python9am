print("1: dell(20000)  2:toshiva(25000)  3:mac(40000) ")
select_option=int(input("enter 1 for dell , enter 2 for toshiva , enter 3 for mac:"))
del_price=0
toshiva_price=0
mac_price=0
delivary_price=0
plastic_price=0
bag_price=0
gift_price=0
location_price=0
tax_amt=0
qt=0



if select_option==1:
    qt=int(input("enter quantity"))
    del_price+=20000*qt
elif select_option==2:
    qt = int(input("enter quantity"))
    del_price += 25000*qt
elif select_option==3:

    qt = int(input("enter quantity"))
    del_price += 40000*qt


else:
    exit()


del_option=int(input("enter \n 1 for home delivary(1000) \n 2 for pickup(free"))
if del_option==1:
    delivary_price+=1000


print("1 for plastic bag(500) \n 2 for nice bag(1000) \n 3 for gift_wrap(5000) \n 4 for nothing")
p_option=int(input("enter your choice"))
if p_option==1:
    plastic_price+=500
elif p_option==2:
    plastic_price+=1000
elif p_option==3:
    plastic_price+=5000
else:
    exit()

print("location \n 1 Ktm(13%) \n 2 ltp(free) \n 3 bkt(free)")
l_option=int(input("enter your location"))
total_price=del_price+toshiva_price+mac_price
if l_option==1:
    tax_amt+=total_price*0.13
gt=total_price+tax_amt+del_price+plastic_price+bag_price+gift_price
print(f"QT {qt} total:{total_price} tax {tax_amt} gt {gt}")




