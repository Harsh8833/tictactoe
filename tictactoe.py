from tkinter import *

window = Tk()
board = dict()
turn = 'X'

def checkwinner():
    # veritcal check
    for j in range(3):
        xcount = 0
        ycount = 0
        for i in range(3):
            if (board[str(j)+str(i)]['text'] == 'X'):
                xcount += 1
            if (board[str(j)+str(i)]['text'] == 'O'):
                ycount += 1
            if (xcount == 3):
                return 0
            if (ycount == 3):
                return 1
    # horizantal check
    for i in range(3):
        xcount = 0
        ycount = 0
        for j in range(3):
            if (board[str(j)+str(i)]['text'] == 'X'):
                xcount += 1
            if (board[str(j)+str(i)]['text'] == 'O'):
                ycount += 1
            if (xcount == 3):
                return 0
            if (ycount == 3):
                return 1
        # diagonal check 1
        xcount = 0
        ycount = 0
        for i in range(3):
            if (board[str(i)+str(i)]['text'] == 'X'):
                xcount += 1
            if (board[str(i)+str(i)]['text'] == 'O'):
                ycount += 1
            if (xcount == 3):
                return 0
            if (ycount == 3):
                return 1
        # diagonal check 2
        xcount = 0
        ycount = 0
        for i in range(3):
            if (board[str(i)+str(2-i)]['text'] == 'X'):
                xcount += 1
            if (board[str(i)+str(2-i)]['text'] == 'O'):
                ycount += 1
            if (xcount == 3):
                return 0
            if (ycount == 3):
                return 1
def click(x, y):
    global turn
    if turn == 'X':
        board[x+y].config(text = 'X')
        board[x+y]["state"] = DISABLED
        turn = 'O'   
    else:
        board[x+y].config(text = 'O')
        board[x+y]["state"] = DISABLED
        turn = 'X'
    winner = checkwinner()
    if (winner == 0):
        print('X is winner')
    elif(winner == 1):
        print('O is winner')        
     
ttt_label = Label(window, text = 'TicTacToe', font=('orbitron',45,'bold'))
ttt_label.pack()
topframe = Frame(window)
topframe.pack()

boardframe = Frame(window)
boardframe.pack(padx=5, pady=5)
boardframe.pack()
for column in range(3):
    for row in range(3):
        button = Button(boardframe, font=('orbitron',45,'bold'), width=3, text=' ',command= lambda x = str(column), y = str(row): click(x, y))
        button.grid(row = row, column = column)
        board[str(column)+str(row)] = button

window.mainloop()
