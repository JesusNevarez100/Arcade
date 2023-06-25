import random

def main_menu():
    
    print("      Menu      ")
    print("--------------------")
    print("1) Hangman")
    print("2) Minesweeper")
    print("3) Stats")
    print("4) About")
    print("5) Exit")
    print("--------------------")

    # User selects what he wants to do in the arcade
    while True:
        print(" ")
        menu_input = input("Please pick an option: ").lower()
        if menu_input == "1" or menu_input == "Hangman" or menu_input == "1) Hangman":
            hangman()
        elif menu_input == "2" or menu_input == "Minesweeper" or menu_input == "2) Minesweeper":
            minesweeper()
        elif menu_input == "3" or menu_input == "Stats" or menu_input == "3) Stats":
            stats()
        elif menu_input == "4" or menu_input == "About" or menu_input == "4) About":
            about()
        elif menu_input == "5" or menu_input == "Exit" or menu_input == "5) Menu":
            print("Fairwale Player!")
            print("Prizes will await next time you log in")
            quit()
        else:
            main_menu()

def hangman():
    # Picks a random word from a list of words
    def get_word():
        words = ["apple", "car", "furniture", "orange", "pear", "while", "patience", "yellow", "now", "there"]
        return random.choice(words)
    # Calls word get_word function
    word = get_word()
    # To remember word, and to keep track of used letters
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()

    # Reveals times played, wins, and losses
    with open("times_played_hangman.txt") as times_played:
        counts = times_played.readlines()
    code_runs = int(counts[0])
    wins = int(counts[1])
    losses = int(counts[2])
    code_runs += 1

    print(" ")
    print("     Hangman     ")
    print("-----------------")
    lives = 6
    score = 0
    while len(word_letters) > 0 and lives > 0:
        print(" ")
        print("Score: ", score)
        print("Incorrect guess left: ", lives)
        print("Incorrect guess letters: ", " ".join(used_letters))

        # List comprehenssion is used to reveal used letter in hidden word. 
        word_list = [letter if letter in used_letters else "*" for letter in word]
        print(" ".join(word_list))

        # User input for letter
        user_letter = input("Guess a letter: ").lower()
        # If the input is valid it gets added to the list of used letters
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # The user letter gets removed from the set of letters called word_letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                score += 2
            else:
                lives -= 1
                score -= 2
                print("Letter is not in word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Guess anohter one.")
        else:
            print("Invalid character. Please try again.")
    # Game over
    if lives == 0:
        print("Sorry, you died. The word was", word)
        losses += 1
    # Win
    else:
        print("Congratulations! You guessed the word", word,"!!")
        print("Your score is", score)
        wins += 1   
        # Score are recorded using text files so that they are easier to acces in the stats function
        with open("hangman_high_score.txt", "r") as current_score:
            for line in current_score:
                number = line.strip()
                if "." in number:
                    number = float(number)
                else:
                    number = int(number)
                if score > number:
                    with open("hangman_high_score.txt", "w") as new_high_score:
                        new_high_score.write("{}".format(score))
        # Record new low score               
        with open("hangman_low_score.txt", "r") as w:
            for line in w:
                number = line.strip()
                if "." in number:
                    number = float(number)
                else:
                    number = int(number)
                if score < number:
                    with open("hangman_low_score.txt", "w") as new_low_score:
                        new_low_score.write("{}".format(score))

                       
    # Record code_runs\wins\losses
    with open("times_played_hangman.txt", "w") as times_played:
        times_played.write(f"{code_runs}\n{wins}\n{losses}")

    # Prompt to play again
    print("Would you like to play again? (Y/N)")
    play_again_input = input("> ").lower()
    if play_again_input == "y":
        hangman()
    elif play_again_input == "n":
        main_menu()

