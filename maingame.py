import random

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
			printEmptyLine

			endGame()

		elif hero.health > 0 and enemy.health > 0:
			continue	
			
    		
    		
    		 	
    					
    			
    		
    		
    			
    	
		    
