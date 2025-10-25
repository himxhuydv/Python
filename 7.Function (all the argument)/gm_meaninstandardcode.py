#  this is the geomitric mean for underoot with n= only 2 
a=24
b=24
gm=(a*b)**(0.5) # we do the 0.5 as the we direclty divide the 1/2 and just the 

# how this works let me tell me u something a*b=48 and then the 
# 48 with the power of 0.5 computer  will convert that


# this is for the geomitirc mean for the n=n 
name=[1,2,3,4,5,6]
product=1
for i in name:
    product*=i
n=len(name)
gm=product**(1/n)
print(gm)