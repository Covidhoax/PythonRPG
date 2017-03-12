import random
import time
import sys

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
    print ("Starting Fight in III...")
    time.sleep(1)
    print ("Starting Fight in II...")
    time.sleep(1)
    print ("Starting Fight in I...")
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

def checkHealth():
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
        choice = input("You have " +str(hero.health)+ " hitpoints. With " +str(hero.meat)+ " meat and " +str(hero.water)+ " flasks of water. You should eat some meat or drink some water. (Enter Meat or Water)")
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

        
def beginFight():
    if hero.enemiesDefeated == randEndCheck:
        runEndBossStory()

    else:
        enemyGoon.health = 40
        fightDone = False

        selectedWeapon = ["Crossbow", "Sword", "Dagger", "Club", "Spear", "Axe"];            

        giveHeroWeapon = random.choice(selectedWeapon)
        giveEnemyWeapon = random.choice(selectedWeapon)

        printEmptyLine()
        print (hero.name+ " pulled out a " +str(giveHeroWeapon)+ "!")
        print (enemyGoon.name+ " pulled out a " +str(giveEnemyWeapon)+ "!")
        printEmptyLine()

        while hero.health <= 100 and enemy.health <= 40:
            randomTurn = random.randint(1,10)
            damageAmount = random.randint(1,20)

            if randomTurn <=5 and randomTurn > 0 and fightDone == False:
                if damageAmount >= 15:
                    print (hero.name+ " attacked " +enemyGoon.name+ " for " +str(damageAmount)+ " damage! It was a CRITICAL HIT!")
                    enemyGoon.health -= damageAmount
                    time.sleep(1)
                else:
                    print (hero.name + " attacked " +enemyGoon.name+ " for " +str(damageAmount)+ " damage!")
                    enemyGoon.health -= damageAmount
                    time.sleep(1)
            elif randomTurn <= 10 and randomTurn > 5 and fightDone == False:
                if damageAmount >= 15:
                    print (enemyGoon.name+ " attacked " +hero.name+ " for " +str(damageAmount)+ " damage! It was a CRITICAL HIT!.Hero is in Danger")
                    hero.health -= damageAmount
                    time.sleep(1)
                else:
                    print (enemyGoon.name+ " attacked " +hero.name+ " for " +str(damageAmount)+ " damage!")
                    hero.health -= damageAmount
                    time.sleep(1)
            elif fightDone == False and randomTurn >= 17:
                print ("Both " +hero.name+ " and " +enemyGoon.name+ " missed their attack!")

            if hero.health <= 0 and enemyGoon.health > 0 and fightDone == False:
                fightDone = True

                printEmptyLine()
                print (hero.name+ " got brutally murdered by " +enemyGoon.name+ ". ")
                endGame()
                break
                        
            elif enemyGoon.health <= 0 and hero.health > 0 and fightDone == False:
                fightDone == True
                
                printEmptyLine()
                print (enemy.name+ " was defeated by our hero, " +hero.name+ "!, and had " +str(hero.health)+ " hitpoints left!")
                hero.enemiesDefeated += 1

                if hero.health <100:
                    printEmptyLine
                    checkHealth()
                    printEmptyLine()

            elif hero.health <= 0 and enemyGoon.health <= 0 and fightDone == False:
                fightDone == True

                printEmptyLine()
                print (enemy.name+ "and " +hero.name+ " both died!!")
                printEmptyLine()
                endGame()
                break

            else:
                printEmptyLine()
                continuedAction = input("Do you want " +hero.name+ " to explore, continue walking, eat ham, drink a potion, or open inventory?")
                doAction(continuedAction)

            if hero.health > 0 and enemyGoon.health > 0:
                continue


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

