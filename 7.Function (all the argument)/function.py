#  --------------------basically a simple way to explain u that how does the function will act ------
#    Starting with the geometric mean normal how we will execute 
a=24
b=24
gm=(a*b)**0.5 # logic 
print(gm)
#           logic explanation 
# WHEN THERE IS THE a*b will go through the then it will do the expotiential power of 1/2 and solve it 
#                                        what actually does in our code 
# a*b=576 
#                                      now thinks as the **(1/2) expoentinal power how would u solve
#                                     #  a number having a^(1/2) can be solve as just giveing the x^(1/2)=√x
# the 24*24=576 
# 576 ** 0.5 = √576


#      instead of the 0.5 u can write the **(1/2) make more easiy to understand  but look for another time using the logic we have to right whole code
c=24
d=24
gm=(c*d)**(1/2)# logic 
print(gm)
# that why we use the function  
#              function with argument given like only find 2 variable ------what about n number of argument or n number of element 



#                          ----   Now with function    ----


def gm(a,b): #always right argument in parenthesis and the after passing argument alays pass : and then indentation 
    gm=(a*b)**(1/2)
    print(gm)
e=43
f=34
gm(e,f)

#----------------------- what about n number of argument or n number of element---------------- 
#     u can understand in this term of formula 
# gm
# n=total element =a1,a2,a3,a4,a5
#gm=n√a1.a2.a3.a4.a5
#n=5 because a5 tak hai then 
#gm=5√a1.a2.a3.a4.a5
