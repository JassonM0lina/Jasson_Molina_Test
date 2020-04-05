# Ormuco Questions and development
 
Question A:  
Your goal for this question is to write a program that accepts two lines 
(x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. 
As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

Question B:   
The goal of this question is to write a software library that accepts 2 version 
string as input and returns whether one is greater than, equal, or less than the 
other. As an example: “1.2” is greater than “1.1”. Please provide all test cases 
you could think of.

#=============================================================================
QUESTION A DEVELOP:  

The program compare the length of two one-dimensional line and returns whether they overlap. We can only input Float or Int type. The 1D line is defined by a 
start and end one-dimensional point (x-point).

In the other hand, the Complex type is not available because is a two-dimensional 
two-dimensional point (real,imag). Also, the program does not accept String, Bool 
and None Type to construct the line.

Run the Question_A.question_A.py file to make your own test. Also, you
can run the Question_A.test_A.py file to automatically do the test.   

#==============================================================================
QUESTION B DEVELOP:

The program compare two String input and returns whether one is greater than, equal, 
or less than the other. Each String can be converter into Complex number or continue be a String to make the comparison.
   
The Complex number are not ordered, so we define a lexicographical order. If we convert the rectangular coordinates into polar form we have  

I.  string1 = x1 + y1j => string1 = r1∙e**θ               
II. string2 = x2 + y2j => string2 = r2∙e**ϕ  
  
We define the bool attribute weight for the class String_Compare, to select the two
lexicographical order programmed. 
  
1.) The first order compare the magnitudes part. If the magnitudes are equal 
    (r1==r2) then compare the angles. This order correspond to True bool value.

2.) The second order compare the angle part. If the angles are equal (θ==ϕ) then 
    compare the magnitudes. This order correspond to False bool value.

Note that if the two input Complex number are Int or Float Type, the two lexicographical 
order programmed do the normal comparison of real numbers. In conclusion, the attribute 
weight have relevance if one of the input string are Complex number.
  
Run the Question_B.question_B.py file to make your own test. Also, you
can run the Question_B.test_B.py file to automatically do the test.  
