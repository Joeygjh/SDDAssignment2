import os
import pickle
import random
import string
import sys

GameBoard = 20



TOTAL_TURNS = 16
NO_OF_SAME_BUILDINGS = 8
BUILDINGS = [' R ', ' I ', ' C ', ' O ', ' * '] 
COLUMN_LABELS = string.ascii_uppercase[:GameBoard]     


def display_board(board):
    ''' Show board '''
    line = ''
    for i in COLUMN_LABELS:
        if len(i) < 2:
            line += ' ' * 5 + i
        else:
            line += ' ' * 4 + i
    print(line)

    dashLine = '  +'
    for i in range(GameBoard):
        dashLine += '-----+'
    print(dashLine)

    for i in range(GameBoard):
        if i >= 9:   
            line = '%s|' % (i + 1)
        else:
            line = ' %s|' % (i + 1)
        for j in range(GameBoard):
            line += ' %s |' % board[i][j]
        print(line)
        print(dashLine)


def check_adj_buildings(board, i, j):       
    ''' Get Adjacent Buildings '''
    adjacent_buildings = []
    for x in [i-1, i+1]:
        if x >= 0 and x < GameBoard and board[x][j] != '   ':
            adjacent_buildings.append(board[x][j])
    for x in [j-1, j+1]:
        if x >= 0 and x < GameBoard and board[i][x] != '   ':
            adjacent_buildings.append(board[i][x])

    return adjacent_buildings


def resume_game(data):           
    ''' Start Game '''
    player = data['player']
    board = data['board']
    turn = data['turn']
    coins = data['coins']
    remaining_buildings = data['remaining_buildings']
    display_board(board)

    while turn < TOTAL_TURNS:
        print(f'Turn: {turn + 1}     Point: {display_score(board)}          Coins: {coins}      ')
        


        randombuilding1 = random.choice(
            [k for k, v in remaining_buildings.items() if v > 0])       # dictionary iternation
        randgombuilding2 = random.choice(
            [k for k, v in remaining_buildings.items() if v > 1])
        #In order to make sure both buildings are different I put a while function for random buildings
        while randombuilding1 == randgombuilding2:
            randgombuilding2 = random.choice(
            [k for k, v in remaining_buildings.items() if v > 1])
            
        build_1 = display_building_names(randombuilding1)
        build_2 = display_building_names(randgombuilding2)
        print(f'''

    1. Build a {build_1}
    2. Build a {build_2}
    3. See current score
    4. Save game
    0. Exit to main menu\n''')
        choice = input('Enter your choice: ')
        if choice == '1' or choice == '2':
            location = input('Build where? ').upper()
            if location[0].isalpha() and location[1:].isnumeric():
                i = int(location[1:3]) - 1 
                j = COLUMN_LABELS.index(location[0])
            else:
                print(f'Invalid location [{location}]')
                continue

            if not (i >= 0 and i < GameBoard and j >= 0 and j < GameBoard):
                print(f'Invalid location [{location}]')
                continue
            
            
            if turn != 0:
                if not check_adj_buildings(board, i, j):
                    print('You must build next to an existing building')
                    continue
            building = randombuilding1 if choice == '1' else randgombuilding2
            board[i][j] = building
            remaining_buildings[building] -= 1
            coins -= 1
            turn += 1
            coins += display_coins(board,location)
            display_board(board)
        elif choice == '3':
            display_score(board)
        elif choice == '4':
            data = {}
            data['player'] = player
            data['board'] = board
            data['turn'] = turn
            data['coins'] = coins
            data['remaining_buildings'] = remaining_buildings
            save_game(data)
        elif choice == '0':
            return
        else:
            print(f'Invalid Option [{choice}] choosen')

    display_board(board)
    total_score = display_score(board)
    
    
 
    if turn == TOTAL_TURNS:
        data = {}           
        data['player'] = player
        data['board'] = board
        data['turn'] = turn
        data['coins'] = coins
        data['remaining_buildings'] = remaining_buildings           
        save_game(data)
        save_pos(player, total_score)


