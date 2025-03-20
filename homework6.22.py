seconds = int(input("Enter second: "))

SEC_IN_MINUTE = 60
SEC_IN_HOUR = 60 * 60
SEC_IN_DAY = 24 * 60 * 60

days, remainder = divmod(seconds, SEC_IN_DAY)
hours, remainder = divmod(remainder, SEC_IN_HOUR)
minutes, seconds = divmod(remainder, SEC_IN_MINUTE)

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)


if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    day_word = "дні"
else:
    day_word = "днів"

result = f"{days} {day_word} {hours_str}:{minutes_str}:{seconds_str}"
print(result)
