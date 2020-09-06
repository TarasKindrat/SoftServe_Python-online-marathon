import re
test_str = "X-DSPAM-Confidence:0.8475"
print(test_str.split(":")[1])


str = "Pythom awasome"
print(str[-2:])

str2 = "British Libreri, London: 2015"
print(re.findall('[A-Z]{1}\w+\s[A-Z]{1}\w+,\s[A-Z]{1}\w+:\s\d{4}', str2))