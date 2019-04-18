import requests
import random
import re
from bs4 import BeautifulSoup
from os import system, name
from time import sleep

def main():
	#clear screen and welcome
	clear()
	print("Welcome to Hangman!")
	sleep(1)
	print("You will be given 6 wrong guesses before you kill the man.")
	sleep(1)
	ready = input("Are you ready to begin? (yes) (no)\n")
	#choose category once ready
	if(ready=="yes"):
		
		chooseCategory()
	else:
		clear()
		main()

def chooseCategory():
	clear()
	#user input category chosen
	category = input("Choose a category: (animals) (body) (months) (clothes) (food) (holidays) (music) (sports)\n")
	clear()	
	getWordList(category)

def getWordList(category):
	#use BeautifulSoup to get words from website given the category chosen
	page_link = "http://www.manythings.org/vocabulary/lists/c/words.php?f="+category
	page_response = requests.get(page_link)
	page_content = BeautifulSoup(page_response.content, "html.parser")
	page_body = page_content.find_all('body')
	words = page_body[0].find_all('li')
	
	f = open('wordList.txt', 'w')

	for i in range(len(words)):
		word = words[i]
		f.write(str(word)[4:(len(word)-6)].lower() + "\n")
	f.close()

	chooseWord()

def chooseWord():
	#choose word from list given category
	word = random.choice(list(open('wordList.txt')))
	hangman(word[:(len(word)-1)])

def hangman(word):
	wordGuessed = False
	unguessedPhrase = ""
	guessedLetters = ""
	wrongGuesses = 0
	for i in range(len(word)):
		if word[i] == " ":
			unguessedPhrase += " "
		elif word[i] == "'":
			unguessedPhrase += "'"
		else:
			unguessedPhrase += "_"
	while wordGuessed != True:
		printLayout(guessedLetters, unguessedPhrase, len(word), wrongGuesses, word)
		letterGuessed = input("Please type your next guess.")
		guessedLetters += letterGuessed
		if letterGuessed in word:
			locations = [m.start() for m in re.finditer(letterGuessed, word)]
			temp = list(unguessedPhrase)
			for i in locations:
				temp[i] = letterGuessed
			unguessedPhrase = "".join(temp)
			if unguessedPhrase == word:
				wordGuessed = True
		else:
			wrongGuesses += 1
	printLayout(guessedLetters, unguessedPhrase, len(word), wrongGuesses, word)
	print("You won! The word was " + word)
	playAgain = input("Would you like to play again? (yes) (no)")
	if playAgain == "yes":
		chooseCategory()
	else:
		clear()
		exit()


def printLayout(guessedLetters, unguessedPhrase, wordLength, wrongGuesses, word):
	clear()
	if wrongGuesses == 0:
		print("   ____")
		print("  |    |     Guessed Letters: " + guessedLetters)
		print("  |          Word Length: " + str(wordLength))
		print("  |  ")
		print("  |  ")
		print("  |  ")
		print(" _|_")
		print("|   |")
		print("|   |_____")
		print("|         |")
		print("|_________|")
		print("")
		print("Phrase: " + unguessedPhrase)
	elif wrongGuesses == 1:
		print("   ____")
		print("  |    |     Guessed Letters: " + guessedLetters)
		print("  |    O     Word Length: " + str(wordLength))
		print("  |  ")
		print("  |   ")
		print("  |  ")
		print(" _|_")
		print("|   |")
		print("|   |_____")
		print("|         |")
		print("|_________|")
		print("")
		print("Phrase: " + unguessedPhrase)
	elif wrongGuesses == 2:
		print("   ____")
		print("  |    |     Guessed Letters: " + guessedLetters)
		print("  |    O     Word Length: " + str(wordLength))
		print("  |    |")
		print("  |   ")
		print("  |  ")
		print(" _|_")
		print("|   |")
		print("|   |_____")
		print("|         |")
		print("|_________|")
		print("")
		print("Phrase: " + unguessedPhrase)
	elif wrongGuesses == 3:
		print("   ____")
		print("  |    |     Guessed Letters: " + guessedLetters)
		print("  |    O     Word Length: " + str(wordLength))
		print("  |   /|")
		print("  |    ")
		print("  |    ")
		print(" _|_")
		print("|   |")
		print("|   |_____")
		print("|         |")
		print("|_________|")
		print("")
		print("Phrase: " + unguessedPhrase)
	elif wrongGuesses == 4:
		print("   ____")
		print("  |    |     Guessed Letters: " + guessedLetters)
		print("  |    O     Word Length: " + str(wordLength))
		print("  |   /|\\")
		print("  |   ")
		print("  |    ")
		print(" _|_")
		print("|   |")
		print("|   |_____")
		print("|         |")
		print("|_________|")
		print("")
		print("Phrase: " + unguessedPhrase)
	elif wrongGuesses == 5:
		print("   ____")
		print("  |    |     Guessed Letters: " + guessedLetters)
		print("  |    O     Word Length: " + str(wordLength))
		print("  |   /|\\")
		print("  |    |")
		print("  |   ")
		print(" _|_")
		print("|   |")
		print("|   |_____")
		print("|         |")
		print("|_________|")
		print("")
		print("Phrase: " + unguessedPhrase)
	elif wrongGuesses == 6:
		print("   ____")
		print("  |    |     Guessed Letters: " + guessedLetters)
		print("  |    O     Word Length: " + str(wordLength))
		print("  |   /|\\")
		print("  |    |")
		print("  |   / ")
		print(" _|_")
		print("|   |")
		print("|   |_____")
		print("|         |")
		print("|_________|")
		print("")
		print("Phrase: " + unguessedPhrase)
	else:
		print("   ____")
		print("  |    |     Guessed Letters: " + guessedLetters)
		print("  |    O     Word Length: " + str(wordLength))
		print("  |   /|\\")
		print("  |    |")
		print("  |   / \\")
		print(" _|_")
		print("|   |")
		print("|   |_____")
		print("|         |")
		print("|_________|")
		print("")
		print("Phrase: " + unguessedPhrase)
		print("Oh no! You guessed wrong too many time!")
		print("The word was " + word)
		tryAgain = input("Would you like to try again? (yes) (no)")
		if tryAgain == "yes":
			chooseCategory()
		else:
			clear()
			exit()



def clear():
	if name == "nt":
		system("cls")
	else:
		system("clear")

main()
