# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

#a) Добавьте игру против бота и добавить интеллект

from random import randint


def winner(a, b):
    if a == 1 and b == 0:
        return 'User #1 is a winner'
    elif a == 0 and b == 0:
        return 'bot is a winner'


n = 2021
while n > 0:
    h = 0
    count_user1 = int(input('How many candies would you like to have up to 28? '))
    if count_user1 < 1 or count_user1 > 28:
        print('User #1 has an incorrect number, try again.')
    else:
        n = n - count_user1
        result = winner(h, n)
        print('There', n, 'candies left')
        result = winner(h, n)
        if result:
            print(result)
            exit()
    h = 1
    count_bot = n % 29
    if count_bot == 0:
        count_bot = 1
    print('bot has chosen', count_bot, 'number of candies')
    n = n - count_bot
    print(f'There', n, 'candies left')
    result = winner(h, n)
    if result:
        print(result)
        exit()
