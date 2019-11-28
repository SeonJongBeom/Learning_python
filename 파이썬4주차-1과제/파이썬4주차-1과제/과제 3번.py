####
#과제 3번, 카드 출력하기

class Card:
	def __init__(self):
		self.card_type = ["클럽", "다이아몬드", "하트", "스페이드"]
		self.number = ["에이스"]
		for i in range(2, 11):
			self.number.append(str(i))
		self.number.append("잭")
		self.number.append("퀸")
		self.number.append("킹")

class Deck(Card):
	type_cnt = -1
	number_cnt = -1

	def __init__(self):
		super().__init__()
		self.deck = []
		self.tmp = ""

	def deck_add(self):
		for i in range(4):
			for j in range(13):
				self.tmp = self.card_type[i] + " " + self.number[j]
				self.deck.append(self.tmp)

	def getDeck(self):
		return self.deck

card = Deck()
card.deck_add()
print(card.getDeck())