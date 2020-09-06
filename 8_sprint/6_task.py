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
