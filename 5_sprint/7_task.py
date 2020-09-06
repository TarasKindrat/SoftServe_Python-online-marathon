"""
Write the function valid_email(...) to check if the input string is a valid email address or not.

An email is a string (a subset of ASCII characters) separated into two parts by @ symbol, a “user_info” and a domain_info, that is personal_info@domain_info:

    in case of correct email the function should be displayed the corresponding message – "Email is valid"
    in case of incorrect email the function should be displayed the corresponding message – "Email is not valid"


Note: in the function you must use the "try except" construct.


Function example:

valid_email("trafik@ukr.tel.com")          #output:   "Email is valid"

valid_email("trafik@ukr_tel.com")        #output:   "Email is not valid"

valid_email("tra@fik@ukr.com")           #output:   "Email is not valid"

valid_email("ownsite@our.c0m")         #output:   "Email is not valid"


"""


def valid_email(email):
    import re
    try:
        pattern = "[a-z-0-9]+@[a-z]+\.*[a-z]+"
        result = re.search(r'(^[a-z-0-9]+@([a-z]+\.)+[a-z]+$)', email)
        #print(result)
        if result:
            print("Email is valid")
        else:
            raise ValueError("Email is not valid")
    except ValueError as e:
        print("Email is not valid")


valid_email("trafik@ukr.jjjj.com")
valid_email("trafik@ukr.com")
valid_email("trafik@ukr.tel..com")
valid_email("example@source_arth.com")
