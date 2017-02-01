from __future__ import print_function #I added this because it made my life a lot easier when
#the 'end = ...' function was added in the print function that I didn't know a nice way to do
#in Python 2.7, so print statements must all have brackets in this version, no need in the server though
# Echo client program
import socket
import random
import time
import os
import platform


HOST = 'localhost'    # Change this to server IP if running it over the internet

# to act as a client
PORT = 50018              # The server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


# APPLICATION

partnerid = -1 # no partner
numberbidders = 0 # will be given by server
artists = ['Picasso', 'Rembrandt', 'Van_Gogh', 'Da_Vinci']

# DO SOMETHING HERE
# you need to change this to do something much more clever
def determinebid(itemsinauction, winnerarray, winneramount, numberbidders, players, mybidderid, artists, standings, rd):


  """
	EXAMPLE BIDDING ALGORITHM
	Patience is the key here. 
	I'll wait for others to fight it out, 
	and once their funds are depleted I'll use mine to 
	grab the goods.

	I'll make the assumption that:
	IF player A has x money left and 2 of the paintings in that round,
	and IF player B has < x money, player B will bet defensively. 

	The sneaky version of this exploits the first-in winner policy:
	IF player A has x money left and 2 of the paintings in that round,
	wait 5 seconds and THEN bet x+1. I will not implement this as I think it's nasty.
  """

  #Default bit of $5. Hopefully I'll pick up something.
  myBid = 5

  """Archaic: increase default bid each round
  if(standings[mybidderid]['money'] < rd):
	mybid = rd

  """

  #Set up dictionary of most common paintings in first 20 rounds:
  ##First count each painting from round 
  p1 = itemsinauction[0:20].count(artists[0])
  p2 = itemsinauction[0:20].count(artists[1])
  p3 = itemsinauction[0:20].count(artists[2])
  p4 = itemsinauction[0:20].count(artists[3])
  occurrenceDictionary = { artists[0]: p1, artists[1]: p2, artists[2]: p3, artists[3]: p4} 



  #Defensive Strategy

  #Create list to hold the players to look out for
  dangerPlayers = []

  #Count how many players have 2 paintings
  for player in players:
	# If another player has 2 of the current round's item 
	if(standings[player][itemsinauction[rd]] == 2 and player != mybidderid):   
		dangerPlayers.append[player]

  # If there remains a player, not me, who can defensively bid for the painting.
  if(len(dangerPlayers) > 0 and len(dangerPlayers) < len(players)-1 ):
	print("SOME PLAYER HAS 2")
	# Define "other players"
	otherPlayers = []
	for player in players:
	  if (player != dangerPlayers[0] and player != mybidderid):
		  #THIS IS/ARE THE OTHER PLAYERS
		  otherPlayers.append(player)

	# Now, for each other player, can they bid higher than the highest dangerplayer?

	# Create list of possible dangerous bets. 
	# Labelled dangerBids because we're assuming 
	# that anyone with 2 paintings is going all in.
	dangerBids = []

	for player in dangerPlayers:
	  dangerBids.append(standings[player]["money"])

	maxDangerBid = max(dangerBids)

	#List otherplayers who can bid higher than maxDangerBid
	defenders = []
	for player in otherPlayers:
	  if(player[standings]["money"] > maxDangerBid):
	    defenders.append(player)

	# Simple for now, can apply weighting later if necessary.
	# If any player can bid higher, then don't bid.
	if(len(defenders) > 0):
	   # PEACE
	  print("Betting that other ppl will bet defensively for me")
        return int(0)
	else:
	  # WAR (i.e. bet against dose ppl. Probably just postponing the inevitable here though.)
	  print("Betting defensively")
	  return int(maxDangerBid + 1)





print("BIDDING: " + str(myBid))
return int(myBid) #No error checking on this since the bot would not be able to change it's output, so make sure you're sending an integer!
# DATA

mybidderid = input("Input team / player name : ").strip()  # this is the only thing that distinguishes the clients 
while len(mybidderid) == 0 or ' ' in mybidderid:
  mybidderid = input("You input an empty string or included a space in your name which is not allowed (_ or / are all allowed)\n for example Emil_And_Nischal is okay\nInput team / player name: ").strip()

