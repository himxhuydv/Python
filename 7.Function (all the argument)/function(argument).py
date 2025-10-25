
# FUNCTION argument in code : are mainly 4 types 
#------------ to understand the technicality we take the example of addition of number
#---------------------------------------------------------------------
# 1.Default argument :
def Additiondefault(a=10,b=12,c=20): # default giving a=10,b=12,c=20
    add=a+b+c
    print("this is the output of default argument:",add)
Additiondefault()
# now in this no argument is passed it will take the defaullt argument passed in the function
#-------------------------------------------------------------------
# 2.Required argument :
#-----important point ------
# there is a rule in python syntax that the non default values parameter should be first and then the rest default values so now the code will works as the c(non defult) b=10(default) c=20(default)   something like:(c,b=10,c=20)
def additionrequired(c,a=20,b=10):
    add=a+b+c
    print("this is the output of required argument:",add)
additionrequired(3) # u can directly give that because the a and b there default parameter 
additionrequired(c=2) #output will be the 32
#-------------------------------------------------------------------
# 3.Keyword argument :
def additionkeyword(a,b,c):
    add=a+b+c
    print("this is output of keyword argument:",add)
additionkeyword(b=5,c=3,a=4) 
#4.Variable length argument :
def additionthroughvariablelength(*number): #use always the * for the tuple and list and ** for the dict on the time of giving parameter
    product=0
    for i in number:
        product+=i
    print("this is ouput of variable length :",product)
name=(1,2,3,4,5)
additionthroughvariablelength(*name) # also used that on the time of  giving it and *(usedfortuple)has to same as the parameter or type error can happened if u give **(used for the dict)these in the argument then, the error will be dict 
#--------------------------------------------------------------------
#important return in functionn 
# lets take the same example 
def additionthroughvariablelength(*number):
    product=0
    for i in number:
        product+=i
    return print("this is ouput of variable length :",product)#so return used to store the executed process in the variable
name=(1,2,3,4,5)
additionis=additionthroughvariablelength(*name) 