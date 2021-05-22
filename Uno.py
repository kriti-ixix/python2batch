#Importing the libraries
import random

#User defined functions
#To generate the deck of cards
def buildDeck():
	deck = []
	colours = ["Red", "Green", "Yellow", "Blue"]
	values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
	wilds = ["Wild", "Wild Draw Four"]

	for colour in colours:
		for value in values:
			cardVal = "{} {}".format(colour, value)
			deck.append(cardVal)
			if value != 0:
				deck.append(cardVal)

	for i in range(4):
		deck.append(wilds[0])
		deck.append(wilds[1])

	return deck 

#To draw numCards from the deck
def drawCards(numCards):
	cardsDrawn = [unoDeck.pop(0) for i in range(numCards)]
	'''
	for i in range(numCards):
		cardsDrawn.append(unoDeck.pop(0))
	'''
	return cardsDrawn

#Main function
unoDeck = buildDeck()
print("")
print(unoDeck)
random.shuffle(unoDeck)
print("")
print(unoDeck)
print("Cards drawn:")
print(drawCards(5))
print("\n", unoDeck)
players = []