from tkinter import *

root = Tk()
canvas = Canvas(root,width=350,height=350)
canvas.pack()

board = [['','',''],
         ['','',''],
         ['','','']]
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

while True:
    try:
        canvas.delete(ALL)

        #draw text
        canvas.create_text(175,325,text=text,font=('TkTextFont',20))

        #draw board
        canvas.create_line(100,0,100,300,width=4)
        canvas.create_line(200,0,200,300,width=4)
        canvas.create_line(0,100,300,100,width=4)
        canvas.create_line(0,200,300,200,width=4)

        #draw peices
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 'x':
                    draw_x((len(board)-x)*100-50,(len(board[x])-y)*100-50)
                if board[x][y] == 'o':
                    draw_o((len(board)-x)*100-50,(len(board[x])-y)*100-50)

        #place peices
        if clicking and not winner and turn == 'x':
            x = int(mouse_x/100)
            y = int(mouse_y/100)
            bx = len(board)-x-1
            by = len(board)-y-1

            text = ''

            if board[by][bx] == '':
                board[by][bx] = turn

                turn = 'o'

            else:
                text = 'That space is already taken!'

            clicking = False

        elif turn == 'o' and not winner:
            AI_move()
            turn = 'x'

        if has_won('x',board):
            text = 'X has won!'
            winner = 'x'
        if has_won('o',board):
            winner = 'o'
            text = 'O has won!'

        root.update()
    except TclError:
        quit()
