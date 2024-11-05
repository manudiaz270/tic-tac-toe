class Board:
    current_player = 'O'
    move_count = 0
    board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    def display_board(self):
        display_string = '0  1  2 \n'
        for idx, row in enumerate(self.board):
            for i in row:
                if not i:
                    char = ' '
                elif i == 1:
                    char = 'X'
                else:
                    char = 'O'
                display_string += f'{char} |'
            display_string += f'{idx}\n'

        return display_string
    
    def update_board(self, move):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        y, x = list(move)
        if int(y) > 2 or int(x) > 2:
            return 'invalid move'
        if self.board[int(y)][int(x)]:
            return 'space already occupied'
        
        self.move_count += 1
        if self.current_player == 'X':
            val = 1
        else:
            val = 10
        self.board[int(y)][int(x)] = val
        
    def sum_diagonals(self):
        principal = 0
        secondary = 0
        for i in range(3):
            for j in range(3):
                if i == j:
                    principal += self.board[i][j]
                
                if (i + j) == 2:
                    secondary += self.board[i][j]
        
        return (principal, secondary)



    def game_status(self):
        for row in self.board:
            total = 0
            for i in row:
                total += i
            if total == 3 or total == 30:
                return 1
        
        for x in range(3):
            total = 0
            for y in range(3):
                total += self.board[y][x]
            if total == 3 or total == 30:
                return 1
            

        if (3 or 30) in self.sum_diagonals():
            return 1
        

        
        if self.move_count == 9:
            return 2
        
        return 0
        



board = Board()
