import os
import pickle
import random
import string
import sys

#Start New Game - Yat Soon
GameBoard = 20
TotalNumOfTurns = 16

#Build building - Cheng Xuan
NO_OF_SAME_Buildings = 8
Buildings = [' R ', ' I ', ' C ', ' O ', ' * '] 
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

    rowLine = '  +'
    for i in range(GameBoard):
        rowLine += '-----+'
    print(rowLine)

    for i in range(GameBoard):
        if i >= 9:   
            line = '%s|' % (i + 1)
        else:
            line = ' %s|' % (i + 1)
        for j in range(GameBoard):
            line += ' %s |' % board[i][j]
        print(line)
        print(rowLine)

#Build building - Cheng Xuan
def check_adj_Buildings(board, i, j):        
    ''' Check Adjacent Buildings '''
    adjacent_Buildings = []
    for x in [i-1, i+1]:
        if x >= 0 and x < GameBoard and board[x][j] != '   ':
            adjacent_Buildings.append(board[x][j])
    for x in [j-1, j+1]:
        if x >= 0 and x < GameBoard and board[i][x] != '   ':
            adjacent_Buildings.append(board[i][x])
    return adjacent_Buildings

def resumegame(data,coins):            
    ''' Start Game '''
    player = data['player']
    board = data['board']
    turn = data['turn']
    remaining_Buildings = data['remaining_Buildings']

    while turn < TotalNumOfTurns:
        print(f'Turn {turn + 1}\n')

        show_board(board)

        randomBuilding1 = random.choice(
            [k for k, v in remaining_Buildings.items() if v > 0])       
        randomBuilding2 = random.choice(
            [k for k, v in remaining_Buildings.items() if v > 1])
        print(f'''
Coins: {coins}

    1. Build a {randomBuilding1}
    2. Build a {randomBuilding2}
    3. See remaining Buildings
    4. See current score
    5. Save game
    0. Exit to main menu\n''')
        choice = input('Enter your choice: ')
        #Build building - Cheng Xuan
        if choice == '1' or choice == '2':
            location = input('Build where? ').upper()
            i = int(location[1:3]) - 1
            j = COLUMN_LABELS.index(location[0])
            print(location[0])
            print(j)
            print(i)
            if not (i >= 0 and i < GameBoard and j >= 0 and j < GameBoard):
                print(f'Invalid location [{location}]')
                continue
            if turn != 0:
                if not check_adj_Buildings(board, i, j):
                    print('You must build next to an existing building')
                    continue
            building = randomBuilding1 if choice == '1' else randomBuilding2
            board[i][j] = building
            remaining_Buildings[building] -= 1
            coins -= 1
            turn += 1
            
            
            
    #     elif choice == '3':
    #         print('Building \t Remaining')
    #         print('-------- \t ---------')
    #         for k, v in remaining_Buildings.items():
    #             print(k, ' \t\t ', v)
    #         input('\nEnter to continue\n')
    #     elif choice == '4':
    #         show_current_score(board)
    #     elif choice == '5':
    #         data = {}
    #         data['player'] = player
    #         data['board'] = board
    #         data['turn'] = turn
    #         data['remaining_Buildings'] = remaining_Buildings
    #         save_game(data)

    #Display Exit Game - Winston
        elif choice == '0':
            return
    #     else:
    #         print(f'Invalid Option [{choice}] choosen')

    # show_board(board)
    # total_score = show_current_score(board)
 
    # if turn == TotalNumOfTurns:
    #     data = {}           #This is a dict and I will input 4 variables for now as shown for the next few lines
    #     data['player'] = player
    #     data['board'] = board
    #     data['turn'] = turn
    #     data['remaining_Buildings'] = remaining_Buildings           
        # save_game(data)
        # save_position(player, total_score)
            
           

def StartNewGame():
    coins = 16
    ''' New Game '''
    data = {}
    data['board'] = [['   '] * GameBoard for i in range(GameBoard)]
    data['turn'] = 0
    data['remaining_Buildings'] = {}
    for i in Buildings:
        data['remaining_Buildings'][i] = NO_OF_SAME_Buildings
    data['player'] = input('Enter the player name: ')
    resumegame(data,coins)






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

        #Display Exit Game - Winston
        elif choice == '0': 
            print('Hope you enjoyed playing City-Building Strategy Game!') 
            sys.exit() 
        # else: 
        #     print(f'Invalid Option [{choice}] choosen') 
 
 
display_menu()
