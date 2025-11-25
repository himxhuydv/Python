#Lambda Function
double=lambda x:x*2
print(double(5))

#For cube we can easily use this lambda function 
Cube=lambda c:c*c*c #we can easily write that in single line of code.
print(Cube(5))

#for average 
avg=lambda x,y:(x+y)/2
print(avg(3,6))
#another function
new_expression=lambda x,y,z:(x+y+z)/3
print(new_expression(4,2,4))

#Using the argument here 
def function_name(f,values):
    return 6+f(values)
print(function_name(Cube,6))

#using Function in that form and using that again in the function
def fucntion_name(o,y):
    return 6+o(y)
print(fucntion_name(lambda x:x+2,8))

## we can use lambda function for the representation of the argument.
mul=lambda x,y:print(f"{x}*{y}={x*y}") # why only {x*y} in together because python print exact variable{which is passed inside of it} but we if we do some calculatioon of it print the value after doing some calculation.
print(mul(2,5))
