
from tkinter import messagebox
from ClientView import ClientView

class ClientController:
    def __init__(self, model):
        self.model = model
        self.isGameStarted = False
        self.client_view = ClientView(self)

    def sendAWord(self,username,word):
        try:
            self.model.sendAWord(username,word)
        except:
            print(":)")


    def getTheSeventeenLetters(self,username):
        return self.model.getTheSeventeenLetters(username)


    def login(self, username, password):
        self.model.login(username, password)


    def playGame(self, username):
        game_id = self.model.playGame(username)
        if game_id != -1:
            self.isGameStarted = True
            self.client_view.show_game_UI()
            # print(self.model.bringItOn(username))
        elif game_id == -1:
            messagebox.showinfo("Error","Not enough players to play the game")
            self.client_view.reset_play_button()


    def bringItOn_command(self, username):
        return self.model.bringItOn(username)

    def showTopFivePlayers(self):
            top_players = self.model.showTopFivePlayers()
            return top_players


    def showTopFiveWords(self):
        # Get the list of top five words from the server.
        topFiveWords = self.model.showTopFiveWords()

        # Display the list of top five words in the GUI.
        self.client_view.showTopFiveWordsGUI(topFiveWords)

    def logOut(self,username):
        self.model.logOut(username)

    def run(self):
        self.client_view.run()