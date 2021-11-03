
import random
def art(x):
    arts = {
        6 : """
    --- +
    |   |
        |
        |
        |
===========""",
        5 : """
    --- +
    |   |
    O   |
        |
        |
===========""",
        4 : """
    --- +
    |   |
    O   |
    |   |
        |
===========""",
        3 : """
    --- +
    |   |
    O   |
    |\  |
        |
===========""",
        2 : """
    --- +
    |   |
    O   |
   /|\  |
        |
===========""",
        1 : """
    --- +
    |   |
    O   |
   /|\  |
     \  |
===========""",
        0 : """
    --- +
    |   |
    O   |
   /|\  |
   / \  |
===========""",
    }
    print(arts[x])


word_list = open("hangman/word_list.txt").read().split()







def start():

    print("""                                            
  /\  /\__ _ _ __   __ _  /\/\   __ _ _ __  
 / /_/ / _` | '_ \ / _` |/    \ / _` | '_ \ 
/ __  / (_| | | | | (_| / /\/\ \ (_| | | | |
\/ /_/ \__,_|_| |_|\__, \/    \/\__,_|_| |_|
                   |___/                    """)
    random_word = random.choice(word_list)
    obscured_word = []
    for char in random_word:
        obscured_word.append("?")

    lives = 6
    while "?" in obscured_word:
        guess = input("\n\nGuess a leter:")
    
        if guess in random_word:
            x = 0
            a = ""
            for i in random_word:
                if guess == i :
                    obscured_word[x] = i
                x += 1
        
            for i in range(len(obscured_word)):
                a += obscured_word[i]
            print(a)
        else:
            a = ""
            lives -= 1
            art(lives)
            for i in range(len(obscured_word)):
                a += obscured_word[i]
            print(a)
            if lives == 0:
                print("""                  __           _   
/\_/\___  _   _  / /  ___  ___| |_ 
\_ _/ _ \| | | |/ /  / _ \/ __| __|
 / \ (_) | |_| / /__| (_) \__ \ |_ 
 \_/\___/ \__,_\____/\___/|___/\__|
                                   """)
                print(f'The word was "{random_word}"')
                exit()
    print("""                __    __            
/\_/\___  _   _/ / /\ \ \___  _ __  
\_ _/ _ \| | | \ \/  \/ / _ \| '_ \ 
 / \ (_) | |_| |\  /\  / (_) | | | |
 \_/\___/ \__,_| \/  \/ \___/|_| |_|
                                    """)

        



start()

