import random
from sys import stdout
from colorama import Fore

# Creates a new game
global WORD_SIZE
WORD_SIZE = 6
global NO_ROUNDS
NO_ROUNDS = 6


class Game:
    def __init__(self, word, noRounds):
        self.word = word
        self.noRounds = noRounds
        self.board = []
        self.guesses = []
        self.roundCounter = 0

    def initialize(self):
        for i in range(0, self.noRounds):
            self.board.append(["*", "*", "*", "*", "*", "*"])

    def showBoard(self):
        for line in self.board:
            for i in range(0, len(line)):
                if self.exactSamePosition(line[i], i):
                    print(Fore.GREEN + line[i], " ", end="")
                elif self.belongsToWord(line[i]):
                    print(Fore.YELLOW + line[i], " ", end="")
                else:
                    print(Fore.WHITE + line[i], " ", end="")
            print("\n")

    def belongsToWord(self, letter):
        if letter in self.word:
            return True
        else:
            return False

    def exactSamePosition(self, letter, position):
        if letter == self.word[position]:
            return True
        else:
            return False

    def addGuessToBoard(self, word):
        word_list = list(word)

        for i in range(0, len(word_list)):

            x = word_list[i]
            word_list[i] = x.upper()

        self.board[self.roundCounter] = word_list
        self.roundCounter += 1

    def isCorrect(self, word):
        if word == self.word:
            return True
        else:
            return False


# Creates a new guess for each round


class Guess(Game):
    def __init__(self, wordGuessed):
        self.wordGuessed = wordGuessed

    def isCorrect(self):
        pass


# Gets list of words from word_list file


def getWordList():
    list = []
    f = open("word_list.txt", "r")
    for line in f.readlines():
        word = ""
        for char in line:
            if char != "\n":
                if char.islower():
                    word += char.upper()
                else:
                    word += char
        list.append(word)

    return list


# picks a random word from the list of available words


def getRandomWord(list):
    return random.choice(list)


def inputWord():
    word = ""
    while len(word) != 6:
        word = input("Guess :")
        if len(word) != 6:
            print("Word must be ", str(WORD_SIZE), " characters long!!!")
    return word


def main():

    # initialize word list from file
    list = getWordList()

    # initialize game
    word = getRandomWord(list)
    wordle = Game(word, NO_ROUNDS)
    wordle.initialize()
    wordle.showBoard()

    # game interface

    while wordle.roundCounter < wordle.noRounds:
        guessedWord = inputWord().upper()
        wordle.addGuessToBoard(guessedWord)
        wordle.showBoard()
        if wordle.isCorrect(guessedWord):
            print(Fore.GREEN + "CORRECT!!!!")
            exit(0)

    print(Fore.RED + "You couldn't guess! The correct word was:", wordle.word)


if __name__ == "__main__":
    main()
