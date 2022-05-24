import random
from board import *

class Player:

	def __init__(self):
		#초기연료20
		self.fuel=20
		#초기자원 0 
		self.resource=0
		self.position = 0

#주사위가 움직이는 방법에 대한 함수
	def move(self, board, diceResults):
		# newPosition을 계산합니다. 필요한경우 overflow
		newPosition = self.getNewPosition(diceResults[0], board)
		# 10번 Just Visiting과 11번 Blackhole이 같은 위치라 도착 위치가 그 사이일 시 위치 +1
		if (newPosition >= board.TILES_JAIL[0] and newPosition < 35) and (
				self.position < board.TILES_JAIL[0] or self.position > 35):
			newPosition += 1
		# 새 위치 적용
		self.position = newPosition

    # 새로운 위치 구하는 함수 (현재 위치 + 주사위 값) % 전체 보드 사이즈
	def getNewPosition(self, offset, board):
		return (self.position + offset) % board.getSize()

	def doChanceCard(self, card, board):
		if card.card_type == "Move":
			if "Blackholl" in card.card_name:
				self.position = board.TILES_JAIL[0]
			elif "Earth" in card.card_name:
				self.position = board.TILES_GO[0]
			elif "Random" in card.card_name:
				self.position = random.randrange(0,41)
			elif "FreeParking" in card.card_name:
				self.position = board.TILES_NONE[1]
			
		
		elif card.card_type=="Fuel":
			self.fuel +=card.value
		else:
			self.resource +=card.value

	def doCommunityCard(self, card):
		# community 카드타입이 Fuel인 경우 
		if card.card_type == "Fuel":
			self.fuel += card.value
		# community 카드타입이 Resource인 경우
		else:
			self.resource +=card.value