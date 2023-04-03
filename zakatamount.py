item=input("what do you have?gold\silver\cash:")
time=input("you have this amount for one year? Yes or No:")

def gold():
    amount=float(input("how much gold do you have?"))
    if amount>=7.5 and time=="Yes":                                                        #a=amnt b= time Q=item
        c=amount*196400*0.025
        print("you have to pay",c)
    else:
            print("you are not eligible for paying zakat")
def silver():
    amount1=float(input("how much silver do you have?"))
    if amount1>=52.5 and time=="Yes":
        m=amount1*2082*0.025
        print("you have to pay",m)
    else:
           print("you are not eligible for paying zakat")a
def cash():
    amount2=float(input("how much cash do you have"))
    if amount2>=109305 and time=="Yes":
        g=amount2*0.025
        print("you have to pay",g)
    else:
        print("you are not eligible for paying zakat")
    
if item=="gold":
    gold()
elif item=="silver":
    silver()
elif item=="cash":
    cash()
else:
    print("invalid input")
             
              
                  
