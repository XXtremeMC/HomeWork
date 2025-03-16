import string

input_string = input("Enter a string: ")

no_punctuation = ""
for char in input_string:
    if char not in string.punctuation:
        no_punctuation += char

hashtag = '#'
for word in no_punctuation.split():
    hashtag += word.capitalize()

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
