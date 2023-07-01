import tkinter as tk
import random

def minesweeper():
    def minesweeper_game():
        BOARD_SIZE = int(board_size_entry.get())
        NUM_MINS = int(number_mines_entry.get())

        game_GUI = tk.Toplevel()
        game_GUI.title("Minesweeper")


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

        def print_board():
            frame = tk.Frame(game_GUI)
            frame.pack()

            num_rows = int(BOARD_SIZE)
            num_cols = int(BOARD_SIZE)

            buttons = []

            for row in range(num_rows):
                row_buttons = []
                for col in range(num_cols):
                    button = tk.Button(frame, text="   ")
                    button.grid(row=row, column=col, padx=5, pady=5)
                    row_buttons.append(button)
                buttons.append(row_buttons)


    minesweeper_GUI = tk.Toplevel()
    minesweeper_GUI.title("Minesweeper Start")
    minesweeper_GUI.geometry("250x145")

    minesweeper_header = tk.Label(minesweeper_GUI, text="Minesweeper")
    minesweeper_header.pack()
    boarder_label = tk.Label(minesweeper_GUI, text="----------------")
    boarder_label.pack()

    entry_frame = tk.Frame(minesweeper_GUI)
    entry_frame.pack()

    frame1 = tk.Frame(entry_frame)
    frame1.pack()
    board_size_label = tk.Label(frame1, text="Board Size:")
    board_size_label.pack(side="left", padx=19)
    board_size_entry = tk.Entry(frame1)
    board_size_entry.pack(side="left")
    # frame1.pack()

    frame2 = tk.Frame(entry_frame)
    frame2.pack()
    number_mines_label = tk.Label(frame2, text="Number of Mines:")
    number_mines_label.pack(side="left", pady=5)
    number_mines_entry = tk.Entry(frame2)
    number_mines_entry.pack(side="left")

    start_game_button = tk.Button(minesweeper_GUI, text="Start Game", command=minesweeper_game)
    start_game_button.pack(pady=10)

def hangman():
    hangman_GUI = tk.Toplevel()
    hangman_GUI.title("Hangman")
    hangman_GUI.geometry("250x300")

    #Selects random word
    def get_word():
        words = ["apple", "car", "furniture", "orange", "pear", "while", "patience", "yellow", "now", "there"]
        return random.choice(words)

    def check_function(guess):
        global lives
        global score
        if len(word_letter)>0 and lives >0:
            if guess in alphabet - used_letter:
                used_letter.add(guess)
                word_list = [letter if letter in used_letter else "*" for letter in word]
                word_label.config(text=" ".join(word_list))
                guessed_letters_label.config(text="Guessed Letters: "+" ".join(used_letter))
                if guess in word_letter:
                    word_letter.remove(guess)
                    results_label.config(text=" ")
                    score += 2
                    str_score = str(score)
                    score_label.config(text=str_score)
                else:
                    lives -= 1
                    score -= 2
                    str_lives = str(lives)
                    str_score = str(score)
                    results_label.config(text="Letter is not in word.")
                    lives_label.config(text=str_lives)
                    score_label.config(text=str_score)
            elif guess in used_letter:
                results_label.config(text="You have already used that letter.")
            else:
                results_label.config(text="Invalid charachter please try again.")
        elif lives == 0:
            results_label.config(text="You FAILED!")
        else:
            results_label.config(text="Congratulations you guessed "+word+"!!!")
            used_letter.add(guess)
            word_list = [letter if letter in used_letter else "*" for letter in word]
            word_label.config(text=" ".join(word_list))
            check_button.config(text="Reset", command=hangman)

    #executes two functions from one command
    def execute_function():
        guess = guess_entry.get().lower()
        check_function(guess)
        guess_entry.delete(0, 'end')
    
    def handle_key(event):
        if event.keysym=="Return":
            execute_function()

    word = get_word()
    global word_letter
    word_letter = set(word)
    global alphabet
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    global used_letter
    used_letter = set()
    global word_list
    word_list = [letter if letter in used_letter else "*" for letter in word]
    
    global lives
    lives = 6
    global score
    score = 0

    hangman_header_label = tk.Label(hangman_GUI, text="Hangman")
    hangman_header_label.pack()
    boarder_label=tk.Label(hangman_GUI,text="-------------------")
    boarder_label.pack()
    current_score_label = tk.Label(hangman_GUI, text="Score")
    current_score_label.pack()
    str_score = str(score)
    score_label = tk.Label(hangman_GUI, text = str_score, fg="green")
    score_label.pack()
    available_lives_label = tk.Label(hangman_GUI, text="Available Lives")
    available_lives_label.pack()
    str_lives = str(lives)
    lives_label = tk.Label(hangman_GUI, text=str_lives,fg="red" )
    lives_label.pack()
    global guessed_letters_label
    guessed_letters_label = tk.Label(hangman_GUI, text="Guessed letters: "+" ".join(used_letter))
    guessed_letters_label.pack()
    global word_label
    word_label = tk.Label(hangman_GUI, text=" ".join(word_list))
    word_label.pack()
    guess_entry = tk.Entry(hangman_GUI)
    guess_entry.pack()
    global results_label
    results_label = tk.Label(hangman_GUI, text="")
    results_label.pack()

    check_button = tk.Button(hangman_GUI, text="Check", command=execute_function)
    check_button.pack()

    hangman_GUI.bind("<Return>", handle_key)

def main_menu():
    global hangman
    global minesweeper
    main_menu_GUI = tk.Tk()
    main_menu_GUI.title("Arcade")
    main_menu_GUI.geometry("250x85+100+100")

    welcome_label = tk.Label(main_menu_GUI, text="Welcome to my Arcade!")
    welcome_label.pack()

    hangman_button = tk.Button(main_menu_GUI, text="Hangman", command=hangman)
    hangman_button.pack()

    minesweeper_button = tk.Button(main_menu_GUI, text="Minesweeper", command=minesweeper)
    minesweeper_button.pack(pady=5)

    main_menu_GUI.mainloop()

if __name__ == "__main__":
    main_menu()