def doAction(choice):
    if choice == "explore":
        printEmptyLine()
        
        steps = random.randint(1,20)

        print (hero.name+ " explored the area around him.")
        if steps <= 10 and steps > 5:
            giveItem("water")
        elif steps <= 20 and steps > 15:
            giveItem("meat")
            
        else:
            print (hero.name+ " found nothing but shit and dust while exploring")

            printEmptyLine()
            continuedAction = input("Would you like " +hero.name+ " to explore the area, continue heading towards Arzengoth, eat meat, drink some water or open inventory? (Enter explore/continue/meat/water/inventory)")
            doAction(continuedAction)

    elif choice == "continue":
        steps = random.randint(1,20)

        if steps <= 8 and steps > 0:
            printEmptyLine()

            if hero.enemiesDefeated == randEndCheck:
                runEndBossStory()

            else:
                print (hero.name+ " just been spotted by someone. It turned out to be one of the mighty tyrant " +enemyGoon.name+ "!" )
    
                choice = input("Do you want " +hero.name+ " to kill the enemy or flee and cry?(type either flee or attack")

                strength = random.randint(1,20)
                if choice == "attack":
                    beginFight()
            
                elif choice == "flee" and strength >= 5 and strength <= 8 and hero.health <= 50:
                    printEmptyLine()
            
                    print("The cowardly " +hero.name+ " managed to flee successfully!")
                    printEmptyLine()
            
                    printEmptyLine()
    
                    continuedAction = input("Would you like " +hero.name+ " to explore the area, continue heading towards Arzengoth, eat meat, drink some water or open inventory? (Enter explore/continue/meat/water/inventory)")
                    doAction(continuedAction)

                else:
                    print (hero.name+ " was not able to flee.He has no choice but to fight")
                    beginfight()
                
        elif steps <= 10 and steps > 8:
            giveItem("water")

            printEmptyLine()
            continuedAction = input("Would you like " +hero.name+ " to explore the area, continue heading towards Arzengoth, eat meat, drink some water or open inventory? (Enter explore/continue/meat/water/inventory)")
            doAction(continuedAction)

        elif steps <= 15 and steps > 11:
            giveItem("meat")

            printEmptyLine()
            continuedAction = input("Would you like " +hero.name+ " to explore the area, continue heading towards Arzengoth, eat meat, drink some water or open inventory? (Enter explore/continue/meat/water/inventory)")
            doAction(continuedAction)    

        else:
            print (hero.name+ " did not find anything but shit and bones")
            printEmptyLine()
            continuedAction = input("Would you like " +hero.name+ " to explore the area, continue heading towards Arzengoth, eat meat, drink some water or open inventory? (Enter explore/continue/meat/water/inventory)")
            doAction(continuedAction)

    elif choice == "exit":
        exit()
    elif choice == "water":
        consume("water")
    elif choice == "meat":
        consume("meat")
    elif choice == "inventory":
        print (hero.name+ " has " +str(hero.meat) + " chunks of meat and " +str(hero.water)+ " flasks of water")

        printEmptyLine()
        continuedAction = input("Would you like " +hero.name+ " to explore the area, continue heading towards Arzengoth, eat meat, drink some water or open inventory? (Enter explore/continue/meat/water/inventory)")
        doAction(continuedAction)

    else:
        printEmptyLine
        decision = input("Invalid keystroke.Try again from explore/continue/meat/water/inventory:  ")
        doAction(decision)    


class Hero:
    def __init__(hero, name):
        hero.name = name
        hero.health = 100
        hero.water = 0
        hero.meat = 0
        hero.enemiesDefeated = 0
        
class Enemy:
    def __init__(enemy, name):
        enemy.name = name
        enemy.health = 90

class EnemyGoon:
    def __init__(enemyGoon, name):
        enemyGoon.name = name
        enemyGoon.health = 40

hero = Hero(input("Name the wannabe hero, if he gets to win he shall be mighty: "))
enemy = Enemy(input("Name the tyrant and mighty Nemesis:  "))
enemyGoon = EnemyGoon(enemy.name+ "'s warriors")

printEmptyLine()
print ("        T H E  B A T T L E   F O R   A R Z E N G O T H        ")
time.sleep(2)
print (hero.name+ " is a BARBARIAN with a dream, motivated to defeat the feared tyrant named..")
time.sleep(3)
print (enemy.name+ " , The Ruthless Ruler of Arzengoth. The hero must first murder enemy warriors..")
time.sleep(3)
print ("Once the enemies are finished off, the hero shall meet his worst nightmare..")
time.sleep(3)
print ("in the final battle for Arzengoth with the mighty evil Lord. Defeat him and..")
time.sleep(3)
print ("Rule Arzengoth! Be a Good King, and save the people........")
time.sleep(2)
print ("Or be a Tyrant and torture the peasants....Choice is yours")
time.sleep(2)
print (" Thanks for playing. Game created By FARHAN NAYEEM ISLAM")
time.sleep(1)
print ("Enter 'exit' without the quotes to exit game. This works after the intro only.")
time.sleep(1)
printEmptyLine()
time.sleep(2)

randEndCheck = random.randint(3,8)

choice = input("Do you want " +hero.name+ " to explore, continue walking towards Arzengoth, eat meat, drink water, or open inventory?\n(Enter Continue, Explore, Meat, Water, or Inventory)")
doAction(choice)
