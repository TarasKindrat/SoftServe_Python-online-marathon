"""
Create function file_parser. If function called with 2 arguments programm must count the number
of occurrences string in a file, if 3 arguments programm must replace string in a file to new string

first argument - path to file

second argument - find string

third argument - replace string

Function must returned string with count of occurrences or count of replaced strings

Example:
    file_parser("file.txt", 'x', 'o')-> Replaced 8 strings
    file_parser("file.txt", 'o') -> Found 8 strings
Please, create class ParsesTest and write unittest for file_parser function uses mock object
"""
import unittest


def file_parcer(file, search_letter, replased_letter=None):
    count = 0
    try:
        f = open(file, "r")
        text = f.read()
        if replased_letter:
            count = text.count(search_letter)
            text = text.replace(search_letter, replased_letter)
            f.close()
            fw = open(file, 'w')
            fw.write(text)
            fw.close()
            return f"Replased {count} strings"
        if not replased_letter:
            count = text.count(search_letter)
            return f"Found {count} strings"
        f.close()
    except FileNotFoundError:
        print("No file")


# class ParserTest(unittest.TestCase):
#    pass


print(file_parcer("1.txt", "txt", "open"))
