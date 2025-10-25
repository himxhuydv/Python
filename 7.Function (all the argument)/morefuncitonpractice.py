#is greater then function         ( with is argument) 
def isgreater(a,b):
    if a>b:
        print(" a is greater then b")
    elif(a==b):
        print("a equal to b")
    else:
        print("b is greater then a")
number1=23
number2=45
isgreater(number1,number2)
# u can directly give the argument 
isgreater(45,34)

#                                (wihtout argument)
c=100
def islessthan(a):
    if a<c:
        print("a is lessthan c")
    elif(a==c):
        print("equal")
    else:
        print("c is greater")
islessthan(40)


