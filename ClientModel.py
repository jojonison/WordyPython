
import sys
import common
from omniORB.ami import CORBA

from tkinter import messagebox


class ClientModel:


    def __init__(self):
        # Initialize the client model
        pass

    def login(self,username,password):
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        obj = orb.string_to_object("corbaname::localhost:9999#Conn")
        GameFunctions = obj._narrow(common.GameFunctions)

        GameFunctions.logIn(username, password)
        messagebox.showinfo("Login successful", "Welcome to WORDY!")

    def showTopFivePlayers(self):
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        obj = orb.string_to_object("corbaname::localhost:9999#Conn")
        game_functions = obj._narrow(common.GameFunctions)

        top_players_sequence = game_functions.getTopFivePlayers()
        sorted_top_players = sorted(top_players_sequence, key=lambda x: x.numberOfWins, reverse=True)

        top_players = []
        rank = 0  # Initialize rank to 0
        prev_wins = None
        for tp in sorted_top_players:
            if tp.numberOfWins != prev_wins:
                rank += 1
            top_players.append((rank, tp.username, tp.numberOfWins))
            prev_wins = tp.numberOfWins
        return top_players


    def showTopFiveWords(self):
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        obj = orb.string_to_object("corbaname::localhost:9999#Conn")
        GameFunctions = obj._narrow(common.GameFunctions)

        topFiveWordsObj = GameFunctions.getTopFiveLongestWords()
        topFiveWords = [(tw.rank, tw.theWord, tw.username) for tw in topFiveWordsObj]
        return topFiveWords

    def playGame(self, username):
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        obj = orb.string_to_object("corbaname::localhost:9999#Conn")
        GameFunctions = obj._narrow(common.GameFunctions)
        game_id = GameFunctions.playGame(username)

        return game_id

    def logOut(self, username):
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        obj = orb.string_to_object("corbaname::localhost:9999#Conn")
        GameFunctions = obj._narrow(common.GameFunctions)

        GameFunctions.logOut(username)

    def getTheSeventeenLetters(self,username):
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        obj = orb.string_to_object("corbaname::localhost:9999#Conn")
        GameFunctions = obj._narrow(common.GameFunctions)

        return GameFunctions.getTheSeventeenLetters(username)

    def sendAWord(self,username,word):
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        obj = orb.string_to_object("corbaname::localhost:9999#Conn")
        GameFunctions = obj._narrow(common.GameFunctions)

        GameFunctions.sendAWord(username,word)

    def bringItOn(self, username):
        orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
        obj = orb.string_to_object("corbaname::localhost:9999#Conn")
        GameFunctions = obj._narrow(common.GameFunctions)

        return GameFunctions.bringItOn(username)

