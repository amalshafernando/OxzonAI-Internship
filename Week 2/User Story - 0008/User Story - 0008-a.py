'''
User Story - 0008 - Error Handling and Debugging
● Topics Covered
    ○ Try, except blocks.
    ○ Raising exceptions.
    ○ Debugging basics and error types.
● Exercises
    ○ Write a program that catches division-by-zero errors.
    ○ Implement exception handling in a calculator program.
'''

#----------------------------------------------------------------
''' Write a program that catches division-by-zero errors.'''
  
def sub_division():
    try:
        numerator = int(input('numerator = ')) 
        denominator = int(input('\ndenominator = '))
        result = numerator/denominator
        print("result = ", result)
    except ZeroDivisionError:
        print('Error: Division by zero is not allowed')
    except ValueError:
        print("Invalid input, please enter valid input")
 
sub_division() 
    

        
            
    
    