#starting field
a = [" "," "," "," "," "," "," "," "," "]
#resets the field
def reset():
    for i in range(len(a)):
        a[i] = " "
#makes a move and draws the frame
def update(x , player):
    while True:
        if(a[x-1] == " "):
            a[x-1] = player
            draw()
            break
        else:
            x = int(input("Essa posiçao já foi jogada, seleciona outra: "))
    
#draws the current frame
def draw():
    print(f"  {a[0]} | {a[1]} | {a[2]}\n____|___|____ \n  {a[3]} | {a[4]} | {a[5]}\n____|___|____  \n    |   |  \n  {a[6]} | {a[7]} | {a[8]}")

#starts a game
def start():
    draw()
    for i in range(9): 
        x = int(input("Seleciona a posicao (1-9): "))
        if(i % 2 == 0):
            update(x,"X")
            if(a[0] != " " and a[0] == a[1] and a[1] == a[2]):
                end("x")
                break
            elif(a[3] != " " and a[3] == a[4] and a[4] == a[5]):
                end("x")
                break
            elif(a[6] != " " and a[6] == a[7] and a[7] == a[8]):
                end("x")
                break
            elif(a[0] != " " and a[0] == a[3] and a[3] == a[6]):
                end("x")
                break
            elif(a[1] != " " and a[1] == a[4] and a[4] == a[7]):
                end("x")
                break
            elif(a[2] != " " and a[2] == a[5] and a[5] == a[8]):
                end("x")
                break
            elif(a[0] != " " and a[0] == a[4] and a[4] == a[8]):
                end("x")
                break
            elif(a[2] != " " and a[2] == a[4] and a[4] == a[6]):
                end("x")
                break
        else:
            update(x,"O")
            if(a[0] != " " and a[0] == a[1] and a[1] == a[2]):
                end("o")
                break
            elif(a[3] != " " and a[3] == a[4] and a[4] == a[5]):
                end("o")
                break
            elif(a[6] != " " and a[6] == a[7] and a[7] == a[8]):
                end("o")
                break
            elif(a[0] != " " and a[0] == a[3] and a[3] == a[6]):
                end("o")
                break
            elif(a[1] != " " and a[1] == a[4] and a[4] == a[7]):
                end("o")
                break
            elif(a[2] != " " and a[2] == a[5] and a[5] == a[8]):
                end("o")
                break
            elif(a[0] != " " and a[0] == a[4] and a[4] == a[8]):
                end("o")
                break
            elif(a[2] != " " and a[2] == a[4] and a[4] == a[6]):
                end("o")
                break
#gameover screen
def end(x):
    player = {
        "x": "Player 1" ,
        "o": "Player 2"
    }
    print("""                                                   
   __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
  / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
  \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
  |___/                                            """)
    print(f"{player[x]} has won!")

#Starts the program
if __name__ == "__main__":
    while True:
        start()
        x = input("Do you want to play again? (y/n): ")
        if x == "y":
            reset()
            continue
        else:
            break

