import random
from util import *
from board import *
from chance import *
from community import *


class Game:

	def __init__(self, players, rounds):
		self.players = players
		self.board = Board()
		self.chancePile = ChancePile()
		self.communityPile = CommunityPile()
		self.rounds = rounds

	def run(self):
		# 주어진 라운드 수 동안 게임 실행
		for i in range(0, self.rounds):
			self.round()

	def round(self):
		# 매 라운드마다, 모든 선수들은 자신의 차례를 가진다.
		for player in self.players:
			self.turn(player)

	def turn(self, player):
		# 주사위 눈을 값으로 가지는 diceResults변수
		diceResults = diceThrow()
		# 플레이어를 칸으로 이동시킵니다, goingToJail True 는 더블이 3개
		goingToJail = player.move(self.board, diceResults)

		#플레이어가 서있는 위치의 칸을 저장합니다.
		tileType = self.board.getTileType(player.position)

		#  'Go To Jail' tile에 위치하면 감옥에 가게합니다.(블랙홀)
		if tileType == "gotojail":
			goingToJail = True
			player.fuel -=5

		# 플레이어가 감옥에 가있을경우, 플레이어의 위치를 재 정의합니다.
		if goingToJail:
			player.position = Board.TILES_JAIL[0]

		# 찬스타일에 있을경우 찬스카드 실행
		if player.position in Board.TILES_CHANCE:
			player.doChanceCard(self.chancePile.pullCard(), self.board)

		# 우주선 발전기금 타일에있을경우 우주선발전기금카드 실행
		if player.position in Board.TILES_COMMUNITY:
			player.doCommunityCard(self.communityPile.pullCard(), self.board)
		
		# 무료우주 여행 타일에 있을 경우 랜덤으로 이동
		if player.position in Board.TILES_TRAVEL:
			player.position = choice([i for i in range(0,41) if i not in board.TILES_TRAVEL])
			#29번 무료우주여행은 나오지않게

        # Free Parking 타일에 있을 경우 자원을 100개 얻는다.
		if player.position in Board.TILES_FREE_PARKING:
			player.resource += 100

		# 우주비행선 타일에있을경우 연료를 3개얻는다.
		if player.position in Board.TILES_TRANSPORT:
			player.fuel += 3

		#이용 감사료 타일에있을 경우 자원 200개를 잃는다.
		if player.position in Board.TILES_TAX:
			player.resource -= 200

			
		


		# 플레이어가 모든 이동 후 타일 위에 착지했다는 사실 기록
		self.board.hit(player.position)

		# 감옥에 가지 않고 두 배를 던졌으면 다시 진행.
		if tileType != "jail" and diceResults[1]:
			self.turn(player)