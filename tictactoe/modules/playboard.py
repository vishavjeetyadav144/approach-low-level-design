from modules.cell import Cell


class PlayBoard:

    def __init__(self, player1, player2) -> None:
        self.board = [[Cell() for _ in range(3)] for _ in range(3)]
        self.player1 = player1
        self.player2 = player2

    def print_board(self):
        print('\n')
        for i in self.board:
            for j in i:
                if j.value == None:
                    print("*", end= '  ')
                else:
                    print(j.value.symbol, end ='  ')
            print('\n\n')

    def check_winner(self):

        for row in self.board:
            if (row[0].value is not None and row[1].value is not None and row[2].value is not None) and row[0].value.symbol == row[1].value.symbol == row[2].value.symbol :
                return row[0].value
        
        for col in range(3):
            if (self.board[0][col].value is not None and self.board[1][col].value is not None and self.board[2][col].value is not None) and self.board[0][col].value.symbol == self.board[1][col].value.symbol == self.board[2][col].value.symbol:
                return self.board[0][col].value
        
        if (self.board[0][0].value is not None and self.board[1][1].value is not None and self.board[2][2].value is not None) and self.board[0][0].value.symbol == self.board[1][1].value.symbol == self.board[2][2].value.symbol:
            return self.board[0][0].value 

        if (self.board[0][2].value is not None and self.board[1][1].value is not None and self.board[2][0].value is not None) and self.board[0][2].value.symbol == self.board[1][1].value.symbol == self.board[2][0].value.symbol:
            return self.board[0][2].value 
        
        for row in self.board:
            for cell in row:
                if cell.value is None:
                    return None

        return "Tie"     
        
    def update_board(self, x, y, player):
        self.board[x][y] = Cell(player)
        return self.check_winner()


        
        
        





