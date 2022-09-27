# Solo project of hangman game 26/09/2022

# Creation of a class
import random
class Hangman():
    '''Class Hangman call different methods in order to play hangman game.
    :Methods :
        play(): ask user to fill an imput and check whether or not that input is in the string that has to be found.
        start-the_game(): launch the game en stop it if failed or win.
        well_played(): stop the game if Win
        game_over(): stop the game when player fail.
    :Attributes: 
        random_words: list of string randomly extracted from random_words.txt.
        possible_words: list of string'''
    # List of random words.
    random_words: list[str] = open('random_words.txt', 'r').read().lower().split('\n')
    possible_words: list[str] = ['becode', 'learning', 'mathematics', 'sessions']

    def __init__(self):
        '''The function set the initial default parameters
        Attributes :
            word_to_find: list[str] containing each letter of the random selected word.
            correctly_guessed_letters: list[str] that will be fill up with a str during the game for each correct guess.
            wrongly_guessed_letters: list[str] that will be fill up with a str during the game for each wrong guess.
            turn_count: int = 0  +1 per turn.
            error_count: int = 0 +1 per error entry.
            lives: int = 5 -1 per error entry'''

        self.word_to_find: list[str] = [*random.choice(self.possible_words)]
        self.correctly_guessed_letters: list[str] = list("_"*len(self.word_to_find))
        self.wrongly_guessed_letters: list[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
        self.lives: int = 5

    # Play function that will either fill the correctly_guessed_letters if the input is correct then turn will be increase by 1 \
    #  otherwise the input is wrong en lifes is decreased by one en error_count is increase by one.
    def play(self) -> list[str] | str:
        '''Function calling for an imput. check if input is one alphabetical letter end if it is yes or not in the word_to_find, depending of the output it update it's parameters.
        Attributes :
            word_to_find: list[str] containing each letter of the random selected word.
            correctly_guessed_letters: list[str] that will be fill up with a str during the game for each correct guess.
            wrongly_guessed_letters: list[str] that will be fill up with a str during the game for each wrong guess.
            turn_count: int = 0  +1 per turn.
            error_count: int = 0 +1 per error entry.
            lives: int = 5 -1 per error entry'''

        Guess_letters = input('Type one letter: ').lower()
        Turns_letters = self.correctly_guessed_letters + self.wrongly_guessed_letters
        if  Guess_letters in Turns_letters:
            print(Guess_letters +" has already be used")
        elif Guess_letters.isalpha() == False:
            print(Guess_letters +" is not a letter")
        elif len(Guess_letters)>1:
            print('Please input one letter only !')
        else:
            # If the letter is correct it will be add at it's right location regarding the word_to_find using index location
            if Guess_letters in self.word_to_find:
                indexes: list[int] = []
                index = 0
                for letter in self.word_to_find:
                    if letter == Guess_letters:
                        indexes.append(index)
                    index += 1    
                # Add the new letter in the correctly_guessed_letters list
                for index in indexes:
                    self.correctly_guessed_letters[index] = Guess_letters
            # add the letter to the wrongly_guessed_letters list  
            else:
                self.wrongly_guessed_letters.append(Guess_letters)
                self.lives -= 1
                self.error_count += 1
            self.turn_count += 1

    # Function that loop the game until it end (in case of game over or win)en each loop print the current game attribute, 
    def start_game(self):
        '''function calling it's function en printing the curent status of its the parameter en if the game win or fail it stop the game.
            :Methods :
        play(): ask user to fill an imput and check whether or not that input is in the string that has to be found.
        well_played(): stop the game if Win
        game_over(): stop the game when player fail.
            :Attributes:
                correctly_guessed_letters: list[str] that will be fill up with a str during the game for each correct guess.
                wrongly_guessed_letters: list[str] that will be fill up with a str during the game for each wrong guess.
                turn_count: int = 0  +1 per turn.
                error_count: int = 0 +1 per error entry.
                lives: int = 5 -1 per error entry'''
        # While the game is not finished the loop continue.
        while self.correctly_guessed_letters != self.word_to_find or self.lives > 0:
            # If guess word correspond to the word to find  run well_played() function then break
            if self.correctly_guessed_letters == self.word_to_find:
                print(self.well_played())
                break
            # If lives = 0 run game_over() then break
            elif self.lives == 0:
                print(self.game_over())
                break
            # If none of the up conditions run play() en then print string
            else:
                self.play()
                print(f'Correct letters: {self.correctly_guessed_letters},\
                \n Wrong letters: {self.wrongly_guessed_letters},\
                \n Lives left: {self.lives},\
                \n Nbr of errors: {self.error_count},\
                \n Nbr of turns: {self.turn_count}.')
            
    def well_played(self) -> str:
        '''
        Function returning that the player win the game, with his scores.
        Attributes :
            word_to_find: list[str] containing each letter of the random selected word.
            turn_count: int = 0  +1 per turn.
            error_count: int = 0 +1 per error entry.'''

        return f'You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!'
    
    def game_over(self) -> int:
        '''function that will stop the game and print 'game over ...' '''
        return 'game over ...'