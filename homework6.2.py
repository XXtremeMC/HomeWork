import string

input_string = input("Enter a string: ")
start, end = input_string.split('-')  # Розбиваємо на початок і кінець

letters = string.ascii_letters
start_idx = letters.index(start)
end_idx = letters.index(end)

result = letters[start_idx:end_idx + 1]
print(result)