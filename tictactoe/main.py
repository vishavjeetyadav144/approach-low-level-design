from modules.playboard import PlayBoard
from modules.players import Player

if __name__ == "__main__":
    print("--- Welcome to tic tac toe game ----- \n")


    player_1_name = input("Player 1 name - ")
    player_1_symbol = input("Player 1 symbol - ")
    player_1 = Player(player_1_name, player_1_symbol)

    player_2_name = input("Player 2 name - ")
    player_2_symbol = input("Player 2 symbol - ")
    player_2 =  Player(player_2_name, player_2_symbol)



    playboard = PlayBoard(player_1, player_2)

    i = 0 
    while True:

        playboard.print_board()
        response = None
        if i == 0:
            x,y = map(int, input("player 1 enter coordinate ex (1,1)- ").split(','))
            response = playboard.update_board(x,y, player_1)
            i += 1
        else:
            x,y = map(int, input("player 2 enter coordinate ex (1,1)- ").split(','))
            response = playboard.update_board(x,y, player_2)
            i -= 1
        if response == "Tie":
            print("---Match Draw ----")
            break
        elif response is not None:
            print(f'{response.name} won this match')
            break

        
        

    

    