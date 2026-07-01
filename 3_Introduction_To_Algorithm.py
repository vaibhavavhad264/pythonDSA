# 1) Palindrome number

def aplindrome(s : str):
    for i in range(0, len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True
print(aplindrome('abcdcba'))

def is_palindrome(s: str):
    return s == s[ : : -1]
print(is_palindrome('abcd'))
print(is_palindrome('ab'))
print(is_palindrome(''))

