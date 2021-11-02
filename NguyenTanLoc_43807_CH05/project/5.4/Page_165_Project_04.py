"""
Author: Nguyen Tan Loc
Date: 7/10/2021
Problem:
Make the following modifications to the original sentence-generator program:
a. The prepositional phrase is optional. (It can appear with a certain
probability.)
b. A conjunction and a second independent clause are optional: The boy took a
drink and the girl played baseball.
c. An adjective is optional: The girl kicked the red ball with a sore foot.
You should add new variables for the sets of adjectives and conjunctions.

Solution:

    ....
"""
import random
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BASEBALL", "BALL","FOOT")
verbs = ("DRINK","PLAY","KICKED")
prepositions = ("WITH", "BY")
adjective=("RED","BLUE")
def sentence():
        return nounPhrase() + " " + verbPhrase()
def nounPhrase():
        return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
        return random.choice(verbs) + " " + nounPhrase() + " " + \
               prepositionalPhrase()
def adjectivePhase():
    return random.choice(articles) + " " + random.choice(adjective)
def prepositionalPhrase():
        return random.choice(prepositions) + " " + nounPhrase()

def main():
 number = int(input("Enter the number of sentences: "))
for count in range(1):
        print(sentence())
if __name__ == "__main__":
    main()