try:
    from tkinter import *
except ImportError:
    from Tkinter import *

root = Tk()
canvas = Canvas(root,width=950,height=950)
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
    mouse_x = event.y
    mouse_y = event.x
    clicking = True

root.bind('<Button-1>',click)

mb = Mega_Board()

while True:
    try:
        canvas.delete(ALL)

        #draw text
        canvas.create_text(175,325,text=text,font=('TkTextFont',20))

        #draw board
        for i in range(3):
            for l in range(3):
                x = i*150
                y = l*150
                canvas.create_line(x+5,y+50,x+145,y+50,width=4)
                canvas.create_line(x+10,y+100,x+145,y+100,width=4)
                canvas.create_line(x+50,y+5,x+50,y+145,width=4)
                canvas.create_line(x+100,y+5,x+100,y+145,width=4)

        for i in mb.boards:
            for j in i.

        root.update()
    except TclError:
        quit()
