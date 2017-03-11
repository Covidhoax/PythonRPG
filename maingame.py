import random
import time

def printEmptyLine():
    print ("")

def endGame():
    printEmptyLine()

    if hero.health <= 0:
        print ("You have failed! " +hero.name+ "!, and you shall never have the Arzengoth")
    else:
        print ("All Hail " +hero.name+ "! as he has defeated " +enemy.name+ " and took over the Arzengoth, although, it is said that," +hero.name+ " turned out to be more evil than " +enemy.name)

def runEndBossStory():
    printEmptyLine()
    print ("After treading through dangerous path" +hero.name+ " finally meets the tyrannical ruler of Arzengoth, " +enemy.name+ ".")
    time.sleep(2)
    print ("Telling " +enemy.name+ ", I am going to destroy you and seize the Arzengoth from you, you evil bastard! You shall face my wrath")
    time.sleep(5)
    print("In reply to the hero, " +enemy.name+ " says... This is is my kingdom and I shall not allow you to have it. I shall have you gutted. Prepare to die bitch!")   
    time.sleep(5)
    print("For Arzengoth!")
    printEmptyLine()

    time.sleep(10)
    print ("Starting Fight in 3...")
    time.sleep(1)
    print ("Starting Fight in 2...")
    time.sleep(1)
    print ("Starting Fight in 1...")
    time.sleep(1)
    print ("TIME FOR BATTLE!!!")

    printEmptyLine()
    runEndBoss()

def runEndBoss():
        enemy.health = 90
        fightDone = False
    
        selectedWeapon = ["Crossbow", "Sword", "Axe", "Mace", "Spear", "Chains"];

        giveHeroWeapon = random.choice(selectedWeapon)
        giveEnemyWeapon = random.choice(selectedWeapon)

        printEmptyLine()
        print (hero.name+ " pulled out a " +str(giveHeroWeapon)+ "!")
        print (enemy.name+ " pulled out a " +str(giveEnemyWeapon)+ "!")
        printEmptyLine()
    
        while hero.health <= 100 or enemy.health <= 90:
            randomTurn = random.randint(1,10)
            damageAmount = random.randint(1,25)

            if randomTurn <= 5 and randomTurn > 0 and fightDone == False:
                if damageAmount >= 17:
                    print (hero.name+ " attacked " +enemy.name+ " for " +str(damageAmount)+ " damage! It was a CRITICAL HIT!")
                    enemy.health -= damageAmount
                    time.sleep(1)
                else:
                    print (hero.name+ " attacked " +enemy.name+ " for " +str(damageAmount)+ " damage!")
                    enemy.health -= damageAmount
                    time.sleep(1)
            elif randomTurn <= 10 and randomTurn > 5 and fightDone == False:
                if damageAmount >= 17:
                    print (enemy.name+ " attacked " +hero.name+ " for " +str(damageAmount)+ " damage! It was a CRITICAL HIT!")
                    hero.health -= damageAmount
                    time.sleep(1)
                else:
                    print (enemy.name+ " attacked " +hero.name+ " for " +str(damageAmount)+ " damage!")
                    hero.health -= damageAmount
                    time.sleep(1)
            elif fightDone == False and randomTurn < 0 or randomTurn > 20:
                print ("Both " +hero.name+ " and " +enemy.name+ " missed their attack!")

            if hero.health <= 0 and enemy.health > 0 and fightDone == False:
                fightDone = True
    
                printEmptyLine()
                print (hero.name+ " was masscred by the Mighty " +enemy.name+ ". " +enemy.name+ " had " +str(enemy.health)+ " hitpoints left!")
                endGame()
                break
            
            elif enemy.health <= 0 and  hero.health > 0 and fightDone == False:
                fightDone = True

                printEmptyLine()
                print (hero.name+ " defeated the Mighty " +enemy.name+ " with " +str(hero.health)+ " hitpoints left!")
                printEmptyLine()

                endGame()
            elif hero.health > 0 and enemy.health > 0:
                continue

def checkHeal():
    if hero.meat > 0 and hero.water <= 0:
        choice = input("You have " +str(hero.health)+ " hitpoints. You should eat some meat. (Enter meat, continue, or explore)")
        if choice == "meat":
            consume(choice)
        else:
            doAction(choice)
        
    elif hero.water > 0 and hero.meat <= 0:
        choice = input("You have " +str(hero.health)+ " hitpoints. You should drink some water. (Enter water, continue, or explore)")
        if choice == "water":
            consume(choice)
        else:
            doAction(choice)
        
    elif hero.water > 0 and hero.meat > 0:
        choice = input("You have " +str(hero.health)+ " hitpoints. With " +str(hero.meat)+ " meat and " +str(hero.water)+ " water(s). You should eat some meat or drink some water. (Enter Meat or Water)")
        if choice == "meat" or "water":
            consume(choice)
        else:
            doAction(choice)

    elif hero.water <= 0 and hero.meat <= 0:
        print ("You need healing, but you have no meat or water.")
        printEmptyLine()
        printEmptyLine()
        continuedAction = input("Do you want " +hero.name+ " to explore, continue walking towards your destination, eat meat, drink some water, or open inventory?")
        doAction(continuedAction)
    else:
        pass

def giveItem(item):
    if item == "water":
        hero.water += 1
        print (hero.name+ " found some water. You now have " +str(hero.water)+ " water(s).")
    elif item == "meat":
        hero.meat += 1
        print (hero.name+ " found meat. You now have " +str(hero.meat)+ " meat.")
    else:
        pass

def consume(food):
    if food == "meat":
        if hero.meat <= 0:
            print ("You do not have any meat!")

        else:
            hero.health += 60
            hero.meat -= 1

            if hero.health > 100:
                hero.health = 100
            
            print ("You ate some meat! You now have " +str(hero.health)+ " hitpoints and " +str(hero.meat)+ " meat left.")
        printEmptyLine()
        continuedAction = input("Do you want " +hero.name+ " to explore, continue walking towards your destination, eat meat, drink some water, or open inventory?")
        doAction(continuedAction)

    elif food == "water":
        if hero.water <= 0:
            print ("You do not have any water!")

        else:
            hero.health = 40
            hero.water -= 1
            
            print ("You drank some water! You now have " +str(hero.health)+ " hitpoints and " +str(hero.water)+ " water(s) left.")
        printEmptyLine()
        continuedAction = input("Do you want " +hero.name+ " to explore, continue walking towards , eat meat, drink some water, or open inventory?")
        doAction(continuedAction)
    else:
        pass


