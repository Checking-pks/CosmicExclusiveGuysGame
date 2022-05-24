class Board:

	TILE_NAME = [
		"시작점(지구)",
		"화성",
		"우주선 발전기금",
		"세레즈",
		"이용감사료",
		"남쪽 우주비행선",
		"목성",
		"찬스",
		"토성",
		"천왕성",
		"Just Visiting",
		"블랙홀",
		"해왕성",
		"무료 우주 여행",
		"명왕성",
		"하우메아",
		"서쪽 우주비행선",
		"마케마케",
		"우주선 발전기금",
		"에리스",
		"이오",
		"FREE PARKING",
		"큰곰자리",
		"찬스",
		"판도라",
		"오베론",
		"북쪽 우주비행선",
		"아리엘",
		"히페리온",
		"무료 우주 여행",
		"프로메테우스",
		"블랙홀로 가시오.",
		"말머리 성운",
		"태양",
		"우주선 발전기금",
		"수성",
		"동쪽 우주비행선",
		"찬스",
		"금성",
		"이용 감사료",
		"달"
	]

	TILES_REAL_ESTATE  = [1,3,6,8,9,12,14,15,17,19,20,22,24,25,27,28,30,32,33,35,38,40]
	TILES_CHANCE       = [7,23,37]
	TILES_COMMUNITY    = [2,18,34]
	TILES_TRAVEL       = [13,29]
	TILES_TRANSPORT    = [5,16,26,36]
	TILES_TAX          = [4,39]
	TILES_NONE         = [10]
	TILES_FREE_PARKING = [21]
	TILES_JAIL         = [11]
	TILES_GO_TO_JAIL   = [31]
	TILES_GO           = [0]

	def __init__(self):
		# 타일의 총 개수가 맞는지 확인.
		tilesCount = self.getSize()
		#만약 타일의 개수가 41개가 아니라면,
		if tilesCount != 41:
			print ("Game board consists of %i tiles, instead of 41!" % tilesCount)

		# 플레이어가 타일에 착륙한 시간을 추적하도록 배열 설정
		self.hits = [0] * 41

	def getTileType(self, tile):
		# 주어진 칸과 일치하는 문자열 반환
		if tile in Board.TILES_REAL_ESTATE:
			return "realestate"
		elif tile in Board.TILES_CHANCE:
			return "chance"
		elif tile in Board.TILES_TRAVEL:
			return "travel"
		elif tile in Board.TILES_COMMUNITY:
			return "community"
		elif tile in Board.TILES_TRANSPORT:
			return "transport"
		elif tile in Board.TILES_TAX:
			return "tax"
		elif tile in Board.TILES_JAIL:
			return "jail"
		elif tile in Board.TILES_GO_TO_JAIL:
			return "gotojail"
		elif tile in Board.TILES_GO:
			return "go"
		else:
			return "none"


	def hit(self, tile):
		# Increment tile hit count in array
		self.hits[tile] += 1

	def getSize(self):
		return (len(Board.TILES_REAL_ESTATE) + len(Board.TILES_CHANCE) +
				len (Board.TILES_TRAVEL)+
				len(Board.TILES_COMMUNITY)+
				len(Board.TILES_TRANSPORT) + len(Board.TILES_TAX) +
				len(Board.TILES_NONE) + len(Board.TILES_JAIL) +
				len(Board.TILES_GO_TO_JAIL) + len(Board.TILES_GO))