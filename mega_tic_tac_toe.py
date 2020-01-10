try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()
canvas = Canvas(root,width=450,height=450)
canvas.pack()

class Tile:
    def __init__(self):
        self.value = ''

class Board:
    def __init__(self):
        self.tiles = [[Tile(),Tile(),Tile()],
                      [Tile(),Tile(),Tile()],
                      [Tile(),Tile(),Tile()]]
        self.winner = ''

class Mega_Board:
    def __init__(self):
        self.boards = [[Board(),Board(),Board()],
                       [Board(),Board(),Board()],
                       [Board(),Board(),Board()]]
        self.winner = ''
        self.available_board = 'any'
        self.turn = 'x'

mouse_x = 0
mouse_y = 0
clicking = False

turn = 'x'

text = ''

winner = None

win_line = [[0,0],[0,0]]

def draw_x(x,y):
    canvas.create_line(x-20,y-20,x+20,y+20,width=4)
    canvas.create_line(x-20,y+20,x+20,y-20,width=4)

def draw_o(x,y):
    canvas.create_oval(x-30,y-30,x+30,y+30,width=4)

def has_won(player, b):
    if b[0][0] == player:
        if b[0][1] == player:
            if b[0][2] == player:
                return True,0,0,0,2
        if b[1][0] == player:
            if b[2][0] == player:
                return True,0,0,2,0
        if b[1][1] == player:
            if b[2][2] == player:
                return True,0,0,2,2
    if b[2][0] == player:
        if b[1][1] == player:
            if b[0][2] == player:
                return True,2,0,0,2
        if b[2][1] == player:
            if b[2][2] == player:
                return True,2,0,2,2
    if b[0][1] == player:
        if b[1][1] == player:
            if b[2][1] == player:
                return True,0,1,2,1
    if b[1][0] == player:
        if b[1][1] == player:
            if b[1][2] == player:
                return True,1,0,1,2
    if b[0][2] == player:
        if b[1][2] == player:
            if b[2][2] == player:
                return True,0,2,2,2
    return False

def AI_move():
    global board

    best_score = -100
    best_move = []

    for i in range(len(board)):
        for l in range(len(board[i])):
            if board[i][l] == '':
                board[i][l] = 'o'
                score = mini_max(False,0)
                board[i][l] = ''
                if score > best_score:
                    best_score = score
                    best_move = [i,l]

    board[best_move[0]][best_move[1]] = 'o'

def mini_max(turn,depth):
    if has_won('o',board):
        return 1
    if has_won('x',board):
        return -1
    full = True
    for i in board:
        for l in i:
            if l == '':
                full = False
    if full:
        return 0

    if turn:
        best_score = -1000
    else:
        best_score = 1000

    for i in range(len(board)):
        for l in range(len(board[i])):
            if board[i][l] == '':
                if turn:
                    board[i][l] = 'o'
                    score = mini_max(False,depth+1)
                    board[i][l] = ''
                    if score > best_score:
                        best_score = score
                else:
                    board[i][l] = 'x'
                    score = mini_max(True,depth+1)
                    board[i][l] = ''
                    if score < best_score:
                        best_score = score
    return best_score

def click(event):
    global mouse_x,mouse_y,clicking
    mouse_x = event.x
    mouse_y = event.y
    clicking = True

root.bind('<Button-1>',click)

mb = Mega_Board()

while True:
    try:
        canvas.delete(ALL)

        #draw text
        canvas.create_text(175,325,text=text,font=('TkTextFont',20))

        #draw board
        canvas.create_line(150,0,150,450,width=4)
        canvas.create_line(300,0,300,450,width=4)
        canvas.create_line(0,150,450,150,width=4)
        canvas.create_line(0,300,450,300,width=4)

        for i in range(3):
            for l in range(3):
                x = i*150
                y = l*150
                canvas.create_line(x+5,y+50,x+145,y+50,width=4)
                canvas.create_line(x+10,y+100,x+145,y+100,width=4)
                canvas.create_line(x+50,y+5,x+50,y+145,width=4)
                canvas.create_line(x+100,y+5,x+100,y+145,width=4)

        for i in mb.boards:
            for j in i:
                for k in j.tiles:
                    for h in k:
                        bx = i.index(j)*150
                        by = mb.boards.index(i)*150
                        x = bx + k.index(h)*50+25
                        y = by + j.tiles.index(k)*50+25

                        if h.value == 'o':
                            canvas.create_oval(x-10,y-10,x+10,y+10)
                        if h.value == 'x':
                            canvas.create_line(x-7,y-7,x+7,y+7)
                            canvas.create_line(x-7,y+7,x+7,y-7)

        if clicking:
            clicking = False

            x = mouse_x//50
            y = mouse_y//50

            mbx = (x)//3
            mby = (y)//3

            bx = (x)%3
            by = (y)%3

            if mbx <= 2 and mby <= 2:
                if mb.boards[mby][mbx] == mb.available_board or mb.available_board == 'any':
                    if mb.boards[mby][mbx].tiles[by][bx].value == '':
                        mb.boards[mby][mbx].tiles[by][bx].value = mb.turn
                        mb.available_board = mb.boards[by][bx]
                        if mb.turn == 'x':
                            mb.turn = 'o'
                        else:
                            mb.turn = 'x'

        root.update()
    except TclError:
        quit()
