import random
class ChanceCard:
	def __init__(self, card_name, card_type, value):
		self.card_name = card_name
		self.type = card_type
		self.value = value

	def __str__(self):
		# 읽을 수 있는 형태로 찬스 카드 반환
		return "ChanceCard(%s, %s, %s)" % (self.card_name, self.card_type, str(self.value))

class ChancePile:
#카드의 이름은 "GoToBlackholl", "GoToEarth","GoToRandom","GoToFreeParking","GetFuel","GetResource", "LoseFuel", "LoseResource"
#카드의 타입은 "Move", "Fuel"", "Resource"
#카드의 벨류는 "Move" 일때는 이동하는 칸의 값, "Value" 일때는 얻거나 잃는 값
	CARDS = [
		ChanceCard("GoToBlackholl", "Move", 31),
		ChanceCard("GoToEarth","Move",0),
		ChanceCard("GoToRandom","Move",random.randrange(0,41)),
		ChanceCard("GoToFreeParking","Move",21),
		ChanceCard("GetFuel","Fuel", 3),
		ChanceCard("GetFuel","Fuel", 5),
		ChanceCard("GetResource","Resource", 50),
		ChanceCard("GetResource","Resource", 100),
		ChanceCard("LoseFuel","Fuel", -1),
		ChanceCard("LoseResource","Resource",-50),
	]

	def __init__(self):
		# 찬스카드 순서 생성
		self.pile = random.sample(range(0, len(self.CARDS)),
			len(self.CARDS))

	def pullCard(self):
		# 현재 파일 맨 위에 있는 카드 가져오기 (젤 위에있는 카드를 뽑는다)
		card = self.pile[0]

		# 선택한 카드를 맨 아래에 두고 새 파일 생성
		newPile = [None] * len(self.pile)
		for i in range(0, len(self.pile) - 1):
			newPile[i] = self.pile[i + 1]
		newPile[len(newPile) - 1] = card

		# newPile을 pile로 설정.
		self.pile = newPile
		
		# 원래 파일 맨 위에 있던 카드 반환
		return self.CARDS[card]

	def __str__(self):
		# Start with calling that is a pile of cards
		string = "PILE OF CHANCE CARDS:\n"

		#모든 찬스카드 출력
		for cardIndex in self.pile:
			string += " - "
			string += str(self.CARDS[cardIndex])
			string += "\n"

		# 생성된 문자열 반환
		return string
