
# 1st solution (3.4 method)
       
player1 = 'rock'
player2 = 'paper'

# tie
if player1 == player2:
    print('It\'s a tie!')

# player2 paper
elif player2 == 'paper':
    if player1 == 'rock':
        print('Player 2 won!')
    else:
        print('Player 1 won!')

#player2 rock    
elif player2 == 'rock':
    if player1 == 'scissors':
        print('Player 2 won!')
    else:
        print('Player 1 won!')

#player2 scissors        
elif player2 == 'scissors':
    if player1 == 'paper':
        print('Player 2 won!')
    else:
        print('Player 1 won!')
              
else: print('It\'s a tie!')
        
# __________________________________________
# 2nd solution (3.5 method)

player1 = 'rock'
player2 = 'paper' 

# paper player 1 or 2
if player1 == 'paper' or player2 == 'paper':
    if player2 == 'rock':
        print('Player 1 won!')
    elif player2 == 'scissors':
        print('Player 2 won!')

# rock player 1 or 2
elif player1 == 'rock' or player2 == 'rock':
    if player2 == 'paper':
        print('Player 2 won!')
    elif player2 == 'scissors':
        print('Player 1 won!')

# scissors player 1 or 2
elif player1 == 'scissors' or player2 == 'scissors':
    if player2 == 'paper':
        print('Player 1 won!')
    elif player2 == 'rock':
        print('Player 2 won!')
else:
    print('It\'s a tie!')
        
# _________________________________________________
# 3rd solution (3.6 method)

player1 = 'scissors'
player2 = 'paper'

# scenario for 1 player won
if player1 == player2:
    print('It\'s a tie!')
elif player1 == 'paper' and player2 == 'rock':
       print('Player 1 won!')
elif player1 == 'rock' and player2 == 'scissors':
       print('Player 1 won!')
       
# tie
elif player1 == 'scissors' and player2 == 'paper':
       print('Player 1 won!')
       
# scenario for 2 player won
else:
    print('Player 2 won!')
     
          
