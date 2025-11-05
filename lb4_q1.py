def Simple_interest(p,t,Senior_input):
    rate = 12 if Senior_input else 10
    interest = (p*t*rate)/100
    return interest
p = float(input("enter principal amount: "))
t = float(input("enter time(in years): "))
Senior_input = input("is the customer a senior citizen(yes/no)?").lower() == "yes"
Si=Simple_interest(p,t,Senior_input)
print("simple interst= ",Si)
