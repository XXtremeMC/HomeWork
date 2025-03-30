def is_palindrome(text):
    text = text.lower()

    cleaned_text = ''.join(char for char in text if char.isalnum())

    return cleaned_text == cleaned_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') is True, 'Test1'
assert is_palindrome('0P') is False, 'Test2'
assert is_palindrome('a.') is True, 'Test3'
assert is_palindrome('aurora') is False, 'Test4'
print("ОК")
print(is_palindrome('OP'))
print(is_palindrome('A man, a plan, a canal: Panama'))