def minesweeper():
    # Board constants
    BOARD_SIZE = 5
    NUM_MINES = 3
    score = 0

    # Revela times plays, wins, and losses
    with open("times_played_minesweeper.txt", "r") as times_played:
        counts = times_played.readlines()
    code_runs = int(counts[0])
    wins = int(counts[1])
    losses = int(counts[2])


    print("Welcome to Minesweeper! ")

    # Create the board
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


    # Place the mines randomly on the board
    for _ in range(NUM_MINES):
        row = random.randint(0, BOARD_SIZE-1)
        col = random.randint(0, BOARD_SIZE-1)
        board[row][col] = -1

    # Fill in the board with the number of mines
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == -1:
                continue

            count = 0
            for r in range(max(0, row - 1), min(row + 2, BOARD_SIZE)):
                for c in range(max(0, col - 1), min(col + 2, BOARD_SIZE)):
                    if board[r][c] == -1:
                        count += 1
            board[row][col] = count

    # Create a helper function to print the board
    def print_board(reveal=False):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if reveal:
                    print(str(board[row][col]).rjust(2), end=" ")
                elif flagged[row][col]:
                    print("F", end=" ")
                else:
                    print("O"if not revealed[row][col] else str(board[row][col]).rjust(2), end=" ")
            print()

    # Create a helper function to recursively reveal the board when the user selects a cell
    def reveal_board(row, col):
        if revealed[row][col]:
            return


        revealed[row][col] = True

        if board[row][col] == -1:
            # Game over
            print("Game over!")
            # Reveal code_runs\wins\losses
            with open("times_played_minesweeper.txt", "r") as read_file:
                counts = read_file.readlines()
            code_runs = int(counts[0])
            wins = int(counts[1])
            losses = int(counts[2])
            code_runs += 1
            losses += 1
            # Record new low score
            with open("Minesweeper_low_score.txt", "r") as w:
                for line in w:
                    number = line.strip()
                    if "." in number:
                        number = float(number)
                    else:
                        number = int(number)
                    if score < number:
                        with open("Minesweeper_low_score.txt", "w") as new_low_score:
                            new_low_score.write("{}".format(score))
            print_board(reveal=True)
            # Record code_runs\wins\losses
            with open("times_played_minesweeper.txt", "w") as recording_losses:
                recording_losses.write(f"{code_runs}\n{wins}\n{losses}\n")
            # Play again Boolean
            print("Would you like to play again? (Y/N)")
            play_again_input = input("> ").lower()
            if play_again_input == "y":
                minesweeper()
            elif play_again_input == "n":
                main_menu()
        elif board[row][col] == 0:
            # Recursively reveal neighboring cells
            for r in range(max(0, row-1), min(row + 2, BOARD_SIZE)):
                for c in range(max(0, col-1), min(col + 2, BOARD_SIZE)):
                    reveal_board(r, c)


    # Create a 2D array to keep track of which cells have been revealed
    revealed = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    flagged = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    Flags = 3

    # Play the game
    while True:
        # Number of flags
        print("Flags left: ", Flags)
        print_board()
        # User Input
        row = int(input("Enter Row: "))
        col = int(input("Enter Colum: "))
        
        # User Action
        action = input("Enter 'r' to reveal, 'f' to flag/unflag: ")

        if Flags == 0:
                print("Sorry no more flags!")
                continue
        elif action == "r":
            # Reveal Cell
            score += 1
            reveal_board(row, col)
        elif action == "f":
            # Flag Cell
            score += 1
            Flags -= 1
            flagged[row][col] = not flagged[row][col]
        else:
            print("Invalid action, try agin.")
            continue
      
        if all(revealed[row][col] or board[row][col] == -1 for row in range(BOARD_SIZE) for col in range(BOARD_SIZE)):
            # Game won
            print_board(reveal=True)
            print("You won!")
            print(" ")
            code_runs += 1
            wins += 1
            # Record new high score
            with open("Minesweeper_high_score.txt", "r") as current_score:
                for line in current_score:
                    number = line.strip()
                    if "." in number:
                        number = float(number)
                    else:
                        number = int(number)
                    if score > number:
                        with open("Minesweeper_high_score.txt", "w") as new_high_score:
                            new_high_score.write("{}".format(score)) 
            # Record new low score              
            with open("Minesweeper_low_score.txt", "r") as w:
                for line in w:
                    number = line.strip()
                    if "." in number:
                        number = float(number)
                    else:
                        number = int(number)
                    if score < number:
                        with open("Minesweeper_low_score.txt", "w") as new_low_score:
                            new_low_score.write("{}".format(score))
            # Record code_runs\wins\losses
            with open("times_played_minesweeper.txt", "w") as times_played:
                times_played.write(f"{code_runs}\n{wins}\n{losses}")

            print("Would you like to play again? (Y/N)")
            play_again_input = input("> ").lower()
            if play_again_input == "y":
                minesweeper()
            elif play_again_input == "n":
                main_menu()

def stats():
    def hangman_stats():
        print("     Hangman     ")
        print("-----------------")
        # Stats are simply pulled from txt files
        # Theses stats are for the high and lows scores
        with open("hangman_high_score.txt", "r") as read_file:
            print("High Score: ", read_file.read())
        with open("hangman_low_score.txt", "r") as read_file:
            print("Low Score: ", read_file.read())
        with open("times_played_hangman.txt", "r") as times_played:
            counts = times_played.readlines()

        code_runs = int(counts[0])
        wins = int(counts[1])
        losses = int(counts[2])

        # The percentage of wins and losses is simply the wins or losses over the times the code has be run 
        percent_wins = (wins/code_runs)*100
        percent_losses = (losses/code_runs)*100

        # Stats for times played or % wins and losses
        print("Games Played: ",code_runs)
        print("{}% Wins, {}% Losses".format(percent_wins, percent_losses))
    def minesweeper_stats():
        print("     Minesweeper     ")
        print("-----------------")
        # Stats are simply pulled from txt files
        # Theses stats are for the high and lows scores
        with open("Minesweeper_high_score.txt", "r") as read_file:
            print("High Score: ", read_file.read())
        with open("Minesweeper_low_score.txt", "r") as read_file:
            print("Low Score: ", read_file.read())
        with open("times_played_minesweeper.txt", "r") as times_played:
            counts = times_played.readlines()

        code_runs = int(counts[0])
        wins = int(counts[1])
        losses = int(counts[2])

        # The percentage of wins and losses is simply the wins or losses over the times the code has be run 
        percent_wins = (wins/code_runs)*100
        percent_losses = (losses/code_runs)*100

         # Stats for times played or % wins and losses
        print("Games Played: ",code_runs)
        print("{}% Wins, {}% Losses".format(percent_wins, percent_losses))

    hangman_stats()
    print(" ")
    minesweeper_stats()

def about():
    print("Terminal Arcade Pack Developed by Jesus Nevarez for CSE107 2023")

def main():
    print("Welcome Player!!")
    main_menu()

if __name__ == "__main__":
    main()