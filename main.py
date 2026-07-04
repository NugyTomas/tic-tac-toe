from random import randrange

INITIAL_BOARD = ["1", "2", "3",
                 "4", "5", "6",
                 "7", "8", "9"]

BOARD = INITIAL_BOARD.copy()

YODA_ASCII = r'''
                    ____
                 _.' :  `._
             .-.'`.  ;   .'`.-.
    __      / : ___\ ;  /___ ; \      __
  ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
       `:-.._J '-.-'L__ `-- ' L_..-;'
         "-.__ ;  .-"  "-.  : __.-"
             L ' /.------.\ ' J
              "-.   "--"   .-"
             __.l"-:_JL_;-";.__
          .-j/'.;  ;""""  / .'\"-.
        .' /:`. "-.:     .-" .';  `.
     .-"  / ;  "-. "-..-" .-"  :    "-.
  .+"-.  : :      "-.__.-"      ;-._   \
  ; \  `.; ;                    : : "+. ;
  :  ;   ; ;                    : ;  : \:
 : `."-; ;  ;                  :  ;   ,/;
  ;    -: ;  :                ;  : .-"'  :
  :\     \  : ;             : \.-"      :
   ;`.    \  ; :            ;.'_..--  / ;
   :  "-.  "-:  ;          :/."      .'  :
     \       .-`.\        /t-""  ":-+.   :
      `.  .-"    `l    __/ /`. :  ; ; \  ;
        \   .-" .-"-.-"  .' .'j \  /   ;/
         \ / .-"   /.     .'.' ;_:'    ;
          :-""-.`./-.'     /    `.___.'
                \ `t  ._  /  
                 "-.t-._:'
'''

WINNING_COMBINATIONS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def greet_players():
    print(YODA_ASCII)
    print("Hmm... Tic Tac Toe, play you wish?")

def print_board():
    print(f"""
             {BOARD[0]} | {BOARD[1]} | {BOARD[2]}
            ---------
             {BOARD[3]} | {BOARD[4]} | {BOARD[5]}
            ---------
             {BOARD[6]} | {BOARD[7]} | {BOARD[8]}
            """)

def choose_game_mode():
    while True:
        game = input("Singleplayer or Multiplayer, choose you must. (S/M): ").upper()
        if game in ("S", "M"):
            return game

        print("\nWrong input, that is. Try again, you must:\n")

def choose_symbol(prompt):
    while True:
        first_symbol = input(prompt).upper()
        if first_symbol in ("X", "O"):
            second_symbol = "O" if first_symbol == "X" else "X"
            return first_symbol, second_symbol

        print("\nWrong input, that is. Try again, you must:\n")

def player_turn(symbol):
    while True:
        players_choice = input("Your next move, choose: ").strip()
        if players_choice in BOARD:
            index = BOARD.index(players_choice)
            BOARD[index] = symbol
            return

        print("\nWrong input, that is. Try again, you must: \n")

def computer_turn(symbol):
    print("The computer's turn, it is.")
    while True:
        computers_choice = str(randrange(1, 10))
        if computers_choice in BOARD:
            index = BOARD.index(computers_choice)
            BOARD[index] = symbol
            return

def check_winner():
    return any(BOARD[a] == BOARD[b] == BOARD[c] for a, b, c in WINNING_COMBINATIONS)

def check_draw():
    return not any(position.isdigit() for position in BOARD)

def end_turn(win_message):
    print_board()

    if check_winner():
        print(win_message)
        return True

    if check_draw():
        print("A draw, this game is!")
        return True

    return False

def play_singleplayer():
    players_symbol, computers_symbol = choose_symbol(
        "Choose your symbol, you must. X or O?: "
    )

    if players_symbol == "O":
        print("First move, the computer has made.!")
        computer_turn(computers_symbol)
    print_board()

    while True:
        player_turn(players_symbol)
        if end_turn("Victory, yours it is! Congratulations, hmm!"):
            return

        computer_turn(computers_symbol)
        if end_turn("Won, the computer has. Better luck next time, you will have."):
            return

def play_multiplayer():
    player1_symbol = "X"
    player2_symbol = "O"

    print_board()
    while True:
        print("Player 1's turn, it is.")
        player_turn(player1_symbol)
        if end_turn("Victory, yours it is, Player 1! Well done, you have."):
            return

        print("Player 2's turn, it is.")
        player_turn(player2_symbol)
        if end_turn("Won, you have, Player 2! Strong with the Force, you are."):
            return


greet_players()

play_game = True
while play_game:
    game_mode = choose_game_mode()

    if game_mode == "S":
        play_singleplayer()
    else:
        play_multiplayer()

    while True:
        restart = input("Play again, do you wish? (Y/N): ").upper()
        if restart in ("Y", "N"):
            if restart == "Y":
                BOARD = INITIAL_BOARD.copy()
                break
            else:
                play_game = False
                break
        print("\nWrong input, that is. Try again, you must! \n")

