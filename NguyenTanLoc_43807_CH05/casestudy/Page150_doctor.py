"""
Author: Nguyen Tan Loc
Date: 7/10/2021
Problem:
Generates and displays sentences using at simple grammar and vocabulary. Words are chosen at random.
Solution:

    ....
"""
import random

# Vocabulary:
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def sentence():
        """Builds and returns a sentence."""
        return nounPhrase() + " " + verbPhrase()
def nounPhrase():
        """Builds and returns a noun phrase."""
        return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
        """Builds and returns a verb phrase."""
        return random.choice(verbs) + " " + nounPhrase() + " " + \
               prepositionalPhrase()
def prepositionalPhrase():
        """Builds and returns a prepositional phrase."""
        return random.choice(prepositions) + " " + nounPhrase()
def main():
        """Allows the user to input the number of sentencesto generate."""
number = int(input("Enter the number of sentences: "))
for count in range(number):
        print(sentence())
# The entry point for program execution
if __name__ == "__main__":
        main()