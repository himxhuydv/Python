#  this is the geomitric mean for underoot with n= only 2 
a=24
b=24
gm=(a*b)**(0.5) # we do the 0.5 as the we direclty divide the 1/2 and just the 

# how this works let me tell me u something a*b=48 and then the 
# 48 with the power of 0.5 computer  will convert that


# this is for the geomitirc mean for the n=n 
# ----------what is the formula for the geometric mean =n
name=[1,2,3,4,5,6] # take list as the  a1,a2,a3,a4,a5...an 
product=1
for i in name:  # acessing every element of the name one by one 
    product*=i # multiplying the element one by one
n=len(name)
gm=product**(1/n) #the formula  in code
print(gm)