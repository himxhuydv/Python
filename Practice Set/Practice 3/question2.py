# #  write a program to full  ina letter template given below with date and name
# letter="""dear </Name/>
# you are selected!
# </date/>"""
# # long way my way
# # p=(letter.replace("</Name/>","himanshu",))
# # c=(p.replace("</date/>","160407"))
# # print(c) 
# #                            smart way in this we order the string to replace and order again to make changes and replace again
# print(letter.replace("</Name/>","himanshu").replace("</date/>","26 september"))


#  if we do that function repeat in replace the print optin can we do this 
name="himanshu yadav i am saying that i am here to greet u all "
print(name.replace("himanshu","himxhu")
      .replace("yadav","ydv")
      .replace("sayanding","saying"))
