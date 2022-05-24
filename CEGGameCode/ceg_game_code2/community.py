import random
from chance import *
#공공기금 카드
class CommunityCard:

	def __init__(self,card_name,card_type, value):
		self.card_name=card_name
		self.type = card_type
		self.value = value

	def __str__(self):
		#읽을 수 있는 형태로 찬스 카드 반환
		return "CommunityCard(%s, %s,%s)" % (self.card_name,self.card_type, str(self.value))

class CommunityPile:
#카드의 이름은 "GetFuel","GetResource", "LoseFuel", "LoseResource"
#카드의 타입은 "Fuel", "Resource"
#카드의 벨류는 얻거나 잃는 값
	CARDS = [
		CommunityCard("GetFuel","Fuel",5),
		CommunityCard("GetFuel","Fuel", 7),
		CommunityCard("GetResource","Resource",100),
		CommunityCard("GetResource","Resource", 150),
		CommunityCard("LoseFuel","Fuel",-2),
		CommunityCard("LoseFuel","Fuel",-3),
		CommunityCard("LoseResouce","Resource",-100),
		CommunityCard("LoseResouce","Resource",-150),

	]

	def __init__(self):
		# 카드 순서 생성
		self.pile = random.sample(range(0, len(self.CARDS)),
			len(self.CARDS))

	def pullCard(self):
		# 제일 위에 있는 카드 뽑기
		card = self.pile[0]

		# 뽑은카드를 제일 아래에 놓기
		newPile = [None] * len(self.pile)
		for i in range(0, len(self.pile) - 1):
			newPile[i] = self.pile[i + 1]
		newPile[len(newPile) - 1] = card

		# Set the new pile to be the pile
		self.pile = newPile
		
		# 원래의 pile 맨 위에있던 카드를 반환함.
		return self.CARDS[card]

	def __str__(self):
		# Start with calling that is a pile of cards
		string = "PILE OF COMMUNITY CHEST CARDS:\n"

		# 모든 찬스카드를 출력
		for cardIndex in self.pile:
			string += " - "
			string += str(self.CARDS[cardIndex])
			string += "\n"

		# 문자열 리턴
		return string
