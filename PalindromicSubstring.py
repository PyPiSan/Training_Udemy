'''Palindromic Substring
Description

You are provided a stringS.

Write a program that returns length of the longest palindromic substring of that string.


Input
Input Format

First line contains S, a string.

Constraints

`1 <= Length of string <= 100


Output
Output Format

Output one number which is length of the longest substring which is a palindrome'''

input_string = input()

def reversethestring(in_string):
    reverse_string = ""
    for char in range(len(in_string)-1, -1, -1):
        reverse_string += in_string[char]

    if reverse_string == in_string:
        return True
    else:
        return False

def maxpalindrome(string):
    max_len = 1
    lenth = len(string)
    for i in range(lenth):
        temp = ""
        j = i+1
        while j < (lenth+1):
            temp = string[i:j]
            if reversethestring(temp) == True and len(temp)> max_len:
                max_len = len(temp)
            else:
                j +=1
    return max_len

print(maxpalindrome(input_string))
