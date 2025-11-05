def check(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
n = int(input("enter a number: "))
print("the number is ", check(n))
