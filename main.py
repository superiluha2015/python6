secret_word = input("Введите слово для игры: ")
print("\033[2J")
win = False
all_letters = []
true_letters = []
points = [0, 0, 0]
counter = 0
while not win:
    letter = input(f"\nИгрок {counter + 1} введите букву: ")
    if letter in all_letters:
        print("Вы уже вводили эту букву")
    elif letter in secret_word:
        true_letters.append(letter)
        print("Вы угадали букву")
        points[counter] += 10
        print(f"Ваши очки - {points}")
    else:
        print("такой буквы нет в слове")
        counter += 1
        if counter == 3:
            counter = 0
    all_letters.append(letter)
    win = True
    for symbol in secret_word:
        if symbol in true_letters:
            print(symbol, end="")
        else:
            print("*", end="")
            win = False
print(f"""
Очки игроков:
Игрок 1 - {points[0]}
Игрок 2 - {points[1]}
Игрок 3 - {points[2]}""")