moneyleft = 100 # should change over time
winnerarray = [] # who won each round
winneramount = [] # how much they paid

itemsinauction = []
myTypes = {'Picasso': 0, 'Rembrandt': 0, 'Van_Gogh': 0, 'Da_Vinci': 0, 'money': moneyleft}

# EXECUTION

# get list of items and types
getlistflag = 1
s.send(str(mybidderid).encode('utf-8'))
while(getlistflag == 1):
  # print "Have sent data from ", str(mybidderid)
  data = s.recv(5024)
  x = data.decode('utf-8').split(" ")
  # print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
  #Receives first how many players are in the game and then all 200 items in auction
  if(x[0] != "Not" and len(data) != 0):
    getlistflag = 0
    numberbidders = int(x[0])
    itemsinauction = x[1:]
  else:
    time.sleep(2)

while True:
  s.send((str(mybidderid) + ' ').encode('utf-8'))
  data = s.recv(5024)
  x = data.decode('utf-8').split(" ")
  #Wait until everyone has connected before bidding
  if (x[0] == 'wait'):
    continue
  #When everyone has connected the server knows all names
  #it can therefore transfer all the names after telling the client that it's ready
  players = []
  for player in range(1, numberbidders + 1):
    players.append(x[player])
  break
#Create initial standings for each player after everyone connected
standings = {name: {'Picasso': 0, 'Van_Gogh': 0, 'Rembrandt': 0, 'Da_Vinci': 0, 'money': 100} for name in players}
# now do bids
continueflag = 1
j = 0
if platform.system() == 'Windows':
  os.system('cls')
else:
  os.system('clear')
while(continueflag == 1):
  #roundStart = time.time()
  print(random.choice(["I'm doing my best, okay?", "Why aren't you cheering louder?", "Aren't you proud of me?", "Damn I'm good, and I don't even have a brain!", "And do you think you could do any better?", "I feel like it's me doing all the work, you're just chilling in your chair", "If I lose this it's your fault not mine... I'm doing EXACTLY what you told me to do!"]))
  print()
  bidflag = 1
  bid = determinebid(itemsinauction, winnerarray, winneramount, numberbidders, players, mybidderid, artists, standings, len(winnerarray))
  #sleep before sending the bid to make sure the server is ready, currently it's at a very big value 1
  #this should make it safe for any speed of computers or internet, but can probably be lower as I have had
  #it working on Wifi with my computer at 0.2
  time.sleep(1)
  s.send((str(mybidderid) + " " + str(bid)).encode('utf-8'))
  while(bidflag == 1):
    # print "Have sent data from ", str(mybidderid)
    data = s.recv(5024)
    x = data.decode('utf-8').split(" ")
    # print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
    if(x[0] != "Not"):
      bidflag = 0
    else:
      print("exception")
      time.sleep(2)


  resultflag = 1
  while(resultflag == 1):
    s.send(str(mybidderid).encode('utf-8'))
    # print "Have sent data from ", str(mybidderid)
    data = s.recv(5024)
    x = data.decode('utf-8').split(" ")
    #Wait for all bids to be received
    if (x[0] == 'wait'):
      continue
    # print "Have received response at ", str(mybidderid), " of: ", ' '.join(x)
    #Check if the server told client that game is finished
    if len(x) >= 7 and x[7] == 'won.':
      time.sleep(5)
      continueflag = 0
      resultflag = 0
      print(data)
      print()
      print('game over')
    #Else update standings, winnerarray etc.
    if(x[0] != "ready") and (continueflag == 1):
      #roundLength = time.time()-roundStart
      #time.sleep(max(0, 5-roundLength))
      resultflag = 0
      if platform.system() == 'Windows':
        os.system('cls')
      else:
        os.system('clear')
      # print x
      winnerarray.append(x[0])
      winneramount.append(int(x[5]))
      standings[x[0]]['money'] -= int(x[5])
      standings[x[0]][x[3]] += 1
      if (x[0] == mybidderid):
        moneyleft -= int(x[5])
        myTypes[itemsinauction[j]] += 1
      # update moneyleft, winnerarray
    else:
      time.sleep(2)
  j+= 1
