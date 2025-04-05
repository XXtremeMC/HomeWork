def popular_words(text, words):
    text_words = text.lower().split()  # Перетворюємо текст в нижній регістр і розбиваємо на слова

    result = {}  # Створюємо словник з результатами

    for word in words:
        # Рахуємо кількість входжень слова в тексті
        # За замовчуванням встановлюємо 0
        result[word] = text_words.count(word)

    return result


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
print(popular_words)
