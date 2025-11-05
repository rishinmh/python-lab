def add_nums(*n):"""sum of numbers"""; return sum(n)
print(add_nums(*map(int, input("enter number: ").split())))
