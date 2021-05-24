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

#To show the hand of the current player
def showHand(player, playerHand):
	print("It's {}'s turn".format(player))
	print("Your Hand:")
	print("---------------------------------")
	y = 1
	for card in playerHand:
		print("{}) {}".format(y, card))
		y += 1
	print("")


#Main function
unoDeck = buildDeck()
random.shuffle(unoDeck)
discards = [] #List of discards
players = [] #List of cards for all players
playerNames = [] #Names of players

#Getting players names and assigning five cards to each player
numPlayers = int(input("How many players? "))
for i in range(numPlayers):
	name = input("Enter player name: ")
	playerNames.append(name)
	players.append(drawCards(5))

#Printing out the cards assigned to each player
print("\nThe cards are: ")
for (name, cards) in zip(playerNames, players):
	print("Player {} has {}".format(name, cards))
print("")

#Setting up the game
playerTurn = 0
playDirection = 1
playing = True
winner = ""

discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColour = splitCard[0]
if currentColour != "Wild":
	cardVal = splitCard[1]
else:
	cardVal = "Any"


#Main loop
while playing:
	showHand(playerNames[playerTurn], players[playerTurn])
	break
