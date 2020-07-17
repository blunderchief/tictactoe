#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[2]:


def GetPlayerNames():
    
    global PlayerOne
    global PlayerTwo
    
    PlayerOne = input('Player One, what is your name? ')
    PlayerTwo = input('Player Two, what is your name? ')


# In[3]:


def GetPlayerOneMove(board):
    
    global move
    keepgoing = False
    
    #Check for move already made
    
    while keepgoing == False:
        move = int(input(f'{PlayerOne}, make a move: '))
        if 'X' in board[move]:
            print('NARP try again!')
            continue
            
        elif move not in range(1,10):
            print('You gotta pick between 1 and 10!')
    
        else:
            keepgoing = True
    
        


# In[4]:


def PlacePlayerOneMove(board):
    
    #global board
    #global move
    #global not_victory
    global top_row
    
    while 'X' not in board[move]:
        board[move] = 'X'
        
        display_board(board)


# In[5]:


def GetPlayerTwoMove(board):
    
    global move
    keepgoing = False
    
    #Check for move already made
    
    while keepgoing == False:
        move = int(input(f'{PlayerTwo}, make a move: '))
        if 'O' in board[move]:
            print('NARP try again!')
            continue
            
        elif move not in range(1,10):
            print('You gotta pick between 1 and 10!')
    
        else:
            keepgoing = True
    


# In[6]:


def PlacePlayerTwoMove(board):
    
    #global board
    #global move
    #victorycheck(top_row)
    
    while 'O' not in board[move]:
        board[move] = 'O'
        
    display_board(board)


# In[7]:


def victorycheck(board, marker):
    
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or # across the top
    (board[4] == marker and board[5] == marker and board[6] == marker) or # across the middle
    (board[1] == marker and board[2] == marker and board[3] == marker) or # across the bottom
    (board[7] == marker and board[4] == marker and board[1] == marker) or # down the middle
    (board[8] == marker and board[5] == marker and board[2] == marker) or # down the middle
    (board[9] == marker and board[6] == marker and board[3] == marker) or # down the right side
    (board[7] == marker and board[5] == marker and board[3] == marker) or # diagonal
    (board[9] == marker and board[5] == marker and board[1] == marker)) # diagonal

    print(board)


# In[8]:


def AskPlayAgain():
        
        return input(f'\nPlay Again? Y/N ').upper().startswith('Y')
            
    


# In[1]:


print(f'Welcome to Exciting Game of: \n\nTIC\n\nTAC\n\nTOE')
print(f'\n\nCompete against a friend, or play in complete solitude \nagainst yourself to see which letter is superior: "X" or "O"!!!')
    
while True:
    
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        
    PlayerOne = 'x'
    PlayerTwo = 'y'
    decision = input(f'\nAre you ready to play? (Y/N) ').upper()
        
    if decision != 'Y' and decision != 'N':
        print(f'\nPlease type "Y" or "N"')
                  
    elif decision == 'N':
        print(f'\nGoodbye.')
        break
            
    else:
        gametime = True
        
        
            
    print(f'\nRules: Each player takes turns placing an "X" or an "O" on the game board, using the numpad as a' 
            ' physical proxy.\nThat is to say, 7 is the upper-left square, 3 is lower-right, etc.  The game will\n' 
            'be over when one player has managed to place three of their letter in a row.  Good luck!\n\n')
        
    GetPlayerNames()
        
    print(f'\nThanks {PlayerOne} and {PlayerTwo}! Begin your harrowing journey!\n')
        
    not_victory = True
  
    display_board(board)
            
    Winner = 'Nobody'
                
    while gametime == True:
        
        PlayAgain = ' '
                    
        move = 'nothing'
                
        if Winner == 'Nobody':
            
            clear_output()
              
            GetPlayerOneMove(board)
              
            PlacePlayerOneMove(board)
                
            if victorycheck(board, 'X'):
            
                display_board(board)
                Winner = f'{PlayerOne}'
                print(f'\nFine, {Winner}, you win; are you happy?')
                gametime = False
                
            else:
                if ' ' not in board:
                    display_board(board)
                    print(f'\nGreat, now nobody gets to win!')
                    break
                    
                    
                    
                    #while PlayAgain == ' ':

                        #AskPlayAgain()
                    
                        #if PlayAgain == 'N':
                            #break
                        #elif PlayAgain != 'N' and PlayAgain != 'Y':
                            #print(f'\nYou gotta type "Y" or "N".')
                            
        if Winner == 'Nobody':
            
            clear_output()
            
            GetPlayerTwoMove(board)
              
            PlacePlayerTwoMove(board)
                
            if victorycheck(board, 'O'):
            
                display_board(board)
                Winner = f'{PlayerTwo}'
                print(f'\nFine, {Winner}, you win; are you happy?')
                gametime = False
                
            elif ' ' not in board:
                display_board(board)
                print(f'\nGreat, now nobody gets to win!')
                break            
                    
                    #while PlayAgain == ' ':

                        #AskPlayAgain()
                    
                        #if PlayAgain == 'N':
                            #break
                        #elif PlayAgain != 'N' and PlayAgain != 'Y':
                            #print(f'\nYou gotta type "Y" or "N".')
                    
    if not AskPlayAgain():
        break
                    
                        
                
    


# In[ ]:




