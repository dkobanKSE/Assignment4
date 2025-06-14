import random

def guessing(guess, word):     
    result, i = "", 0
    
    while i < len(word):
        char_of_guess = guess[i]
        
        if char_of_guess == word[i]:
            result += f' [{char_of_guess.upper()}]'
            i += 1
        
        elif char_of_guess in word:
            result += f' ({char_of_guess})'
            i += 1
        
        else:
            result += f' {char_of_guess}'
            i += 1

    return result

def creat_word() -> str:
    words = ['apple', 'bread', 'candy', 'dream', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']
    x = random.randint(0, len(words) - 1)
    secret_word = words[x]
    
    return secret_word    
 
def char_is_str(guess):
    factor = False
    
    factor = any(char_of_guess.isdigit() for char_of_guess in guess)
    
    spes_char = ['{','}',',','.','/','|','?','!','-','+','=','[',']','#','@','\\']
    for chars in guess:
        if chars in spes_char:
            factor = True
            
    return factor
     
 
def main():

    secret_word = creat_word()
    
    tries = 6
    
    print("Welcome to Wordle!")
    print("Guess the",len(secret_word),"- letter word. You have", tries, "tries.")
    
    while tries != 0: 
        try: 
            guess = input("Attempt "+str(7 - tries)+"/6 – Enter guess: ").lower().replace(" ", "")
        
            if guess == secret_word:
                print("You win!!!")
                break
            
            if char_is_str(guess) == True:
                print("Write only letters in your word")
                continue
        
            print(f'Result: {guessing(guess, secret_word)}')
            tries -= 1
            
        except IndexError:
            print(f'Write a {len(secret_word)}-word')
            continue
        
        
        if tries == 0: print(f'You lost \nWord was - {secret_word}')


while True: 
    start_game = input("Do you want to play WORDLE? (y/n) - ").lower()
    
    if start_game == 'n':
        print("Goodbye!")
        break
    
    elif start_game != "y" and start_game != "n":
        print("Write only n(no) or y(yes)")
        continue
    
    main()