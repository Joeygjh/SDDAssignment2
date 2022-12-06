import os
import pickle
import random
import string
import sys

#Start New Game - Yat Soon
GameBoard = 20
Total_NumOfTurns = 16
NO_SAME_BUILDINGS = 8
BUILDINGS = [' R ', ' I ', ' C ', ' O ', ' * '] 
COLUMN_LABELS = string.ascii_uppercase[:GameBoard]     

def show_board(board):
    ''' Show board '''
    line = ''
    for i in COLUMN_LABELS:
        if len(i) < 2:
            line += ' ' * 5 + i
        else:
            line += ' ' * 4 + i
    print(line)

    RowLine = '  +'
    for i in range(GameBoard):
        RowLine += '-----+'
    print(RowLine)

    for i in range(GameBoard):
        if i >= 9:   
            line = '%s|' % (i + 1)
        else:
            line = ' %s|' % (i + 1)
        for j in range(GameBoard):
            line += ' %s |' % board[i][j]
        print(line)
        print(RowLine)

#1 

def resumegame(data,coins):            
    ''' Start Game '''
    player = data['player']
    board = data['board']
    turn = data['turn']
    remaining_buildings = data['remaining_buildings']

    while turn < Total_NumOfTurns:
        print(f'Turn {turn + 1}\n')

        show_board(board)

        RandomBuilding1 = random.choice(
            [k for k, v in remaining_buildings.items() if v > 0])       
        RandomBuilding2 = random.choice(
            [k for k, v in remaining_buildings.items() if v > 1])
        print(f'''
Coins: {coins}

    1. Build a {RandomBuilding1}
    2. Build a {RandomBuilding2}
    3. See remaining buildings
    4. See current score
    5. Save game
    0. Exit to main menu\n''')
        choice = input('Enter your choice: ')
        if choice == '1' or choice == '2':
                coins -= 1
                turn += 1
        #2     

def StartNewGame():
    coins = 16
    ''' New Game '''
    data = {}
    data['board'] = [['   '] * GameBoard for i in range(GameBoard)]
    data['turn'] = 0
    data['remaining_buildings'] = {}
    for i in BUILDINGS:
        data['remaining_buildings'][i] 
    data['player'] = input('Enter the player name: ')
    resumegame(data,coins)



#Display Exit Game - Winston
def ExitGame():
    EndGame = 'Hope you enjoy playing City-Building Strategy Game'
    return EndGame
EXitG = ExitGame()

#Display Main Menu - Joey
def display_menu(): 
    ''' Display Menu''' 
    while True: 
        print(''' 
    Welcome, mayor of Ngee Ann City! 
    ---------------------------- 
    1. Start new game 
    2. Load saved game 
    3. Show High Score 
    0. Exit\n''') 
        choice = input('Enter your choice: ') 
        if choice == '1': 
             StartNewGame() 
        # elif choice == '2': 
        #     load_game() 
        # elif choice == '3': 
        #     show_score() 
        # elif choice == '0': 
        #     print('Bye!') 
        #     sys.exit() 
        # else: 
        #     print(f'Invalid Option [{choice}] choosen') 
 
 
display_menu()
