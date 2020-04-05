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


class Line:
    
    '''Représentation d'une ligne dans le x-axe, les attributs sont X1 et X2 
       qui représentent les valeur des coordonnées unidimensionnelles, x-point '''
    
    def __init__(self,begin,finish):       
        '''les constructeurs de la ligne, X1 et X2 doivent être numériques,
           sinon, l'exception TypeError est déclenché''' 

        if (type(begin) is not bool) and (type(finish) is not bool): 
            try:
                'organisateur en ordre croissant'
                self.begin = min(float(begin),float(finish))
                self.finish = max(float(begin),float(finish))                               
            except:
                pass
        else:
            pass     
        
'Vérifier si self-ligne se chevaucher avec ref-ligne'
def overlap(line_case,line_ref):         
    try:       
        if line_ref.begin >= line_case.begin and line_ref.begin <= line_case.finish:
            return show(line_case,line_ref,"Overleap")        
        elif line_ref.finish >= line_case.begin and line_ref.finish <= line_case.finish:
            return show(line_case,line_ref,"Overleap")       
        elif line_ref.finish >= line_case.finish and line_ref.begin <= line_case.begin:
            return show(line_case,line_ref,"Overleap")       
        else:                
            return show(line_case,line_ref,"No Overleap")       
    except:
        return print("X1 and X2 must be numeric values")
           
' impression des attributs de self-ligne et réf-lign. aussi, état de chevaucher '    
def show(line_case,line_ref,ovleap):
      
        return ("""Line_case: ({0}, {1}) - {2} - Line_ref: ({3} {4}) """
                .format(line_case.begin, line_case.finish, ovleap, 
                        line_ref.begin, line_ref.finish))
 
# =======================================================================================


if __name__ == "__main__":
        
    A=input("Enter X1 - for Reference line: ") 
    B=input("Enter X2 - for Reference line: ")    
    C=input("Enter X1 - for Case line: ")
    D=input("Enter X2 - for Case line: ")     
    line_case = Line(C,D)
    line_ref = Line(A,B)
    
    print(overlap(line_case,line_ref))
    
else:   
    print("You are running the test_A")
    
    
    