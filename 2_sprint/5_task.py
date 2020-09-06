"""
As input data you have list of strings with information about some location:

"id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"

Using regular expression write method max_population() for parsing strings and get info about location with highest population
"""
import re


def max_population(data):
    city = ''
    max_population = 0

    for item in data:
        if re.findall(r',(\d+)', item):

            population = int((''.join(re.findall(r',(\d+)', item))))
            if population > max_population:
                max_population = population
                city = ''.join(re.findall(r',(\w+),', item))
    max = (city, max_population)
    #return f"'{city}', {str(max_population)}"
    return max


data = ["id,name,poppulation,is_capital",
        "3024,eu_kyiv,24834,y",
        "3025,eu_volynia,20231,n",
        "3026,eu_galych,23745,n",
        "4892,me_medina,18038,n",
        "4401,af_cairo,18946,y",
        "4700,me_tabriz,13421,n",
        "4899,me_bagdad,22723,y",
        "6600,af_zulu,09720,n"]

print(max_population(data))
