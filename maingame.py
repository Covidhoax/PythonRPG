import random
import time

def printEmptyLine():
	print ("")
	
def endGame():
	printEmptyLine()	

	if hero.health <= 0:
	    print ("You have failed " +hero.name+ " ,the Kingdom does not belong to you")

	else:
		print ("All hail " +hero.name+ " ,the Kingdom belongs to you now")

def runEndBossStory():
	printEmptyLine()
	print ("After treading through dangerous path" +hero.name+ " finally meets the tyrannical ruler of Arzengoth, " +enemy.name+ ".")
	time.sleep(3)
	print ("Telling " +enemy.name+ ", I am going to destroy you and seize the Arzengoth from you, you evil bastard! You shall face my wrath")
	time.sleep(6)
	print("In reply to the hero, " +enemy.name+ " says... This is is my kingdom and I shall not allow you to have it. I shall have you gutted. Prepare to die bitch!")
	time.sleep(5)
	print("Thus the Battle Begins. For Arzengoth!!!")
	printEmptyLine()

	time.sleep(10)
	print ("Starting Battle in 3...")
    time.sleep(1)
    print ("Starting Battle in 2...")
    time.sleep(1)
    print ("Starting Battle in 1...")
    time.sleep(1)
    print ("Time for BATTLE!")

    printEmptyLine() 		
	runEndBoss()

def runEndBoss():
	enemy.health = 65
	fightDone = False

	selectedWeapon = ["Crossbow", "Sword", "Axe", "Club", "Spear", "Longbow"];
	giveHeroWeapon = random.choice(selectedWeapon)
    giveEnemyWeapon = random.choice(selectedWeapon)

    printEmptyLine()
    print (hero.name+ " pulled out a " +str(giveHeroWeapon)+ "!")
    print (enemy.name+ " pulled out a " +str(giveEnemyWeapon)+ "!")
    printEmptyLine()

    while hero.health <= 100 or enemy.health <=65
    	randomTurn = random.randint(1,10)
    	damageAmount = random.randint(1,20)

    	if randomTurn <= 5 and randomTurn > 0 and fightDone == False:
    		if damageAmount >= 17:
    			print (hero.name+ " attacked " +enemy.name+ " and he took " + str(damageAmount)+ " damage,it was CRITICAL HIT!")
    			enemy.health -= damageAmount
    			time.sleep(2)
    		else:
    			print (hero.name+ " attacked " +enemy.name+ " and he took " +str(damageAmount)+ " damage")
    			enemyHealth -= damageAmount
    			time.sleep(1)
    	elif randomTurn <= 10 and randomTurn > 5 and fightDone == False:
    		if damageAmount >= 17:
    			print (enemy.name+ " attacked " +hero.name+ " and he took " +str(damageAmount)+ " damage, it was CRITICAL HIT")
    			hero.health -= damageAmount
    			time.sleep(1)
    		else:
    			print (enemy.name+ " attacked " +hero.name+ " and he took " +str(damageAmount)+ " damage")
    			hero.health -= damageAmount
    			time.sleep(1)
    	elif fightDone == False and randomTurn < 0 or randomTurn > 20:
    		print("Both the hero and Tyrant missed their attacks")

    	if hero.health <= 0 and enemy.Health > 0 and fightDone == False:
    		fightDone == True

    		printEmptyLine
    		print (hero.name+ " was murdered and gutted by the Mighty " +enemy.name+"!")
    		endGame()
    		break

    	elif enemy.health <= 0 and hero.health >0 and fightDone == False:
    		FightDone == True

			printEmptyLine()
			print (enemy.name + " was butchered by " +hero.name+ " with " +str(hero.health)+ " health left!)
			printEmptyLine()

			endGame()

		elif hero.health > 0 and enemy.health > 0:
			continue	
			
def checkHealth():
	if hero.meat > 0 and hero.water <= 0:
		choice = input("You got " +str(hero.health)+ " hitpoints, You should devour some meat. (Enter meat, continue or explore)" )
		if choice == "meat":
			consume(choice)
		else:
			doAction(Choice)

	elif hero.water > 0 and hero.meat <= 0:
		choice = input("You got " +str(hero.health)+ " hitpoints, You should drink water. (Enter water, continue or explore)")
		if choice == "water":
			consume(choice)
		else:
			doAction(Choice)

	elif hero.water > 0 and hero.meat > 0
		choice = input("You have " +str(hero.health)+ " hitpoints, you should drink water or eat meat(Enter water or meat)")
		if choice == "meat" or "water":
			consume(choice)
		else:
			doAction(choice)

	elif hero.water <= 0 or hero.mear <= 0
		print ("You need healing, but you have no meat or water.")
		printEmptyLine()
		printEmptyLine()
		continuedAction = input("Do you want to explore, continue towards your destination, drink water, eat meat or open inventory?")
		doAction(continuedAction)
	else:
		pass

def consume(food):
	if food == "meat":
		if hero.meat <= 0:
			print ("You have no meat left")
	else:
		hero.health += 60
		hero.meat -= 1

		if hero.health >= 100:
			hero.health = 100

		print ("You ate meat. Now you are stronger and have " +str(hero.health)+ ",hitpoints and " +str(hero.meat)+ " chunk of meat left.")

	printEmptyLine()
	continuedAction = input("Do you want to explore, continue walking towards the destination, eat meat, drink water, or open the inventory?")
	doAction = continuedAction 	 	

	elif food == "water":
		if hero.water <= 0:
			print ("You have no water to drink")
		else:
			hero.health += 40
			hero.water -= 1

		print ("You drank a potion and now you have " +str(hero.health)+ ", hitpoints and " +str(hero.water)+ " flasks of watter left.")

		printEmptyLine()
		continuedAction = input("Do you want to explore, continue walking towards the destination, eat meat, drink water, or open the inventory?")
		doAction = continuedAction

	else:
	pass	
			

			
			
					
			 						
					    		
    		
    		 	
    					
    			
    		
    		
    			
    	
		    
