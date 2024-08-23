from random import choice
import sys


# OOP version:
class RPS:
    def __init__(self):
        print('Welcome to our RPS game!')

        self.score = [0, 0]

        self.moves = {
            'rock': '🪨',
            'paper': '🗞️',
            'scissors': '✂️',
        }

        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_choice = input('Rock, paper, scissors, GO! >> ').lower()

        if user_choice == 'exit':
            print('Thanks for playing!')
            sys.exit()

        if user_choice not in self.valid_moves:
            print('Invalid choice, try again.')
            return self.play_game

        ai_choice = choice(self.valid_moves)

        self.display_moves(user_choice, ai_choice)
        self.check_results(user_choice, ai_choice)

    def display_moves(self, user_choice, ai_choice):
        print("------")
        print(f"You chose {self.moves[user_choice]}")
        print(f"AI chose {self.moves[ai_choice]}")
        print("------")

    def check_results(self, user_choice, ai_choice):
        if user_choice == ai_choice:
            print("it's a tie!")
            print(f"The score is: You {self.score[0]} : AI {self.score[1]}")
        elif user_choice == 'rock' and ai_choice == 'scissors':
            self.score[0] += 1
            print("You win!")
            print(f"The score is: You {self.score[0]} : AI {self.score[1]}")
        elif user_choice == 'paper' and ai_choice == 'rock':
            self.score[0] += 1
            print("You win!")
            print(f"The score is: You {self.score[0]} : AI {self.score[1]}")
        elif user_choice == 'scissors' and ai_choice == 'paper':
            self.score[0] += 1
            print("You win!")
            print(f"The score is: You {self.score[0]} : AI {self.score[1]}")
        else:
            self.score[1] += 1
            print('AI wins!')
            print(f"The score is: You {self.score[0]} : AI {self.score[1]}")

if __name__ == "__main__":
    rps = RPS()

    while True:
        rps.play_game()


# Without OOP:
#
# def play_game():
#     print("Welcome! Excited to play RPS?!")
#     score = [0, 0]
#     game_is_on = True
#     while game_is_on:
#         valid_moves = ['rock', 'paper', 'scissors']
#         ai_rps = choice(valid_moves)
#         user_choice = input('Choose rock, paper, or scissors: ').lower()
#         if user_choice not in valid_moves:
#             print('Please make a valid choice.')
#         elif user_choice == 'exit':
#             print(f"""Thanks for playing!
# the final score is {score}""")
#             game_is_on = False
#             return
#         elif ai_rps == user_choice:
#             print(f"""You chose {user_choice}
# AI chose {ai_rps}
# It is a tie!
# The score is {score}""")
#         elif ai_rps == 'rock' and user_choice == 'scissors':
#             score[0] += 1
#             print(f"""You chose {user_choice}
# AI chose {ai_rps}
# AI wins!!
# The score is {score}""")
#         elif ai_rps == 'rock' and user_choice == 'paper':
#             score[1] += 1
#             print(f"""You chose {user_choice}
# AI chose {ai_rps}
# You win!!
# The score is {score}""")
#         elif ai_rps == 'scissors' and user_choice == 'rock':
#             score[1] += 1
#             print(f"""You chose {user_choice}
# AI chose {ai_rps}
# You win!!
# The score is {score}""")
#         elif ai_rps == 'scissors' and user_choice == 'paper':
#             score[0] += 1
#             print(f"""You chose {user_choice}
# AI chose {ai_rps}
# AI wins!!
# The score is {score}""")
#         elif ai_rps == 'paper' and user_choice == 'rock':
#             score[0] += 1
#             print(f"""You chose {user_choice}
# AI chose {ai_rps}
# AI wins!!
# The score is {score}""")
#         elif ai_rps == 'paper' and user_choice == 'scissors':
#             score[1] += 1
#             print(f"""You chose {user_choice}
# AI chose {ai_rps}
# You win!!
# The score is {score}""")
#
#
#
# if __name__ == "__main__":
#     play_game()