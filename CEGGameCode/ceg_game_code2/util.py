from random import randint
import argparse

def diceThrow():          #주사위는 눈 6개를 가지는 것 두개 
	dice1 = randint(1, 6)
	dice2 = randint(1, 6)

	# Return total num of eyes, and whether or not the dices were equal(총 눈 수와 주사위가 동일한지 여부를 반환합니다.)
	return [dice1 + dice2, dice1 == dice2]

#정수형인지 아닌지 알아보는 코드
def representsInt(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False


def positiveInt(x):
	if not representsInt(x):
		raise argparse.ArgumentTypeError("should be a integer")
	x = int(x)
	if x <= 0:
		raise argparse.ArgumentTypeError("should be bigger than 0")
	return x