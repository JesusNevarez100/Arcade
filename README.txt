Purpose:
    The purpose of the final project is to create a terminal arcade that can play the classic games Hangman and Minesweeper.
    When loading up the game you are greeting with a wellcome and a Main Menu, from the Main Menu you can choose
    to play Hangman or Minesweeper by inputing 1 for Hangman or 2 for Minesweeper. From this same menu you have 
    the option to view stats, view the creators, or leave the game with a farewell message. 
    When playing Hangman, you will be recursivley given your current score, lives, and guessed letter,
    the length of your word is given in astrics. This is done by grabbing a word from a predefined 
    list, and passing it thoruogh a list comprehenssion loop, where the letters are replaced by astrics.
    If the user inputs a letter, and the if letter is not in the list comprehension word,
    a boolean statement will add the letter to a guessed word list, and no letter is revealed.
    If the user inputs a letter, and the if letter is in the list comprehension word, the letter is revealed,
    and the letter is added to the used letters list.
    While playing Minesweeper, the user is asked to to enter a Y coordinate as a row, and a X cordinate and column.
    The user is then asked to input either r to reveal the working cell, or f to flag the suspicios cell.
    If the user reveales the cell and there is a bonb under that cell the game ends.
    If the user reveales the cell and ther is not a bomb the reveal board function will recursivley reveal
    all cell that do not have a bomb. The board is created using list comprihension given the BOARD_SIZE.
    The mines are randomly placed using the reandom library and some for statements and if statesments as booleans.
    In the reveal_board function, the user inputs are passed through the board list comprehension.

    Main Menu Comands:
    The following commans should be enter when prompted. 
    - "1" or "Hangman" or "1) Hangman" for Hangman   
    -"2" or "Minesweeper" or "2) Minesweeper" for Minesweeper
    - "3" or "Stats" or "3) Stats" for Stats
    - "4" or "About" or "4) About" for About
    - "5" or "Exit" or "5) Exit" for Exit

    Hangman Commands:
    The following commans should be enter when prompted. 
    - "abcdefghijklmnopqrstuvwxyz" for Guess a letter promtpt
    - "y" or "Y" for yes in Would like to play again? (Y/N) prompt
    - "n" or "N" for no in Would like to play again? (Y/N) prompt

    Minesweeper Comands:
    The following commans should be enter when prompted. 
    - "0-4" for Enter Row, or Y axis Prompt, 0 being 1, and 4 being 5
    - "0-4" for Eneter Column, or X axis Prompt, 0 being 1, and 4 being 5
    - "r" to reveal cell selected cell when prompted
    - "f" to reveal cell selected cell when prompted 
    - "y" or "Y" for yes in Would like to play again? (Y/N) prompt
    - "n" or "N" for no in Would like to play again? (Y/N) prompt

    
