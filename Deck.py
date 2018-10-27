import random as rand

from Card import Card

numSuits = 4
minRank = 2
maxRank = 15

class Deck:
	def __init__(self):
		self.deck = []
		self.deck.append(Card(2, 0))#club 2
		self.deck.append(Card(2, 3))#heart 2
		for suit in range(0,numSuits):
			for rank in range(minRank+1,maxRank):
				self.deck.append(Card(rank, suit))

	def __str__(self):
		deckStr = ''
		for card in self.deck:
			deckStr += card.__str__() + '\n'
		return deckStr

	def shuffle(self):
		rand.shuffle(self.deck, rand.random)
                #self.deck=self.deck# for debug

	def deal(self):
		return self.deck.pop(0)

	def sort(self):
		self.deck.sort()

	def size(self):
		return len(self.deck)

	def addCards(cards):
		self.deck += cards
