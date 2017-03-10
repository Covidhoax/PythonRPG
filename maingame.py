import random

def printEmptyLine():
	print ("")
	
def endGame():
	printEmptyLine()	

	if hero.health <= 0:
	    print ("You have failed" +hero.name+ " ,the Kingdom does not belong to you")

	else:
		print ("All hail" +hero.name+ " ,the Kingdom belongs to you now")
		    
