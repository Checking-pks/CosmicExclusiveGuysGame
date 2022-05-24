import random

#  Tile Information
chanceTile = [7, 22, 36]
communityTile = [2,17]
thanksFee = [4, 39]
freeParking = [20]
freeTravel = [12, 28]
spaceCraft = [5, 15, 25, 35]

#땅 , 이름
playerTile = {
    0: ("지구"),
    1: ("화성"),
    2: ("우주선 발전기금"),
    3: ("세레스"),
    4: ("이용 감사료"),
    5: ("남쪽 우주비행선"),
    6: ("목성"),
    7: ("찬스 카드"),
    8: ("토성"),
    9: ("천왕성"),
    10: ("블랙홀"),
    11: ("Just Visiting"),
    12: ("해왕성"),
    13: ("무료 우주여행"),
    14: ("명왕성"),
    15: ("하우메아"),
    16: ("서쪽 우주비행선"),
    17: ("마케마케"),
    18: ("우주선 발전기금"),
    19: ("에리스"),
    20: ("이오"),
    21: ("Free Parking"),
    22: ("큰곰자리"),
    23: ("찬스"),
    24: ("판도라"),
    25: ("오베론"),
    26: ("북쪽 우주비행선"),
    27: ("아리엘"),
    28: ("히페리온"),
    29: ("무료 우주여행"),
    30: ("프로메테우스"),
    31: ("블랙홀로 가시오"),
    32: ("말머리성운"),
    33: ("태양"),
    34: ("우주선 발전기금"),
    35: ("수성"),
    36: ("동쪽 우주비행선"),
    37: ("찬스"),
    38: ("금성"),
    39: ("이용 감사료"),
    40: ("달")
}

# 찬스카드 종류 (위치 or 잃거나 얻는 연료나 자원, 출력텍스트)
chanceCards = {
	0: (10, "Go to Blackholl!"),
	1: (0, "Go to Earth!"),
	2: (random.randrange(0,41), "Go to Random!"),
	3: (20, "Go to Free Parking"),
	4: (3, "Get 3 fuel!"),
	5: (5, "Get 5 fuel!"),
	6: (50, "Get 50 resource!"),
	7: (100, "Get 100 resource!"),
	8: (-1, "Lose 1 fuel"),
	9: (-50, "Lose 50 resource")
}

# 커뮤니티 카드 종류 (잃거나 얻는 연료 or 자원, 출력텍스트)
communityCards = {
    0:(5,"Get 5 fuel!"),
    1:(7,"Get 7 fuel!"),
    2:(100,"Get 100 resource!"),
    3:(150,"Get 150 fuel!"),
    4:(-2,"Lose 2 fuel!"),
    5:(-3,"Lose 3 fuel!"),
    6:(-100,"Lose 100 resource!"),
    7:(150,"Lose 150 resource!"),

}

# 땅 정보 (연료소비, 자원획득) 
boardTile = {
    1: ("화성", -1, 15),
    3: ("세레스", -1, 20),
    6: ("목성", -1,40),
    8: ("토성", -1,60),
    9: ("천왕성", -1,50),
    12: ("해왕성", -2,90),
    14: ("명왕성", -2,80),
    15: ("하우메아", -2,100),
    17: ("마케마케", -2,110),
    19: ("에리스", -2,85),
    20: ("이오", -2,95),
    22: ("큰곰자리", -3,100),
    24: ("판도라", -3,110),
    25: ("오베론", -3,95),
    27: ("아리엘", -3,105),
    28: ("히페리온", -3,103),
    30: ("프로메테우스", -3,107),
    32: ("말머리성운", -4,120),
    33: ("태양", -4,125),
    35: ("수성", -4,130),
    38: ("금성", -4,134),
    40: ("달", -4,137)
}

# Dice를 굴리는 함수
def rollDice():
    return random.randrange(1, 13)

class Game:
    def __init__(self, turns, cards, freeSpaceTravel, autoExploration):
        self.turns = turns
        self.cards = cards
        self.freeSpaceTravel = freeSpaceTravel
        self.autoExploration = autoExploration
        self.playerPos = 0
        self.fuel = 20
        self.resource = 20

        self.hits = [0]*41
        self.wins = False

    def run(self):
        # 찬스칸에 도착했을 경우
        if self.playerPos in chanceTile:
            if self.cards:
                chanceNum = random.randrange(0, 10)
                if chanceNum == 0:
                    self.playerPos = 10
                elif chanceNum == 1:
                    self.playerPos = 0
                elif chanceNum == 2:
                    self.playerPos = random.randrange(0, 41)
                elif chanceNum == 3:
                    self.playerPos = 20
                elif chanceNum == 4:
                    self.fuel += 3
                elif chanceNum == 5:
                    self.fuel += 5
                elif chanceNum == 6:
                    self.resource += 50
                elif chanceNum == 7:
                    self.resource += 100
                elif chanceNum == 8:
                    self.fuel -= 1
                elif chanceNum == 9:
                    self.resource -= 50

        #우주선 발전기금칸에 도착했을 경우
        elif self.playerPos in communityTile:
            if self.cards:
                communityNum = random.randrange(0,8)
                if communityNum == 0:
                    self.fuel += 5
                elif communityNum == 1:
                    self.fuel +=7
                elif communityNum == 2:
                    self.resource +=100
                elif communityNum == 3:
                    self.resource +=150
                elif communityNum == 4:
                    self.fuel -= 2
                elif communityNum == 5:
                    self.resource -=3
                elif communityNum == 6:
                    self.resource -=100
                elif communityNum == 7:
                    self.resource -150

        #이용 감사료칸에 도착했을 경우
        elif self.playerPos in thanksFee:
            if self.autoExploration:
                self.resource -= 200
        #행성에 도착했을 경우
        elif self.playerPos in boardTile:
            if self.autoExploration:
                self.fuel += boardTile[self.playerPos][1]
                self.resource += boardTile[self.playerPos][2]
        #무료 우주여행칸에 도착할경우    
        elif self.playerPos in freeTravel:
            if self.freeSpaceTravel:
                self.playerPos=random.randrange(0,40)
        #우주비행선 칸에 도착했을경우
        elif self.playerPos in spaceCraft:
            if self.autoExploration:
                self.fuel += 3
        # 파킹칸에 도착했을경우
        elif self.playerPos in freeParking:
            if self.autoExploration:
                self.resource += 100

        #블랙홀로 이동   
        if self.playerPos == 30:
            self.playerPos = 10
            if self.autoExploration:
                self.fuel -= 5

        #주사위를 굴려 블랙홀 칸에 도착한 경우
        if self.playerPos == 10:
            if self.autoExploration:
                self.fuel -=5
            
        notMovePlayerPos = self.playerPos

        self.playerPos += rollDice()
        self.turns -= 1

        if notMovePlayerPos < 11 and self.playerPos >= 11:
            self.playerPos += 1

        if self.playerPos > 40:
            self.playerPos -= 41
            #self.turns -= 1
            self.fuel += 10

        self.hits[self.playerPos] += 1
        
        if self.resource >= 1000:
            self.wins = True
            return
        elif self.turns <= 0:
            self.wins = False
            return
        else:
            self.run()
