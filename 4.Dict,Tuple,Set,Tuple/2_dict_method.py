#  method of dictonries 
#   empty dict
# d={}

#  dict
marks={"harrry":200,
       "shubham":50,
       "ragav":20}

#  item method 
#             use for printing the whole key and values together in tuple form each key and values written in seprate tuples
# print(marks.items())

# values method 
#              use for getting the values from the dictnoreis rather than keys 
# print(marks.values())

# keys used for the key astraction

# print(marks.keys())

# for updating the dictonries like changing in the current keys 
# (marks.update({"harrry":99})) 
# print(marks) 
#  you can also add that in the dictnories using the update function just let u know that the enteries should not be present in the dict or it will just update the dict
# marks.update({"himanshu":99} ) 
# marks.update({'shubham':23,"salman":1})
# 
# marks.update({"ashish":23,"aditya":90}  ) # can we add two input at once  
#  increasing the term 
# marks.update({"icespice":0,"arpitbala":90,"kaicenet":100})
# print(marks.keys())
# print(marks.items())
# print(marks.values())

#  get method 
             # use for the extration of the  values it will give the if the given key is presn
# print(marks.get(("harrry"))) # u can get this if the givem key is present in the dictnories 


#  BIGGEST DIFFERENCCE BETWEEN 
# print(['harrry'])
# print(marks.get("harrry"))
# in both of these we get the value but if the key is wrong the print harry will print error 
# and the get will print none 
# print(marks["uais"]) # this will print the error in key 
# print(marks.get("harr3y"))# this will print the the none becausse the key is not present 