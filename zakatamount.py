q=input("what do you have?gold\silver\cash:")
b=input("you have this amount for one year? Yes or No:")

def gold():
    a=float(input("how much gold do you have?"))
    if a>=7.5 and b=="Yes":
        c=a*196400*0.025
        print("you have to pay",c)
    else:
            print("you are not eligible for paying zakat")
def silver():
    s=float(input("how much silver do you have?"))
    if s>=52.5and b=="Yes":
        m=s*2082*0.025
        print("you have to pay",m)
    else:
           print("you are not eligible for paying zakat")
def cash():
    d=float(input("how much cash do you have"))
    if d>=109305 and b=="Yes":
        g=d*0.025
        print("you have to pay",g)
    else:
        print("you are not eligible for paying zakat")
    
if q=="gold":
    gold()
elif q=="silver":
    silver()
elif q=="cash":
    cash()
else:
    print("invalid input")
             
              
                  
