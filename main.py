original_text = input('Введите сообщение: ')
length_text = len(original_text)
print(f"Количество символов в строке: {length_text}")
print(f"Второй символ в строке: {original_text[1]}")
print(f"Последний символ в строке: {original_text[-1]}")
print(f"Первые три символа в строке : {original_text[:3]}")
print(f"Последние три символа в строке : {original_text[-3:]}")
print("\u001b[36;1m")
print("\u001b[42m")
print(original_text)
print("\u001b[0m")
color = input("""Выберите цвет:
1. Красный
2. Синий
3. Зелёный
В ответе запишите цифру: """)
color_start = int(input("Выберите с какого символа закрашивать. В ответ запишите цифру: "))
color_end = int(input("Выберите по какой символ закрашивать. В ответ запишите цифру: "))
if color == "1":
    print(f"{original_text[:color_start]}\u001b[31m{original_text[color_start:color_end]}\u001b[0m{original_text[color_end:]}")
elif color == "2":
    print(f"{original_text[:color_start]}\u001b[34m{original_text[color_start:color_end]}\u001b[0m{original_text[color_end:]}")
elif color == "3":
    print(f"{original_text[:color_start]}\u001b[32m{original_text[color_start:color_end]}\u001b[0m{original_text[color_end:]}")
else:
    print("""Ошибка. Попробуйте позже.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
error: 403""")
old_char = input("Выберите символ, который хотите заменить: ")
new_char = input("Выберите символ, на который хотите заменить: ")
modified_text = original_text.replace(old_char, new_char)
print(f"{modified_text}")
even_chars = modified_text[::2]
print(f"Срез по нечётным символам: {even_chars}")
odd_chars  = modified_text[1::2]
print(f"Срез по чётным символам: {odd_chars}")
reversed_text = original_text[::-1]
print(f"Текст с изменённым порядком номеров: {reversed_text}")
middle_index = len(original_text)//2
swapped_text = original_text[middle_index:] + original_text[:middle_index]
print(swapped_text)
