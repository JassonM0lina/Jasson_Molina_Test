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

import cmath

class String_Compare:
    
    ''' Representation of class String_compare with three attributes: The two input string 
        to be compared and weigth attribute for Complex number '''
    def __init__(self,string1,string2,weigth):
        self.string1=string1
        self.string2=string2
        self.weigth = bool(weigth) 
        
    def value_type(self):
        
        try:
            'Convert rectangular form into polar form'         
            val1 = cmath.polar(complex(self.string1))
            val2 = cmath.polar(complex(self.string2))           
            
            ' Do the Complex number comparison depending of the weigth value'
            if ((val1[0] != val2[0] and self.weigth is True) or
                (val1[1] == val2[1] and self.weigth is False)):
                
                return compare(self, val1[0], val2[0])
                
            else:                
                return compare(self, val1[1], val2[1])                           
                
        except:
            
            if ((type(self.string1) is None or type(self.string2) is None) or
               (type(self.string1) is bool or type(self.string2) is bool)):               
                return print("One of the input is invalid")
            
            elif not type(self.weigth) is bool:
                return print(" Only accept bool type to choose the lexicographical comparison")
                          
            else:
                'Compare string input if are not other type values'
                return compare(self,self.string1,self.string2)
                                    

def compare(self,value1, value2):
    ' Method that compare value1 with value2'
    if value1 < value2:
        return show(self,"is less than")
    elif value1 > value2:
        return show(self,"is greater than")
    else:
        return show(self,"is equal to")
   
def show(self,result):    
    return """{0} {1} {2}""".format(self.string1, result,self.string2)  


#===========================================================================================

if __name__ == "__main__":   
    
    print("Only in complex number comparison, the lexicographical comparison is relevant")
    A = input("Enter the first string: ")
    
    try: 
        a = complex(A)
        
        try:
            a = float(A)

            "C could be False or True, not matter if is complex number comparison"
            C = True               
        except:
            C = input("Choose the two kind of lexicographical comparison - write True or False: ")            
    except:      
        "C could be False or True, not matter if is complex number comparison"
        C = True
        
    
    B = input("Enter the second string: ")
    
    try: 
        b = complex(B)
        
        try:
            b = float(B)                    
        except:
            if not isinstance(a, complex):
                C = input("Choose the two kind of lexicographical comparison - write True or False: ")            
    except:      
        pass
    
    print(String_Compare(A,B,C).value_type())
    
else:
    print("You are running the test_B")   

            