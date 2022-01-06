class Board:
    def __init__(self):
        self
        #  الفاكشن دي معموله علشان ترسم الشكل بتاع ال board

    def drawBoard(board):
        # This function prints out the board that it was passed. Returns None.
        HLINE = '  +---+---+---+---+---+---+---+---+'
        VLINE = '  |   |   |   |   |   |   |   |   |'

        print('    1   2   3   4   5   6   7   8')
        print(HLINE)
        for y in range(8):
            print(VLINE)
            print(y+1, end=' ')
            for x in range(8):
                print('| %s' % (board[x][y]), end=' ')
            print('|')
            print(VLINE)
            print(HLINE)
# انما دي علشان تظهر البورد اليي بتكون موجوده اول ماللعبه تبدا

    def resetBoard(board):
        # Blanks out the board it is passed, except for the original starting position.
        for x in range(8):
            for y in range(8):
                board[x][y] = ' '

        # Starting pieces:
        board[3][3] = 'X'
        board[3][4] = 'O'
        board[4][3] = 'O'
        board[4][4] = 'X'
# انما دي بتعمل كريت لنيو بورد علشان بدا نستخدمها فس اكتر من مكان بعد كده

    def getNewBoard():
        # Creates a brand new, blank board data structure.
        board = []
        for i in range(8):
            board.append([' '] * 8)
        return board

    def getBoardCopy(board):
        # Make a duplicate of the board list and return the duplicate.
        dupeBoard = Board.getNewBoard()

        for x in range(8):
            for y in range(8):
                dupeBoard[x][y] = board[x][y]

        return dupeBoard
# دي الي بتححد اذا كا  المكان الي احنا بندور عليه ده في البور ولا بره 
    def isOnBoard(x, y):
        # Returns True if the coordinates are located on the board.
        return x >= 0 and x <= 7 and y >= 0 and y <= 7
