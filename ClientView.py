
from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
# Declare a global variable for GameFunctions
global GameFunctions

class ClientView:
    def __init__(self, controller):
        self.top_five_players_window = None
        self.top_five_words_window = None
        self.game_UI = None
        self.submitWord = None
        self.username = None
        self.main_menu = None
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("WORDY")
        self.root.geometry('450x200')
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.button = tk.Button(self.root, text="Login", command=self.getLoginCredentials)
        self.button.pack()

    def getLoginCredentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.username = username
        try:
            self.controller.login(username, password)
            self.show_main_menu()
        except Exception as e:
            error_message = str(e.exceptionMessage)
            messagebox.showerror("Login failed", error_message)

    def getUsername(self):
        return self.username

    def show_main_menu(self):
        self.root.destroy()
        self.main_menu = tk.Tk()
        self.main_menu.title("Main Menu")

        # Add main menu elements here
        self.main_menu.title("WORDY - Main Menu")
        self.main_menu.geometry('450x300')

        self.playButton = tk.Button(self.main_menu, text="Play", command=self.play_button_command)
        self.playButton.pack()

        self.topFivePlayersButton = tk.Button(self.main_menu, text="Top 5 Players", command=self.top_five_players_command)
        self.topFivePlayersButton.pack(pady=30)

        self.topFiveWordsButton  = tk.Button(self.main_menu, text="Top 5 Words", command=self.top_five_words_command)
        self.topFiveWordsButton .pack(pady=20)

        self.logOutButton = tk.Button(self.main_menu, text="Log Out", command=self.log_out_command)
        self.logOutButton.pack(pady=30)

        self.main_menu.protocol("WM_DELETE_WINDOW", self.disable_event)
        self.main_menu.mainloop()

    def disable_event(self):
        messagebox.showinfo("Error", "Use the Log Out Button to exit")
        pass
    def log_out_command(self):
        self.controller.logOut(self.getUsername())
        self.main_menu.destroy()
        print("Thank you for using Wordy")

    def show_game_UI(self):
        self.game_UI = tk.Tk()
        self.test = self.controller.bringItOn_command(self.username)
        self.game_UI.title("WORDY - Game")
        self.game_UI.geometry('450x300')
        self.labelLetters = Label(self.game_UI)
        self.labelGame = Label(self.game_UI, text="Form a word with the given letters")
        self.textFieldCharacters = Text(self.game_UI, height= 10, width= 20)
        self.textFieldCharacters.insert(tk.END, self.test)
        self.textFieldCharacters.pack()
        self.labelEnter = Label(self.game_UI, text="Letters change every 10 seconds, keep hitting ENTER to update!")
        self.entryWord = Entry(self.game_UI)

        def submit():
            theWord = self.entryWord.get()
            print(self.getUsername())
            print(theWord)
            self.controller.sendAWord(self.username, theWord)
            self.textFieldCharacters.delete(1.0, tk.END)
            print(self.controller.getTheSeventeenLetters(self.username))
            checkIfWinner = self.controller.getTheSeventeenLetters(self.username)
            self.textFieldCharacters.insert(tk.END, self.controller.getTheSeventeenLetters(self.username),"")
            self.entryWord.delete(0, tk.END)

            if checkIfWinner[0] == "-":
                messagebox.showinfo("Announcement", checkIfWinner)
                self.game_UI.destroy()
                self.reset_play_button()

        self.submitButton = Button(self.game_UI, text= "Enter Word", command=submit)

        self.labelLetters.pack()
        self.labelGame.pack()

        self.labelEnter.pack()
        self.entryWord.pack()

        self.submitButton.pack()
        self.entryWord.bind("<Return>", lambda event: submit())


        def on_closing():
            if self.playButton['text'] == 'Searching...':
                self.reset_play_button()
            self.game_UI.destroy()

        self.game_UI.protocol("WM_DELETE_WINDOW", on_closing)
        self.game_UI.mainloop()

    def get_Letters_command(self):
        print(self.controller.getTheSeventeenLetters(self.getUsername()))

    def play_button_command(self):
        self.playButton.config(text="Searching")
        self.playButton.configure(state="disabled")
        self.main_menu.update_idletasks()
        self.controller.playGame(self.getUsername())

    def reset_play_button(self):
        self.playButton.config(text="Play")
        self.playButton.configure(state="normal")

    def showTopFivePlayersGui(self, topFivePlayers):
        if self.top_five_words_window is not None and self.top_five_words_window.winfo_exists():
            self.top_five_words_window.lift()
            return

        self.top_five_players_window = tk.Toplevel(self.main_menu)
        self.top_five_players_window.title("Top 5 Players")

        # Create a Treeview widget with three columns
        tree = ttk.Treeview(self.top_five_players_window, columns=("Rank", "Player", "Wins"), show="headings")
        tree.column("Rank", width=50)
        tree.column("Player", width=100)
        tree.column("Wins", width=100)
        tree.heading("Rank", text="Rank")
        tree.heading("Player", text="Player")
        tree.heading("Wins", text="Wins")
        tree.pack()

        rank = 0  # Initialize rank to 0
        prev_wins = None
        for player in topFivePlayers:
            if player[2] != prev_wins:
                rank += 1
            tree.insert("", "end", values=(rank, player[1], player[2]))  # Start rank from 1
            prev_wins = player[2]
    def top_five_players_command(self):
        topFivePlayers = self.controller.showTopFivePlayers()
        self.showTopFivePlayersGui(topFivePlayers)
    def top_five_players_command(self):
        topFivePlayers = self.controller.showTopFivePlayers()
        self.showTopFivePlayersGui(topFivePlayers)

    def showTopFiveWordsGUI(self, topFiveWords):

        if self.top_five_words_window is not None and self.top_five_words_window.winfo_exists():
            self.top_five_words_window.lift()
            return

        self.top_five_words_window = tk.Toplevel(self.main_menu)
        # Create a frame to hold the list of top five words.
        frame = tk.Frame(self.top_five_words_window)
        frame.pack()

        # Create a label for the list of top five words.
        label = tk.Label(frame, text="Top 5 Words")
        label.pack()

        tree = ttk.Treeview(self.top_five_words_window, columns=("Rank", "Player", "Word"), show="headings")
        tree.column("Rank", width=50)
        tree.column("Player", width=100)
        tree.column("Word", width=200)
        tree.heading("Rank", text="Rank")
        tree.heading("Player", text="Player")
        tree.heading("Word", text="Word")
        tree.pack()

        # Add the top five words to the listbox.
        for rank, word, player in topFiveWords:
            tree.insert("", "end", values=(rank, player, word))

    def top_five_words_command(self):
        # Get the username from the user
        topFiveWords = self.controller.showTopFiveWords()

        # Display the list of top five words in the GUI.
        self.showTopFiveWordsGUI(topFiveWords)

    def run(self):
        self.root.mainloop()
