"""
Question text

Write  the function divide_number(num_1, num_2) the two input parameters of which are numbers.
The function returns the result of dividing two numbers.
     in case of correct data the function should be displayed the corresponding message –

"Result is … " \n  "No exceptions:)" \n "Closed all connections."

    in the case of division by zero the function should be displayed the corresponding message –

"Oops, division by zero is error!!!" \n "Closed all connections."

    in the case of incorrect data the function should be displayed the message – "Value Error" \n
    "Closed all connections."

    in all other cases the function should be displayed the message –"Something went wrong:(" \n "Closed all connections."

symbol \n means moving to a new line

Note: in the function you must use the "try except" construct.

Function example:

divide_number(8, 16)        #output:   "Result is 0.5" \n "No exceptions:)" \n "Closed all connections."

divide_number (5, 0)        #output:   "Oops, division by zero is error!!!" \n "Closed all connections."

divide_number("25", 5)    #output:   "Result is 5.0" \n "No exceptions:)" \n "Closed all connections."

 divide_number("abc", 9)  #output:    "Value Error" \n "Closed all connections."

"""


def divide_number(num_1, num_2):
    try:
        result = int(num_1) / int(num_2)
        print(f"Result is {result} \nNo exceptions:)\nClosed all connections.")
    except ZeroDivisionError:
        print("Oops, division by zero is error!!! \nClosed all connections.")
    except ValueError:
        print("Value Error \nClosed all connections.")
    except:
        print("Something went wrong:( \nClosed all connections.")

divide_number("9", 3)