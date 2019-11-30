#task3

age=int(input("enter your age="))
if age<3 :
    ticket=0;
    print("$"+ str(ticket))
elif age>=3 and age<=12 :
    ticket=10;
    print("$"+ str(ticket))
elif age>12 :
    ticket=15;
    print("$"+ str(ticket))
    