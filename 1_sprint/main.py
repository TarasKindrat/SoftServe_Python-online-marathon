"""For n = 3 and k = 4, the output should be
kthTerm(n, k) = 9.

For n = 3, the sequence described above begins as follows: 1, 3, 4, 9, 10, 12, 13...
[3**0] => [1]
[1, 3**1, 3**1 +1] => [1, 3, 4]
[1, 3, 4, 3**2, 3**2 +1, 3**2 +3, 3**2 +4] => [1, 3, 4, 9, 10, 12, 13]
...

The 4th number in this sequence is 9, which is the answer.
"""
import sys
sys.maxsize = 1000
def kthTerm(n, k):
    list = []
    for i in range(0, k):
        print(f'before append{list}  n is: {n} i is:{i} {n**i}')
        list.append(n**i)
        print(f"after append {list}")
        #list2 = list
        last_element_number = len(list)-1
        print(f"last_element_number {last_element_number}")
        if last_element_number >= 1:
            for j in range(0, len(list)-1):
               # print(j)
                list.append(list[last_element_number]+list[j])
                print(f"i is: {i} and j is {j}")
                print(list)
    print(list)

    if k <= len(list):
        return list[k-1]
    else:
        return "IndexError: k out of range "


kthTerm(30, 100)


