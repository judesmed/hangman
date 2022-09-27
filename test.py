# Solo project of hangman game 26/09/2022

# creation of a class
class Hangman:


    #list of possible string that will be selected  
    ##possible_words: list[str] = ['becode', 'learning', 'mathematics', 'sessions']
    possible_words: list[str] = ['becode']
    #Select a word from the list and unpack the selected word
    import random
    word_to_find = [*random.choice(possible_words)]
    print(word_to_find)
    # number of initial lives of the player
    lives = 5
    correctly_guessed_letters = []
    for letter in word_to_find:
        correctly_guessed_letters.append('_')
    error_count = 0
    turn_count = 0
    Alphabet_letters: list[str] = list('abcdefghijklmnopqrstuvwxyz')
    #list of strings where each element will be a letter guessed by the user.
    
    
    #i will replace an item of the list regarding its index


    #list of strings where each element will be a letter guessed by the user that is not in the word_to_find
    wrongly_guessed_letters: list[str] = []
    #loop 
    while lives > 0:
        print("loop" + str(lives))
        print(correctly_guessed_letters)
        print(word_to_find)
        Guess_letters = input('type a letter')
        # check if letter is part of alphaet en not already logged
        Turns_letters = correctly_guessed_letters + wrongly_guessed_letters
        if  Guess_letters in Turns_letters:
            print(Guess_letters +" has already be used")
        elif Guess_letters not in Alphabet_letters:
            print(Guess_letters +" is not a letter")

        else:
            ## def play(Guess_letters,lives,correctly_guessed_letters,word_to_find)
            #the letter is in the selected word and has not been already selected
            if Guess_letters in word_to_find:
                indexes: list[int] = []
                index = 0
                for letter in word_to_find:
                    if letter == Guess_letters:
                        indexes.append(index)
                    index += 1    
                #add the new letter in the correctly_guessed_letters list
                for index in indexes:
                    correctly_guessed_letters[index] = Guess_letters
                # check if correctly_guessed_letters = word_to_find
                ##well_played(correctly_guessed_letters,word_to_find):
                if correctly_guessed_letters == word_to_find:
                    print('yheaaaa'+str(correctly_guessed_letters) + str(wrongly_guessed_letters) + str(lives)+ str(error_count)+str(turn_count))
            # add the letter to the wrongly_guessed_letters list  
            else:
                wrongly_guessed_letters.append(Guess_letters)
                lives -= 1
                error_count += 1
                ## game_over(lives)
                if lives == 0:
                    print('game over ...')
            turn_count += 1
            print(str(correctly_guessed_letters) + str(wrongly_guessed_letters) + str(lives)+ str(error_count)+str(turn_count))





