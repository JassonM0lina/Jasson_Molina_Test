# -*- coding: UTF-8 -*-

#================================================================================
#  
#  Crée en 2 avr. 2020
#  @author: JassonM0lina
#   
#   
#  Question A:
#  
#  Your goal for this question is to write a program that accepts two lines 
#  (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. 
#  As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
#
#===================================================================================
#
#  Question A develop:
#  
#  The program compare the length of two one-dimensional line and returns whether    
#  they overlap. We can only input Float or Int type. The 1D line is defined by a 
#  start and end one-dimensional point (x-point).
#
#  In the other hand, the Complex type is not available because is a two-dimensional 
#  two-dimensional point (real,imag). Also, the program does not accept String, Bool 
#  and None Type to construct the line.
#
#  Run the Question_A.question_A.py file to make your own test. Also, you
#  can run the Question_A.test_A.py file to automatically do the test.   
#
#====================================================================================


from Question_A import question_A

 
## REFERENCE LINE 
line_ref = question_A.Line(1.1,5.2)  


## CASE TEST

# the beginning of the line is overlapping
case_test1 = question_A.Line(-10,1.1)

# the end of the line is overlapping
case_test2 = question_A.Line(5.2,10)

# the reference line is bigger than the case line
case_test3 = question_A.Line(1.2,5.1)

# the reference line is shorter than the case line
case_test4 = question_A.Line(1,5.3)

# Not overlapping in right side
case_test5 = question_A.Line(5.3,8)

# Not overlapping in left side
case_test6 = question_A.Line(-3.7,1)

# String input case
case_test7 = question_A.Line("Ormuco",5)

# Bool input case
case_test8 = question_A.Line(True,50)

# Nonetype input case
case_test9 = question_A.Line(None,98)

# Complex number input case, this type is no available because 
# Complex number is two dimensional point, we work only
# with one dimensional point for 1D => x - axis.
case_test10 = question_A.Line((3+2j),777)


## TEST CASES

        
cases = [case_test1, case_test2, case_test3, 
         case_test4, case_test5, case_test6,
         case_test7, case_test8, case_test9,
         case_test10]

for prove in cases:
    print(question_A.overlap(prove,line_ref))
    

