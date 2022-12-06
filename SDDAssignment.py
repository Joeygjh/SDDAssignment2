import random
#Start New Game - Yat Soon
def StartNewGame():
    board = [['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
            ['','','','','','','','','','','','','','','','','','','',''],\
                ]
    turn = 1
    print('Turn {}'.format(turn))

    # 5 Building, 8 Copies each
    BuildingCode = ['R','I','C','O','*']

    #Creation of Board
    print("{:>5}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}{:>6}".format("A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"))
    for x in range(len(board)):
        column = len(board[x])
        
        print('  ' + '+-----'*column + '+')
      
        if x >=9:
            print(x+1, end = '')
        else:
            print('',x+1, end = '')
        for y in range(len(board[x])):
            print('|{:^5}'.format(board[x][y]), end = '')
        print('|')
    print('  ' + '+-----'*column + '+')
    Building1 = random.randint(0,4)
    Building2 = random.randint(0,4)
    #Selection
    print('1. Build a {}'.format(BuildingCode[Building1]))
    print('2. Build a {}'.format(BuildingCode[Building2]))
    print('3. See remaining buildings')
    print('4. See current score')
    print()
    print('5. Save game')
    print('0. Exit to main menu')
    option = input('Your choice? ')
    return option,board,Building1,Building2,turn
startNG = StartNewGame()



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
