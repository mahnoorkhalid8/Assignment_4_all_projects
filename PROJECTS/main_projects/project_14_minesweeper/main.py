import random
import re

# lets create a board object to represent the minesweeper game
#  this is sp that we can just say "create a new board object" or "dig here" or "render this game for this object"

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()         # plant the bomb
        self.assign_values_to_board()              # assign values to the board
        
        # initialize a set to keep track of which locations we have uncovered, we will save (roe, col) tuples inot this set
        self.dug = set()
        
    def make_new_board(self):
        # construct a new board based on the dim size and num bombs, we should construct the list of lists here
        # (or whatever representation you prefer but since we have a 2D board, list of lists is most natural)
        
        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)] 
        # this creates an array like this:
        # [[None, None, ..... , None],
        #  [None, None, ..... , None],  
        #  [...                     ],
        #  [None, None, ..... , None]]
        # we can see how this represents a board!
        
        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)     # returns a random number between N  such that a <= N <= b
            row = loc // self.dim_size           # we want the number of items dim_size goes into loc to tell us what row to look at
            col = loc % self.dim_size            # we want the remainder to tell us what index in that row to look at
           
            if board[row][col] == '*':
                # this means we have actually planted a bomb there already so keep going
                continue
            
            board[row][col] = '*'          # plant the bomb
            bombs_planted += 1
            
        return board
    
    def assign_values_to_board(self):
        # now that we have the bommbs planted, let's assign a number 0-8 for all the empty spaces which represents how many neighbouring bombs
        # there are, we can precompute these and it'll save us some effort checking what's around the board later on:
        
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomd, we don't want to calculate anything
                    continue
                # this means we are at an empty space, let's check how many bombs are around it
                self.board[r][c] = self.get_num_neighbouring_bombs(r, c)
                
    def get_num_neighbouring_bombs(self, row, col):
        # let's iterate through all the neighbouring positions and sun number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # middle left: (row, col-1)
        # middle right: (row, col+1)    
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)   
        # bottom right: (row+1, col+1)
        
        # make sure to not out of bounds!
        
        num_neighbouring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
              
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1
                    
        return num_neighbouring_bombs
    
    def dig(self, row, col):
        # dig at that location! return True if successful dig, False if bomb dug
        
        # a few scenarios:
        # 1. dug a bomb -> game over
        # 2. gid at location with neighbouring bombs -> finish dig
        # 3. gid at location with no neighhbouring bombs -> recursively dig neighbours!
        
        self.dug.add((row, col))      # keep track of the location we dug
        
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        
        return True
    
    def __str__(self):
        # this is a magic function where if you call print this object, it'll print out what this function returns!Returns a string that shows the board to the playr
        
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
                    
        # put this together in a string
        string_rep = ""
        # get maximum column width for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key  = len)))
            
        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = "%-" + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += ' '.join(cells)
        indices_row += ' \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = "%-" + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'
            
        str_len = int(len(string_rep) / self.dim_size) 
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len
        
        return string_rep       
    
    # play the game

def play(dim_size=10, num_bombs=10):
    # step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)
        
    # step 2: show the player the board and ask for where they want to dig
    # step 3a: if location is a boomb, show game over message
    # step 3b: if location is not a bmb, dig recursively until each square is atleast next to a bomb
    # step 4: repeat steps 2 and 3a/3b until there are no more places to dig -> VICTORY!
    safe = True
        
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # 0,0 or 0, 0 or 0,    0
            
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))      #"0, 3"
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Oops, that's not even in the range! Try again")
            continue
            
        # if it's in range, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb
            break   # game over RIP
        
    # 2 ways to end loop, let's check whih one
    if safe:
        print("CONGRATULATIONS! YOU WON!")
    else:
        print("SORRY, GAME OVER!")
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)
            
if __name__ == '__main__':
    # play the game
    play()
        