import itertools
import random
#import pandas as pd

class Cards:
     
     def __init__(self):
        self.suits = ['Spades','Hearts','Diamonds','Clubs']
        self.values = range(1,14)
        self.actualcards = [] #Empty List to Append
        for card in itertools.product(self.suits,self.values):
                self.actualcards.append(card) #Cartesian Product to Create Deck
     
     def Getrandomcard(self):
         Randomnumber = random.randint(0,51)
         Cardtobereturned = self.actualcards[Randomnumber] #Generates Random Card
         return(Cardtobereturned)

class Player:
     
     def __init__(self,ID,Card,Point):
         self.Playerid = ID
         self.Cardforplayer = Card
         #self.Point = list()

class Game:
     
     def __init__(self,Nameofgame):
         self.name = Nameofgame

class Simplegame():
     
     def __init__(self,Numberofplayers):
         self.Numberofplayers = Numberofplayers
         self.Playerlist = []
         self.Gameconfig = {
         1:52,
         2:26,
         3:17,
         4:13
         }
         self.Pointdict = {}

     def Startgame(self):
         utilised_cards = list()
         iteration = 0
         Deckofcards = Cards()
         for i in range(self.Gameconfig[self.Numberofplayers]):#change here
             for playerid in range(1,self.Numberofplayers+1):
                 #print(utilised_cards)
                 Cardforplayer = Deckofcards.Getrandomcard() #Deal Card to Player
                 while (Cardforplayer in utilised_cards):
                     Cardforplayer = Deckofcards.Getrandomcard()
                 utilised_cards.append(Cardforplayer)
                 Newplayer = Player(playerid,Cardforplayer,'''Point''') #Save Player ID and Card
                 self.Playerlist.append(Newplayer)
             self.Decidewinner()
         #print(utilised_cards)
     
     def Decidewinner(self):
         Winningid = self.Playerlist[0] #Choose Player 0 as Potential Winner
         for playerid in self.Playerlist:
             if(playerid.Cardforplayer[1]>Winningid.Cardforplayer[1]):
                 Winningid = playerid #Find the Player with Highest Card
         #print Winningid.Playerid
         self.Pointdict[Winningid.Playerid] = self.Pointdict.get(Winningid.Playerid, 0) + 1
         #if Winningid.Playerid in Pointdict:
             #(Winningid.Playerid) += 1
        # else:
        #    (Winningid.Playerid) = 1
         print ("Winner is Player " +str(Winningid.Playerid))
         print ("Winning Card was " +str(Winningid.Cardforplayer[1])+"of"+str(Winningid.Cardforplayer[0]))

         self.Playerlist = list()
         print (self.Pointdict)
         

if __name__=="__main__":
     Totalplayers = int(input("Enter number of players\n"))

     if 1 < Totalplayers < 5:
         print ("You are playing with", Totalplayers - 1,"Other Players\n")
         New = Simplegame(Totalplayers)
         New.Startgame()

     else:
         print ("You cannot play with less than 1 and Greater than 4 Players")


