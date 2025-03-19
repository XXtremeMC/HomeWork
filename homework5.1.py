import string

test_data = ['_', '__', 'x', 'my_value', 'my name', 'hello!',
             'super_cool_value', 'Big_value', 'small_Value', 'getValue',
             '7up', 'up7', 'while', 'do_something', 'super_duper_value']

reserved_words = ['__', 'my name', 'hello!', 'Big_value', 'small_Value',
                  'getValue', '7up', 'while']

for test_variable in test_data:
    if len(test_variable) > 0:
        if test_variable in reserved_words:
            print("Error! " + test_variable + " is reserved!")
        elif test_variable[0].isnumeric():
            print("Error! " + test_variable + " starts with number!")
        elif not test_variable.islower():
            print("Error! " + test_variable + " has big letters!")
        elif " " in test_variable:
            print("Error! " + test_variable + " has space!")
        else:
            is_good = True
            for symbol in string.punctuation:
                if symbol != "_" and symbol in test_variable:
                    is_good = False
                    print("Error! " + test_variable + " has bad symbol!")
                    break
            if is_good:
                print("Good! " + test_variable + " is ok!")
    else:
        print("Error! Empty name!")