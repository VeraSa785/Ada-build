
# 1st solution

player1 = 'rock'
player2 = 'paper' 

if player1 == 'paper' or player2 == 'paper':
    if player2 == 'rock':
        print('Player 1 won!')
    elif player2 == 'scissors':
        print('Player 2 won!')
    else:
        print('It\'s a tie!')
        
if player1 == 'rock' or player2 == 'rock':
    if player2 == 'paper':
        print('Player 2 won!')
    elif player2 == 'scissors':
        print('Player 1 won!')
    else:
        print('It\'s a tie!')
        
 if player1 == 'scissors' or player2 == 'scissors':
    if player2 == 'paper':
        print('Player 1 won!')
    elif player2 == 'rock':
        print('Player 2 won!')
    else:
        print('It\'s a tie!')
        
# 2nd solution
       
player1 = 'rock'
player2 = 'paper'

if player2 == 'paper':
    if player1 == 'rock':
        print('Player 2 won!')
    else:
        print('Player 1 won!')
    
elif player2 == 'rock':
    if player1 == 'scissors':
        print('Player 2 won!')
    else:
        print('Player 1 won!')
        
elif player2 == 'scissors':
    if player1 == 'paper':
        print('Player 2 won!')
    else:
        print('Player 1 won!')
else:
    print('It\'s a tie!')
