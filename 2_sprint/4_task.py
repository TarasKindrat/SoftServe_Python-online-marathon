"""
As input data, you have a string that consists of words that have duplicated characters at the end of it.

All duplications may be in the next format:

    wordxxxx
    wordxyxyxy
    wordxyzxyzxyz

, where x, xy or xyz repeated ending of the word

Using re module write function pretty_message() that remove all duplications

For example:
Test 	Result

data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed
groupssss of symbolssss"
print(pretty_message(data))



This is echo string. Replace repeated groups of symbols

data = "Another input data string"
print(pretty_message(data))
"""

import re
def pretty_message(data: str) -> str:
    new_list = []
    list = data.split()
    repeat_pattern = re.compile(r'(\w)\1*')
    repeat_pattern2 = re.compile(r'(\w\w)\1+')
    repeat_pattern3 = re.compile(r'(\w\w\w)\1+')
    match_substitution = r'\1'

    for item in list:
        y = repeat_pattern.sub(match_substitution, item)
        z = repeat_pattern2.sub(match_substitution, y)
        new_list.append(repeat_pattern3.sub(match_substitution, z))
    return ' '.join(new_list)



print(pretty_message("Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"))