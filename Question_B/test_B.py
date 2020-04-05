# -*- coding: UTF-8 -*-

#=====================================================================================
#  Créen 4 avr. 2020
#  @author: JassonM0lina   
# 
#  
#  Question B
#
#  The goal of this question is to write a software library that accepts 2 version 
#  string as input and returns whether one is greater than, equal, or less than the 
#  other. As an example: “1.2” is greater than “1.1”. Please provide all test cases 
#  you could think of.
#
#======================================================================================
#
#  Question B develop
#
#  The program compare two String input and returns whether one is greater than, equal, 
#  or less than the other. Each String can be converter into Complex number or continue  
#  be a String to make the comparison.
#   
#  The Complex number are not ordered, so we define a lexicographical order. If we  
#  convert the rectangular coordinates into polar form we have  
#
#  string1 = x1 + y1j => string1 = r1∙e**θ 
#  string2 = x2 + y2j => string2 = r2∙e**ϕ  
#  
#  We define the bool attribute weight for the class String_Compare, to select the two
#  lexicographical order programmed. 
#  
#  1.) The first order compare the magnitudes part. If the magnitudes are equal 
#      (r1==r2) then compare the angles. This order correspond to True bool value.
#
#  2.) The second order compare the angle part. If the angles are equal (θ==ϕ) then 
#      compare the magnitudes. This order correspond to False bool value.
#
#  Note that if the two input Complex number are Int or Float Type, the two lexicographical 
#  order programmed do the normal comparison of real numbers. In conclusion, the attribute 
#  weight have relevance if one of the input string are Complex number.
#  
#========================================================================================== 
#  Run the Question_B.question_B.py file to make your own test. Also, you
#  can run the Question_B.test_B.py file to automatically do the test.   
#
#===========================================================================================


from Question_B import question_B

print("\n# Trying on int\n")

print(question_B.String_Compare("10","20",True).value_type())
print(question_B.String_Compare("50","20",True).value_type())
print(question_B.String_Compare("5","5",True).value_type())

print("\n# Trying on float\n")

print(question_B.String_Compare("5.28","5.279",True).value_type())
print(question_B.String_Compare("100.23","250.87",True).value_type())
print(question_B.String_Compare("46.23","46.23",True).value_type())

print("\n# Trying on string\n")

print(question_B.String_Compare("DFR","RFD",True).value_type())
print(question_B.String_Compare("ormuco","ORMUCO",True).value_type())
print(question_B.String_Compare("ORMUCO","ORMUCO",True).value_type())

print("\n# Trying on complex, giving importance to the magnitud part\n")

print(question_B.String_Compare("3+2j","4+5j",True).value_type())
print(question_B.String_Compare("66+10j","55+8j",True).value_type())
print(question_B.String_Compare("8+6j","8+6j",True).value_type())

print("\n# Trying on complex, giving importance to the angle part \n")

print(question_B.String_Compare("3+2j","4+5j",False).value_type())
print(question_B.String_Compare("66+10j","55+8j",False).value_type())
print(question_B.String_Compare("8+6j","8+6j",False).value_type())

print("\n# Trying on complex and other types, giving importance to the angle part \n")

print(question_B.String_Compare("3+2j","32",False).value_type())
print(question_B.String_Compare("66+10j","52.8",False).value_type())
# In the below case 8+6j is treaty as string type
print(question_B.String_Compare("8+6j","Ormuco",False).value_type())



