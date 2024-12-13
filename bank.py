def validate(pin_no):
    if(pin_no==1234):
       view()
       choice=int(input("enter option"))
       #if(choice==1):
          # deposit()
       #elif(choice==2):
           #withdraw()
    else:
        print("enter valid pin")
def view():
    print("1.deposit\n 2.withdrew \n 3.bal enqueriy \n 4.exit")
print("welcome to raj bank")
pin_no=int(input("enter atm pin"))
validate(pin_no)
