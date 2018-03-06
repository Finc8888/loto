# Лото
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 1. Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 2. Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 1. Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 2. Если цифры на карточке нет - игра продолжается.
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html
# Домашнее задание на GitHub
# https://github.com/GeekBrainsTutorial/Python_lessons_basic/tree/master/lesson07
#Создание функции-генератора для получение случайного бочонка
from random import randint, sample, choice
import itertools as it
# def gen():
# 	samp = range(1, 91)
# 	stack = iter(sample(samp, 90))
# 	return next(stack)
# #print(gen())
# #Генерация позиции нахождение числа в карточке
# def position():
# 		samp = range(9)
# 		stack = iter(sample(samp, 9)) #for i in range(5)])
# 		return next(stack)
# 		# print(stack)
#
# def card_str():
# 	samp = range(1, 91)
# 	stack2 = iter(sample(samp, 15))
# 	a_field = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
# 	b_field = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
# 	c_field = ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
# 	for i in range(5):
# 		a_field[position()] = next(stack2)
# 		print(a_field,"a",position())
# 	for i in range(5):
# 		b_field[position()] = next(stack2)
# 		print(b_field,"b",position())
# 	for i in range(5):
# 		c_field[position()] = next(stack2)
# 		print(c_field,"c",position())
#
# 	sign = it.chain(a_field, b_field, c_field)
# 	print(list(sign))
# 	print("Карточка компьютера".center(35, "-"))
# 	# for j in range(3):
# 	# 	for i in sign:
# 	# 		print(i)
# 	# 		print("\n")
# 	a = iter(a_field)
# 	b = iter(b_field)
# 	c = iter(c_field)
# 	for i in a:
# 		print(i, end = " ")
# 	print("\n")
# 	for i in b:
# 		print(i, end = " ")
# 	print("\n")
# 	for i in c:
# 		print(i, end = " ")
# 	print("\n")
# # print(position())
# print(card_str())
import pytest
class Gamer(object):
	from random import randint, sample, choice
	import itertools as it
	"""Карточка игрока"""
	# card = [["-"] * 9, ["-"] * 9, ["-"] * 9]
	N = 90
	def __init__(self):
		# self.arg = arg
		pass
	def forming(self):
		"""
		Заполнение карточки случайными числами
		"""
		card = [["-"] * 9, ["-"] * 9, ["-"] * 9]
		import itertools
		card2 = list(itertools.chain(*card))
		print(card2)
		memory = []
		for i in card:
			# print(i)
			nums_insert = []
			nums_loto = []
			while len(nums_insert) < 5:
				num = choice(list(range(0,9)))
				# print("num=",num)
				if num not in nums_insert:

					loto_num = choice(list(range(1,91)))
					print("loto_num=", loto_num)
					if loto_num not in nums_loto:
						nums_insert.append(num)
						nums_loto.append(loto_num)
						i[num] = loto_num
						print(loto_num)
						print(nums_loto)
				else:
					continue
			# memory.
		# nums_insert = []
		# nums_loto = []
		return card



class Player(Gamer):
	"""docstring for Player."""
	def __init__(self):
		pass


class PC(Gamer):
	"""docstring for Player."""
	def __init__(self):
		pass


class Game(object):
	"""Реализован порядок игры в лото согласно правилам"""
	def __init__(self, arg):
		super(Game, self).__init__()
		self.arg = arg

def test_5field(who):
	"""
	Метод тестирования количества цифр в каждом поле карточки(5)

	"""
	for i in who:
		assert i.count("-") == 4,"Поля не верно сформированы"


def test_card(who2):
	"""
	Метод тестирования количества цифр в каждом поле карточки(5)

	"""
	bufer = []
	for i in who2:
		for j in i:
			if j == "-":
				continue
			elif j not in bufer:
				bufer.append(j)

			else:
				print(j)
				assert j == 100,"Одинаковые номера в одной карточке"
	print(*sorted(list(map(int,filter(lambda x: x!= "-", bufer)))))
	bufer = []


a = Player()
b = PC()

print("Карточка игрока".center(30, '#'))
card_player = a.forming()
test_5field(card_player)
print("")
for j in card_player :
	print(*j)
test_card(card_player)

print("Карточка компьютера".center(30, '#'))
card_pc = b.forming()
test_5field(card_pc)
print("")
for k in card_pc:
	print(*k)
test_card(card_pc)


# if __name__ == '__main__':
