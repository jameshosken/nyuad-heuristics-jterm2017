#Best change problem

"""
	How can a given amount of money be made with the least number of coins of given denominations 
	
	Let's break it down. You will be given 2 things: 
	1) A list of 3 coins of certain denominations (e.g. 1c,5c,10c)
	2) A certain amount of money.
	
	Goal: You have to figure out how to get to that amount using the least number of coins.
	
	Go.
"""

## "Biggest First" solution:
"""
	This solution looks at the highest possible coin value that can fit into the number, and uses it.
	If there's still change left, it tries again.
"""



denominations = [1,5,10, 25, 50]

def biggestFirst(targetamount):
	currentamount = 0		#This keeps a running total of the coins added together
	coinlist = []			#This keeps a list of all the coins we're using to reach the target.
	round = 0				#This will keep track of how many coins we are using.
							#The "round" is just to be explicit, because we could also check the len() of coinlist.
	
	#if the target amount is already a coin, just use that coin.
	if targetamount in denominations:
		return targetamount		#Return will quit this function, and nothing more in here will happen.
	

	#.sort() sorts list from lowest to highest
	denominations.sort()
	
	while currentamount < targetamount:
		
		#Now we loop through the sorted denominations, 
		#and find the first value that will fit into the target.
		
		for coinvalue in denominations[::-1]:		#Here we're going through the sorted list BACKWARDS (high to low)
			
			if(coinvalue+currentamount <= targetamount):		# Make sure we don't go over the target.
				#Keep track of what's happening:
				#print str(coinvalue) + " fits!"
				#Append current coin value to our list of coins:
				coinlist.append(coinvalue)
				#Add this coin's value to the running total:
				currentamount = currentamount + coinvalue
				#Add 1 to the number of coins
				round = round + 1
				#print "We have: " + str(round) + " + coins so far"
				#Finally, quit this for loop to start a new 'round'
				break	#Break
			else:
				#This just means keep on going with the for loop.
				continue
	#After the while loop, return the list of coins
	return coinlist
		

#change = biggestFirst(23)

for x in range(100):
	print (biggestFirst(x))