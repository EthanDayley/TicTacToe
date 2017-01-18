from tkinter import*
def CheckGame(LastMove):
    global ListPositions
    global ListXPositions
    global ListOPositions
    ListXPositions.sort()
    ListOPositions.sort()
    isWin = False
    #exec('List = List%sPositions' % LastMove)
    #exec('numMoves = len(List%sPositions)' % LastMove) # assign the number of items in List(X or O)Positions to numMoves
    #numMoves = len(List)
    #if numMoves >= 2:
    if LastMove == 'X':
        print('X: '+str(ListXPositions))
        if len(ListXPositions) >= 3:
            for step in range(1,5):
                Count = 0
                for i in range(ListXPositions[0],ListXPositions[-1]+1,step):
                    if i in ListXPositions:
                        Count+=1
                        if Count == 3:
                            isWin = True
                            break
                    elif i not in ListXPositions:
                        Count = 0
                        break
    elif LastMove == 'O':
        print('O: '+str(ListOPositions))
        if len(ListOPositions) >= 3:
            for step in range(1,5):
                Count = 0
                for i in range(ListOPositions[0],ListOPositions[-1]+1,step):
                    if i in ListOPositions:
                        Count+=1
                        if Count == 3:
                            isWin = True
                            break
                    elif i not in ListOPositions:
                        Count = 0
                        break
    if isWin: return 'W'
    elif '' not in ListPositions: return 'T'
    
            #for i,x in zip(range(ListXPositions[0], 9), ListXPositions):
                

def Move(PressedButton, ButtonIndex):   # ButtonIndex is the index of the button in the global list ListPositions
    global ListPositions #not initializing, global variables must be declared wherever you wish to access them
    global WhoseTurn
    global ListXPositions
    global ListOPositions
    if ListPositions[ButtonIndex] != '':
        PressedButton.flash()
    else:
        PressedButton.config(text=WhoseTurn, activeforeground='red')
        ListPositions[ButtonIndex] = WhoseTurn
        if WhoseTurn == 'X':
            ListXPositions.append(ButtonIndex)
            WhoseTurn = 'O'
            Result = CheckGame('X')
            if Result == 'W':
                print(Result)
                print('X Wins!')
            if Result =='T': print('The game is a tie!')
            
        elif WhoseTurn == 'O':
            ListOPositions.append(ButtonIndex)
            WhoseTurn = 'X'
            Result = CheckGame('O')
            if Result == 'W': print('O Wins!')
            if Result =='T': print('The game is a tie!')
def Initialize():
    #initialize variables
    global ListPositions #List of the current values of each index
    ListPositions = ['', '', '', '', '', '', '', '', '']
    global ListXPositions
    ListXPositions = []
    global ListOPositions
    ListOPositions = []
    global WhoseTurn
    WhoseTurn = 'X'
    #root
    root = Tk()
    root.config(bg='black')
    root.wait_visibility(root)
    root.wm_attributes('-alpha','0.7')
    root.wm_attributes('-fullscreen','true')
    #title
    title = Label(root, bg='#222', fg='white', text='TicTacToe version 2.0', font=('Snas-Serif',50,'normal'))
    title.pack()
    title.place(relx=0.5, rely=0, anchor=N)
    #exitButton
    exitButton = Button(root, text="X", font=('Sans-Serif',70,'bold'), bg='black', fg='white', height=1, width=1, borderwidth=0, highlightthickness=0, activeforeground='red', activebackground='black', cursor='hand2')
    exitButton.pack()
    exitButton.place(relx=1, rely=0, anchor=NE)
    exitButton.bind('<Button-1>', lambda event: root.destroy())
    ########Initializing buttons#################
    #A
    A=Button(root, text='   ', fg='black', bg='white',font=('Sans-Serif',100,'bold'), cursor='hand2')
    A.pack()
    A.place(relx=0.4,rely=0.3, anchor=CENTER, width=166, height= 166)
    A.bind('<Button-1>', lambda event, pressedButton = A: Move(pressedButton, 0))
    
    #B
    B=Button(root, text='   ', fg='black', bg='white',font=('Sans-Serif',100,'bold'), cursor='hand2')
    B.pack()
    B.place(relx=0.5,rely=0.3, anchor=CENTER, width=166, height= 166)
    B.bind('<Button-1>', lambda event, pressedButton = B: Move(pressedButton, 1))
    #C
    C=Button(root, text='   ', fg='black', bg='white',font=('Sans-Serif',100,'bold'), cursor='hand2')
    C.pack()
    C.place(relx=0.6,rely=0.3, anchor=CENTER, width=166, height= 166)
    C.bind('<Button-1>', lambda event, pressedButton = C: Move(pressedButton, 2))
    #next line
    #D
    D=Button(root, text='   ', fg='black', bg='white',font=('Sans-Serif',100,'bold'), cursor='hand2')
    D.pack()
    D.place(relx=0.4,rely=0.475, anchor=CENTER, width=166, height= 166)
    D.bind('<Button-1>', lambda event, pressedButton = D: Move(pressedButton, 3))
    #E
    E=Button(root, text='   ', fg='black', bg='white',font=('Sans-Serif',100,'bold'), cursor='hand2')
    E.pack()
    E.place(relx=0.5,rely=0.475, anchor=CENTER, width=166, height= 166)
    E.bind('<Button-1>', lambda event, pressedButton = E: Move(pressedButton, 4))
    #F
    F=Button(root, text='   ', fg='black', bg='white',font=('Sans-Serif',100,'bold'), cursor='hand2')
    F.pack()
    F.place(relx=0.6,rely=0.475, anchor=CENTER, width=166, height= 166)
    F.bind('<Button-1>', lambda event, pressedButton = F: Move(pressedButton, 5))
    #next line
    #G
    G=Button(root, text='   ', fg='black', bg='white',font=('Sans-Serif',100,'bold'), cursor='hand2')
    G.pack()
    G.place(relx=0.4,rely=0.651, anchor=CENTER, width=166, height= 166)
    G.bind('<Button-1>', lambda event, pressedButton = G: Move(pressedButton, 6))
    #H
    H=Button(root, text='   ', fg='black', bg='white',font=('Sans-Serif',100,'bold'), cursor='hand2')
    H.pack()
    H.place(relx=0.5,rely=0.651, anchor=CENTER, width=166, height= 166)
    H.bind('<Button-1>', lambda event, pressedButton = H: Move(pressedButton, 7))
    #I
    I=Button(root, text='   ', fg='black', bg='white',font=('Sans-Serif',100,'bold'), cursor='hand2')
    I.pack()
    I.place(relx=0.6,rely=0.651, anchor=CENTER, width=166, height= 166)
    I.bind('<Button-1>', lambda event, pressedButton = I: Move(pressedButton, 8))
    #mainloop
    root.mainloop()
Initialize()

