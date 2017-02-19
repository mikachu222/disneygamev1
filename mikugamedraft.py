# Series of question dictionaries with the question, choices, answer and difficulty level
QuestionDict1 = {"Question1": "Which ride would you find a basketball court?",
                "Choice1": ["A. Tennis", "B. Water Polo", "C. Soccer", "D. Kung Fu"],
                "Answer1": "B", "Difficulty1": "Easy"}

QuestionDict2 = {"Question2": "Which African statesman received the Freedom of the City of Cardiff in a ceremony in 1998?",
                "Choice2": ["A. Pele", "B. Nelson Mandela", "C. Barack Obama", "D. George Washington"],
                "Answer2": "B", "Difficulty1": "Easy"}

QuestionDict3 = {"Question3": "Which seven-a-side ball game is played in a swimming pool?",
                "Choice3": ["A. Tennis", "B. Water Polo", "C. Soccer", "D. Kung Fu"],
                "Answer3": "B", "Difficulty1": "Easy"}

QuestionDict4 = {"Question4": "Which seven-a-side ball game is played in a swimming pool?",
                "Choice4": ["A. Tennis", "B. Water Polo", "C. Soccer", "D. Kung Fu"],
                "Answer4": "B", "Difficulty1": "Medium"}

QuestionDict5 = {"Question5": "Which seven-a-side ball game is played in a swimming pool?",
                "Choice5": ["A. Tennis", "B. Water Polo", "C. Soccer", "D. Kung Fu"],
                "Answer5": "B", "Difficulty1": "Medium"}

QuestionDict6 = {"Question6": "Which seven-a-side ball game is played in a swimming pool?",
                "Choice6": ["A. Tennis", "B. Water Polo", "C. Soccer", "D. Kung Fu"],
                "Answer6": "B", "Difficulty1": "Medium"}

QuestionDict7 = {"Question7": "What would you find in a formicary?",
                "Choice7": ["A. Elephants", "B. Cats", "C. Ants", "D. Tigers"],
                "Answer7": "B", "Difficulty1": "Medium"}

QuestionDict8 = {"Question8": "Which seven-a-side ball game is played in a swimming pool?",
                "Choice8": ["A. Tennis", "B. Water Polo", "C. Soccer", "D. Kung Fu"],
                "Answer8": "B", "Difficulty1": "Hard"}

QuestionDict9 = {"Question9": "Which seven-a-side ball game is played in a swimming pool?",
                "Choice9": ["A. Tennis", "B. Water Polo", "C. Soccer", "D. Kung Fu"],
                "Answer9": "B", "Difficulty1": "Hard"}

QuestionDict10 = {"Question10": "Which seven-a-side ball game is played in a swimming pool?",
                "Choice10": ["A. Tennis", "B. Water Polo", "C. Soccer", "D. Kung Fu"],
                "Answer10": "B", "Difficulty1": "Hard"}

#Dollar value of every round
ValuesDict = {"Round0": 0, "Round1": 100, "Round2": 200, "Round3": 500, "Round4": 1000, "Round5": 5000,
             "Round6": 10000, "Round7": 100000, "Round8": 250000, "Round9": 500000,
             "Round10": 1000000}

CurrentBalance = ValuesDict["Round0"]

#Welcome the user to the game
print "Welcome to 'Who Wants to be a Millionaire!' the Disneyland edition. Let's play!"
print """
______________$$$$$$$
_____________$$$$$$$$$
____________$$$$$$$$$$$
____________$$$$$$$$$$$
____________$$$$$$$$$$$
_____________$$$$$$$$$
_____$$$$$$_____$$$$$$$$$$
____$$$$$$$$__$$$$$$_____$$$
___$$$$$$$$$$$$$$$$_________$
___$$$$$$$$$$$$$$$$______$__$
___$$$$$$$$$$$$$$$$_____$$$_$
___$$$$$$$$$$$__________$$$_$_____$$
____$$$$$$$$$____________$$_$$$$_$$$$
______$$$__$$__$$$______________$$$$
___________$$____$_______________$
____________$$____$______________$
_____________$$___$$$__________$$
_______________$$$_$$$$$$_$$$$$
________________$$____$$_$$$$$
_______________$$$$$___$$$$$$$$$$
_______________$$$$$$$$$$$$$$$$$$$$
_______________$$_$$$$$$$$$$$$$$__$$
_______________$$__$$$$$$$$$$$___$_$
______________$$$__$___$$$______$$$$
______________$$$_$__________$$_$$$$
______________$$$$$_________$$$$_$_$
_______________$$$$__________$$$__$$
_____$$$$_________$________________$
___$$$___$$______$$$_____________$$
__$___$$__$$_____$__$$$_____$$__$$
_$$____$___$_______$$$$$$$$$$$$$
_$$_____$___$_____$$$$$_$$___$$$
_$$_____$___$___$$$$____$____$$
__$_____$$__$$$$$$$____$$_$$$$$
__$$_____$___$_$$_____$__$__$$$$$$$$$$$$
___$_____$$__$_$_____$_$$$__$$__$______$$$
____$$_________$___$$_$___$$__$$_________$
_____$$_$$$$___$__$$__$__________________$
______$$____$__$$$____$__________________$
_______$____$__$_______$$______________$$
_______$$$$_$$$_________$$$$$$$__$$$$$$
__________$$$_________________$$$$$
"""

# #Display the question and choices from game_question and prompts the player for an answer
print QuestionDict1["Question1"]
print QuestionDict1["Choice1"]
print "Your current balance is $%s." % (CurrentBalance)
print "This one's for $%s. What is your answer: A, B, C, or D?" % (ValuesDict["Round1"])
PlayerAnswer1 = raw_input()

#If statement that determines if the player's answer is correct.
#If yes, add money to their winnings balance and print the new value.
#If not, print the balance and exit the game.

if str.upper(PlayerAnswer1) == QuestionDict1["Answer1"]:
    NewBalance = ValuesDict["Round1"] + CurrentBalance
    print NewBalance
else:
    print "You still walk away with $%s!" % (ValuesDict["Round1"])
