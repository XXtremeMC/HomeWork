def first_word(text):
    word = ""
    started = False

    for char in text:
        if char.isalpha() or char == "'":
            word += char
            started = True
        elif started and char in " ,.":
            break

    return word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

print(first_word("Hello world"))
