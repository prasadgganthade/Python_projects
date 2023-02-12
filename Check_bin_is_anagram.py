# 8. Check if binary representations of two numbers are an anagram
from collections import Counter

def check_bin_is_anagram(num1,num2):
    n1 = bin(num1)[2:]  # removing 0b part and get pure binary format
    n2 = bin(num2)[2:]

    # Adjusting the length of uneven binary numbers
    zero = abs(len(n1) - len(n2))
    if len(n1) > len(n2):
        n2 = '0' * zero + n2
    else:
        n1 = '0'*zero + n1

    if Counter(n1) == Counter(n2):
        # Counter converts string to dictionary
        return True
    else:
        return False

num1,num2 = map(int,input().split())
print('Binary representation of two numbers are an anagram :',check_bin_is_anagram(num1,num2))

"""
o/p
8 98
Binary representation of two numbers are an anagram : False
"""