def display_score():
    ''' Show Score '''
    if not os.path.isfile('high.score'):
        print('No Highscore Found')
        return
    data = pickle.load(open('high.score', 'rb'))
    print('''--------- HIGH SCORES ---------''')
    line = '{:3}  {:12}  {:5}'.format('Rank', 'Player', 'Score')
    print(line)
    line = '{:>3}  {:>12}  {:>5}'.format('-'*3, '-'*12, '-'*5)
    print(line)
    rank = 0
    for (k, v) in data:
        rank += 1
        line = '{:>3}  {:12}  {:>3}'.format(rank , k, v)
        print(line)

    
def save_pos(player, total_score):
    ''' Save Position '''
    data = []
    if os.path.isfile('high.score'):
        old_data = pickle.load(open('high.score', 'rb'))
        data = []
        count = 0
        entered_flag = False
        for (k, v) in old_data:
            count += 1
            if entered_flag == False and total_score > v:
                print(
                    f'Congratulations! You are number {count} on the highscore board!')
                data.append((player, total_score))
                entered_flag = True
            data.append((k, v))
        if entered_flag == False:
            data.append((player, total_score))
        pickle.dump(data, open('high.score', 'wb'))
    else:
        data = []
        data.append((player, total_score))
        pickle.dump(data, open('high.score', 'wb'))
        print('Congratulations! You are number 1 on the highscore board!')
    display_score()

def display_building_names(name):
    if name == ' I ':
        return 'Industry (I)'
    elif name == ' R ':
        return 'Residential (R)'
    elif name == ' C ':
        return 'Commercial (C)'
    elif name == ' O ':
        return 'Park (O)'
    elif name == ' * ':
        return 'Road (*)'


def start_new_game():
    ''' New Game '''
    data = {}
    data['board'] = [['   '] * GameBoard for i in range(GameBoard)]
    data['turn'] = 0
    data['coins'] = 16
    data['remaining_buildings'] = {}
    for i in BUILDINGS:
        data['remaining_buildings'][i] = NO_OF_SAME_BUILDINGS
    data['player'] = input('Enter the player name: ')
    resume_game(data)


def load_saved_game():
    ''' Load Game '''
    data = pickle.load(open('game.save', 'rb'))
    resume_game(data)

def calculate_coins(board, i, j):
    '''Get score of coins'''
    coins = 0
    building = board[i][j]
    adjacent_buildings = check_adj_buildings(board, i, j)
    if building == ' I ' :
        if ' R ' in adjacent_buildings:
            coins += 1
    return coins
            
def calculate_score(board, i, j):
    ''' Get score of a building '''
    score = 0
    building = board[i][j]
    adjacent_buildings = check_adj_buildings(board, i, j)
    if building == ' * ':
        if board[i][j+1] == ' * ':
            score += 1
    elif building == ' R ':
        if ' I ' in adjacent_buildings:
            score += 1
        else:
            for building in adjacent_buildings:
                if building in [' R ', ' C ']:
                    score += 1
                elif building == ' O ':
                    score += 2

    elif building == ' I ':
        score += 1
    elif building == ' C ':
        if board[i][j+1] == ' C ':
            score += 1
        if board[i+1][j] == ' C ':
            score += 1
 
    elif building == ' O ' :
        if board[i][j+1] == ' O ':
            score += 1
        if board[i+1][j] == ' O ':
            score += 1
 
    return score


def display_coins(board,location):
    ''' Show additional coins '''
    total_coins = 0
    i = int(location[1:3]) - 1 
    j = COLUMN_LABELS.index(location[0])
    total_coins += calculate_coins(board, i, j)
    return total_coins


def display_score(board):
    ''' Show current score '''
    total_score = 0
    for i in range(GameBoard):
        for j in range(GameBoard):
            total_score += calculate_score(board, i, j)
    
    return total_score


def save_game(data):
    ''' Save Game '''
    pickle.dump(data, open('game.save', 'wb'))
    print('Saved game successfully!')


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
            start_new_game()
        elif choice == '2':
            load_saved_game()
        elif choice == '3':
            display_score()
        elif choice == '0':
            print('Bye!')
            sys.exit()
        else:
            print(f'Invalid Option [{choice}] choosen')


display_menu()