# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficiency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text = str(text)
    text_len = len(text)
    i = 0
    j = 0
    max_palindrom_len = 0
    for index, symbol in enumerate(text):
        left_index = right_index = index
        while left_index >=0 and right_index < text_len:
            if str.lower(text[left_index]) == str.lower(text[right_index]):
                right_index += 1
            if right_index >= text_len:
                break
            if not str.lower(text[left_index]) == str.lower(text[right_index]):
                left_index -= 1
            if left_index < 0:
                left_index += 1
                break
            if not str.lower(text[left_index]) == str.lower(text[right_index]):
                left_index += 1
                break
        cur_len = right_index - left_index
        if cur_len > max_palindrom_len:
            max_palindrom_len = cur_len
            i = left_index
            j = right_index
        
    return i, j
    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()