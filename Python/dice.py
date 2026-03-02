import random

player1 = 0
player2 = 0

total1 = 0
total2 = 0

for i in range(10):
    player1 = random.randint(1,6)
    total1 = total1 + player1
    
# print("player 1 scored:", total1)

for i in range(10):
    player2 = random.randint(1,6)
    total2 = total2 + player2
    
# print("player 2 scored:", total2)

if total1 > total2:
    print("Player 1 has won!")
elif total1 == total2:
    print("Player 1 and 2 have drawn")
else:
    print("Player 2 has won!")
