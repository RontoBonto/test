# Imports, Globals, and Variables

init python:
    import random
    
    global bandages
    global bullet
    global isPlaying
    global weapontrack
    global armortrack
    global score
    global en1
    global en1atk
    global en1HitRate
    global atk
    global shotsLoaded
    global shotsLeft
    global northEnemy1
    global northEnemy2
    global northEnemy3
    global beast1
    global northenemy1hitrate
    global northenemy1atk
    global northenemy2hitrate
    global northenemy2atk
    global northenemy3hitrate
    global northenemy3atk
    global northEnemyBool
    global northEnemy2Bool
    global northEnemy3Bool
    global enemyOfficer
    global aggTrack
    global calmtrack
    global southtracker2
    global runnersent
    global starving
    global heavyshelling
    global mines
    global team1
    global team2
    global team3
    global interrogated 
    global machineguns
    global austrianCounteroffensive
    global meleehordehitrate
    global meleehorde
    global deepertrenchesDone
    global machinegunsDone
    global digminesDone
    global barbedwireDone
    global bunkersaddedDone
    global revettingAddedDone
    global boobytrapsDone
    global count
    global healupdone
    global requestsuppliesdone
    global repairarmordone
    global upgradeweapondone
    global runnersent
    global prisoner
    global battle3count
    global heavyshelling
    global finalbattlehp
    global finalbattlebandages
    global barrierhp
    global finalbattleatk
    global finalbattleenemyhp
    global finalbattleenemyatk
    global finalbattleenemyhitrate1
    global germanInfantry
    germanInfantry = 75
    finalbattlehp = 100
    finalbattlebandages = 7
    barrierhp = 200
    finalbattleatk = 40
    finalbattleenemyhp = 5*(germanInfantry)
    finalbattleenemyatk = int(0.75*(germanInfantry))
    finalbattleenemyhitrate1 = random.randrange(1,5)
    finalbattleenemyhitrate2 = random.randrange(1,3)
    battle3count = 0
    prisoner = False
    choicetrack = 0
    healupdone = False
    requestsuppliesdone = False
    repairarmordone = False
    upgradeweapondone = False
    runnersent = False
    count = 0
    deepertrenchesDone = False
    machinegunsDone = False
    digminesDone = False
    barbedwireDone = False
    bunkersaddedDone = False
    revettingAddedDone = False
    boobytrapsDone = False
    austrianCounteroffensive = 40
    machineguns = True
    team1 = False
    team2 = False
    team3 = False
    interrogated = True
    runnersent = False
    aggTrack = 0
    calmtrack = 0
    enemyOfficer = 100
    northEnemy3Bool = False
    gowesttrack = 1
    en1atk = 5
    en2atk = 10
    en1HitRate = random.randrange(1,11)
    en2HitRate = random.randrange(1,11)
    shotsLoaded = 6
    shotsLeft = 18
    beastammo = 6
    isPlaying = True
    bullet = random.randrange(1, 6)
    score = 0
    debugMode = False
    location = "Officer's Bunker."
    location2 = "West of the Bunkers."
    southtracker2 = 1
    weapontrack = 1
    armortrack = 1
    medictrack = 1
    bandages = 0
    torf = 0
    bonus = 0
    atk = 25
    hp = 100 # this should be global
    en1 = 50
    en2 = 100
    en3 = 125
    beasthp = 200
    northEnemy1 = 60
    northEnemy2 = 60
    northEnemy3 = 60
    northEnemyBool = True
    northEnemy2Bool = False
    northEnemy3Bool = False
    starving = False
    enemyOfficer =  100
    enemyOfficeratk = 25 
    peopleDead = ("Pavel Andreyevich Korolev - Private","Anton Vladimirovich Dmitriev - Private","Grigory Alekseyevich Popov - Private","Yuri Dmitrievich Kovalchuk - Private","Sergei Andreyevich Romanov - Private","Andrei Petrovich Orlov - Private","and Sgt. Konstantin Dmitrievich Tarasov")
    stringpeopleDead = ", ".join(peopleDead)
    heavyshelling = False
    global swordFightingBattle
    swordFightingBattle = False
    def label_callback(name, abnormal):
        if name.startswith("_"): return
        devlog.info(name)
        store.current_label = name
        stuff = store.current_label
        return stuff

    config.label_callback = label_callback

    class battleScenes: 
        """
        This function is meant to describe battle scenes in the game. The other stuff here is terrible and others have already made their own function and stuff so yeah
        Anyways, hitRate is out of 20. If the random number is bellow the number chosen, then that is when the enemy should attack. 
        This is meant to 
        """
        def __init__(self, enemyNumbers, enemyHp, enemyatk, hitRate):
            self.enemyNumbers = int(enemyNumbers)
            self.enemyHp = int(enemyHp)
            self.originalEnemyHp = int(enemyHp)
            self.hitRate = int(hitRate)
            self.enemyatk = int(enemyatk)
        def choice(self):
            renpy.say(n,"Will you attack or heal?")
            renpy.display_menu([("Attack", battleScenes.attack()),("Heal", battleScenes.heal())])
        def attack(self):
            """ Attacks the enemy. """
            renpy.say(n, "You attack!")
            renpy.say(n, "You deal [atk] damage" )
            renpy.sound.play("Revolver Sound Effect.mp3")
            self.enemyHp -= atk
            renpy.say(n, "The enemy has [self.enemyHp] hp left")
            if self.enemyHp <= 0 and self.:
                renpy.say(n, "This enemy has fallen, another takes his place.")
                self.enemy
            chaos = random.randrange(1, 21)
            if chaos <= self.hitRate:
                renpy.say(n, "The enemy hits you and deals [self.enemyatk] damage to you.")
                hp -= self.enemyatk
                if hp <= 0:
                    renpy.call_in_new_context("badEnding")
                renpy.say(n, "You have [hp] remaining")
                
            else: 
                renpy.say(n, "")
            battleScenes.choice()
        def heal(self):
            print("lol")
    class swordBattle(battleScenes):
        def __init__(self):
            swordFightingBattle = True










# Declaration of Characters

define n = Character("Narrator")
define y = Character("You")
define k = Character("Sgt. Konstantin")
define i = Character("Ivan")
define w = Character("Weaponsmith")
define a = Character("Armorer")
define m = Character("Medic")
define e1 = Character("Enemy 1")
define e2 = Character("Enemy 2")
define j = Character("Jakab")
define u = Character("???")
define s0 = Character("Soldier")
define s1 = Character("Soldier1")
define s2 = Character("Soldier2")

# Images used for Scenes

image trenchHall = "images/trench hallways.png"
image officer_bunker = "images/officers_bunker.png"
image mainTrench = "mainTrenches.jpg"
# image konstantin_office = ""
# image west_trenches_1 = ""
# image west_trenches_2 = ""
image camp = "images/camp.jpg"
# image armorer = ""
image weaponsmithworkarea = "images/weaponsmith_station.png"
image armorerworkarea = "images/armorer station.png"
# image medicworkarea = "images/medic_station"
image reverse trench hall = "images/trench hallways reversed.png"
# image west_of_bunkers = ""
image trenches = "images/trenches.png"
image battle_1 = "images/battle_1.png"
# image battle1_ends = ""
# image battle_2 = ""
# image battle2_ends = ""
# image final_battle = ""
# image fnalbattle_ends = ""
image blurry_trenches = "images/blurry_trenches.png"
image enemy_officer_bunker = "images/officers_bunker_reversed.png"
image no mans land = "images/no-mans-land.jpg"
image surrender = "prisoner.jpg"
image GoodEnding = "1900s Russian village.jpg"

# Images used for Characters

image Konstantin = "images/sgt konstantin.png"
# image Ivan = "images/ivan"
image weaponsmith = "images/weaponsmith.png"
image armorer = "images/armorer.png"
image medic = "images/medic.png"
# image enemy1 = "images/enemy1"
# image enemy2 = "images/enemy2"
# image Jakab = "images/Jakab"
# image Unknown = "images/Unknown"
# image Soldier = "images/Soldier"
# image Soldier1 = "images/Soldier1"
# image Soldier2 = "images/Soldier2"

# Images used for warning and end

image warning_screen = "images/warning_screen.jpg"
image black_screen = "images/black screen.png"
image the_end = "images/the_end.jpg"

# Defines for Fades

define gunshotFade = Fade(0.1,2,1,color="#FFF")
define warningFade = Fade(0.1,1,1,color="#000")
define bunkerFade = Fade(0.5,1,1,color="#000")
define blackscreenFade = Fade(1,1,1,color="#000")

# Warning screen thing

label splashscreen:
    
    show image "warning_screen.jpg" with warningFade
    pause 4
    
    show black_screen with blackscreenFade
    
    $ renpy.music.set_volume(7)

return

# Start of Russian Roulette Game

label start:

    stop music

    play music "ArtilleryRecovery.mp3" loop

    show officer_bunker with bunkerFade

    n "You have 1 bullet loaded in the chamber."

    n "It has already been spun into place."

label extraBulletChoosing:
    python:
        try:
            extraBullet = int(renpy.input("How many bullets will you add in the chamber?"))

        except:
            renpy.say(n, "Please input an integer")
            renpy.call_in_new_context("extraBulletChoosing")
                    
                
            if extraBullet < 0:
                "That's too low, that's a negative number, that's impossible. "
                renpy.call_in_new_context("extraBulletChoosing")
            
    # Rest of your code here after getting a valid input

# Shoot or Spin decision

label initialChoosing:
    python:
        try:
            function = renpy.input("Will you shoot or spin? ").lower()
        except:
            renpy.say("Shoot or Spin")
            renpy.jump(initialChoosing)
    if function == "shoot":
        jump shoot

    elif function == "spin":
        jump spin
    else:
        n "SHOOT OR SPIN"
        jump initialChoosing

# Shoot decision

label shoot:

    $ global isPlaying
    
    python:
        
        if bullet >= (5 - float(extraBullet)):
            shot = True
        
        elif 1 <= bullet <= (4 - float(extraBullet)):
            shot = False
    
    if shot == True:
        call fired1 from _call_fired1
    
    elif shot == False:
        call didnotFire1 from _call_didnotFire1

label fired1:

    $ global isPlaying
    
    n "You decide to pull the trigger of the gun..."

    n "You fire your gun..."

    play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop
    
    with gunshotFade
    
    scene black_screen

    n "Game over, you died..."
    
    n "Your final score is: [score]"
    
    stop music 

    $ isPlaying = False
    
    call youDied from _call_youDied
    
    if debugMode == True:
        n "[bullet]"

label didnotFire1:

    $ global isPlaying
    
    n "You decide to pull the trigger of the gun..."

    n "You fire your gun..."
    
    play audio "audio/misclick.mp3"
    
    n "You lived!"
    
    python:
        score += 2 * (int(extraBullet) + 1)
        bullet += 1
    
    n "Your score is: [score]" 
    jump initialChoosing

# Spin decision

label spin:

    $ global isPlaying
    
    $ bullet = random.randrange(1,6)

    python:
        
        if bullet >= (5 - float(extraBullet)):
            shot = True
        
        elif 1 <= bullet <= (4 - float(extraBullet)):
            shot = False

    if shot == True:
        jump fired2

    elif shot == False:
        jump didnotFire2

label fired2:

    $ global isPlaying
    
    n "You decide to spin the chamber of the gun..."

    n "You fire your gun..."
    
    play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop
    
    with gunshotFade
    
    scene black_screen

    n "Game over, you died..."
    
    n "Your final score is: [score]"
    
    stop music

    $ isPlaying = False
    
    call youDied from _call_youDied2
    
    if debugMode == True:
        n "[bullet]"

label didnotFire2:

    $ global isPlaying
    
    n "You decide to spin the chamber of the gun..."

    n "You fire your gun..."
    
    play audio "audio/misclick.mp3"
    
    n "You lived!"
    
    python:
        score += 1 * (int(extraBullet) + 1)
        bullet += 1
    
    n "Your score is: [score]" 
    jump initialChoosing

# Label when you die playing Russian Roulette

label youDied:
    jump wakeUp

# Start of decision-based game when you die

label wakeUp:
    
    stop music

    play music "HillsofManchuria.mp3" loop volume 7
    
    scene officer_bunker with bunkerFade
    
    n "You wake up from a dream as the bullet inched closer to the fragile temple."

    n "For some background, you are a Lieutenant of the Tsarist Russian forces." 

    n "You have received your orders for a new offensive, the Brusilov offensive.{w} After playing that deadly game, you are satisfied with your luck." 

    n "You are inside the officer’s bunker within your trenches.{w} There is a map here but the room is dimly lit."

    n "You can check your location, talk to Sgt. Konstantin, go west to leave and see the condition of the trenches outside, or blow the whistle to signal battle."

    n "What will you do?"

    jump menu1

# Decisions after the start of the decision-based game

label menu1:
    
    scene officer_bunker
    
    menu:
        "CHECK LOCATION":
            jump checkLocation1

        "TALK TO SEARGENT KONSTANTIN":
            jump talkToKonstantin

        "GO WEST":
            jump goWest1

        "BLOW WHISTLE":
            jump blowWhistle

# Allows user to check loaction (Officer's Bunker)

label checkLocation1:

    scene officer_bunker

    n "Your are at the [location]"

    n "What will you do now?"

    jump menu1

# Makes user talk to Konstantin

label talkToKonstantin:

    scene officer_bunker

    show Konstantin

    y "So, how's it going?"

    k "Well sir, frankly, we’re all nervous for this new offensive."

    k "The Austrians have been under heavy shelling for a while now, but we’re not sure if it’s effective."

    y "Don’t worry too much, we went over this already."

    y "The men  we have are trained and the artillery has been fire spotted to give it the most effectivity."

    y "Also, there are tunnels that allow the men to instantly appear in front of the enemy trenches without them getting spotted."
    
    k "Well, another problem is that we’re starving!"

    k "Our logistics is terrible, so the men haven’t had much food to eat."

    k "Also, I must say that I feel as though the supply won’t be running with us if we break through the enemy lines."

    menu:
        "Reassure Konstantin":
            y "Don’t worry about it too much!" 
            
            y "The food will be sure to follow us as long as we break through."

            k "Sir, yes sir!"

            jump menu1

        "Agree with Konstantin":
            y "I agree, however we need to keep pushing forward."

            k "Alright, I guess."

            jump menu1

# This is for the first "go west" action of the user

label goWest1:
    
    scene mainTrench

    n "You go outside to see the condition of the trenches, they are average for the time." 

    n "There are rats running about and the ground is muddy, but there are wood planks placed to support you from sinking into it."

    n "There is a periscope that you can check, and you can either go north or south to check on your right and left flanks."

    n "Otherwise, if you’re ready, you can blow the whistle to signal the men to attack."

    jump menu2

# Choices for when the user goes west once (no Ivan Encounter)

label menu2:

    scene mainTrench
    
    menu:

        "GO SOUTH":
            jump goSouth
        
        "GO NORTH":
            jump goNorth

        "GO WEST AGAIN":
            jump goWest2

        "CHECK LOCATION":
            jump checkLocation2

        "GO BACK":
            jump menu1

        "BLOW WHISTLE":
            jump blowWhistle

# Scene when user chooses to go South

label goSouth:
    scene reverse trench hall
    
    $ global southtracker2

    if southtracker2 == 1:

        $ survivalRate = random.randrange(1,21)

        scene reverse trench hall

        n "Suddenly, you hear a large crack, and the man manning the maxim gun had just been shot." 
    
        n "You order your men to return fire.{w} Do you man the maxim gun?"

        menu:
            "YES":
                n "You man the maxin gun."
                play audio "Maxim Gun.opus" noloop
                n "The enemy sniper has been suppressed, but he is still able to fire one last shot."

                if survivalRate == 1:

                    play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop

                    scene black_screen

                    with gunshotFade

                    n "Game over, you died..."

                    jump badEnding

                elif 5 > survivalRate > 1:
                    n "The shot hits your shoulder." 
                
                    n "Despite that, you keep on firing and eventually, you hear no more shots coming from the Austrian sniper." 
                
                    n "He is likely dead by now.{w} The men are inspired by your sacrifice."

                    $ southtracker2 -= 1

                    n "You retreat and go back north."

                    n "What will you do now?"

                    jump menu2

                else:
                    n "The shot misses though and because the enemy sniper shoots, you see the muzzle flash and aim the machine gun in that direction."
                    
                    n "The enemy sniper is likely dead at this point.{w} The men are inspired by your sacrifice."

                    $ southtracker2 -= 1

                    n "You retreat and go back north."
                    stop audio
                    n "What will you do now?"
                    
                    jump menu2
                

            "NO":
                n "You quickly retreat out of there.{w} You do not want to deal with that enemy sniper and the men understand."

                $ southtracker2 -= 1

                n "You retreat and go back north."

                n "What will you do now?"
                    
                jump menu2    

    else:
        n "You've been here before and it's too dangerous.{w} Go back north and choose a different decision."

        jump menu2

# Scene when user chooses to go north (Armorer, Weaponsmith, and Medic)

label goNorth:

    scene camp
    
    n "After heading North, you notice a small camp with some supplies."

    n "You search the area and notice three people of different specialities."

    n "You see an armorer, a weaponsmith, and a medic."

    n "What will you do now?"

    jump awm_menu

# Chices after user encounters the Armorer, Weaponsmith, and Medic

label awm_menu:
    
    play music "HillsofManchuria.mp3" loop volume 7

    scene camp

    menu:
        "GO TO THE ARMORER":
            jump armorer

        "GO TO THE WEAPONSMITH":
            jump weaponsmith

        "GO TO THE MEDIC":
            jump medic

        "GO BACK SOUTH":
            scene mainTrench
            
            n "You head back south after checking out the area."

            n "What will you do now?"

            jump menu2

        "BLOW WHISTLE":
            jump blowWhistle

# Scene when Armorer is chosen

label armorer:
    stop music
    scene armorerworkarea

    show armorer

    $ global armortrack
    $ global hp
    
    if armortrack == 1:

        stop music fadeout 2
        play music "audio/Armorer OST.mp3" loop 
        
        a "Hello, im the armorer!{w} You are in luck today because I have just created the best chestplate suited for battle!"

        a "Since you have helped us in so many aspects, Lieutenant, this piece is free of charge!"

        a "Would you want to use this piece, sir?"

        menu:

            "YES, I WOULD LOVE TO WEAR IT!":

                a "Nice choice, sir! You look stronger and readier for combat!"

                n "100 HP has been added to your character"

                $ hp += 100

                a "I hope to see you again next time, soldier."

                n "You are now ready for combat with your new armor!"

                n "What will you do now?"

                $ armortrack -= 1
                stop music fadeout 2
                jump awm_menu

            "NO, I'M GOOD.":

                a "Huh? Are you sure about that? This is the finest piece you'll find in all the world!"

                menu: 

                    "YES, I WOULD LOVE TO WEAR IT!":

                        a "Nice choice, sir! You look stronger and readier for combat!"

                        n "100 HP has been added to your character"

                        $ hp += 100

                        a "I hope to see you again next time, soldier."

                        n "You are now ready for combat with your new armor!"

                        n "What will you do now?"

                        $ armortrack -= 1
                        stop music fadeout 2
                        jump awm_menu

                    "NO, I SAID I'M GOOD.":

                        a "Last chance, sir! It's my proudest work of all time!"

                        menu:

                            "FINE, I GUESS SOME PROTECTION WOULDN'T HURT.":

                                a "Nice choice, sir! You look stronger and readier for combat!"

                                n "100 HP has been added to your character."

                                $ hp += 100

                                a "I hope to see you again next time, soldier."

                                n "You are now ready for combat with your new armor!"

                                n "What will you do now?"

                                $ armortrack -= 1
                                stop music fadeout 2

                                jump awm_menu

                            "HOW MANY TIMES DO I HAVE TO SAY NO!?":

                                a "If you insist, sir.{w} However, please take this lucky pendant."

                                a "It has protected my family my whole life, and I know it will protect you too."

                                y "Fine, atleast its light enough to not bother me in combat."

                                a "Thank you, soldier.{w} I wish you luck and I hope to see you again next time."

                                n "OBTAINED LUCKY PENDANT"

                                n "With your newly obtained lucky pendant from the armorer, you feel as if you are now ready for combat!"

                                n "What will you do now?"

                                $ armortrack -= 1
                                stop music fadeout 2

                                jump awm_menu

    else:
        hide armorer
        n "Nothing here..."
    jump awm_menu

# Scene when Weaponsmith is chosen

label weaponsmith:
    stop music
    scene weaponsmithworkarea

    show weaponsmith

    $ global weapontrack
    $ global torf
    $ global atk
    $ global bonus

    if weapontrack == 1:

        stop music fadeout 2
        play music "audio/weaponsmith OST.mp3" loop

        w "Hello fine sir! I am the prestigious weaponsmith of the camp! Do you want an upgrade to your arsenal?"

        w "Of course you do!"

        w "All you have to do is answer three Math questions! Each correct answer will give you 5 ATK points!"

        w "Make sure to scream TRUE or FALSE for each answer! Goodluck!"

        w "First, it is possible to have one value for x and have two values for y in a linear equation?"

        $ weaponanswer1 = renpy.input("TRUE or FALSE?")

        if weaponanswer1 == "FALSE":
            $ torf += 1

        w "Interesting answer..."

        w "Next, if your gold is compounded monthly for seven years, is the total number of periods 84?"

        $ weaponanswer2 = renpy.input("TRUE or FALSE?")

        if weaponanswer2 == "TRUE":

            $ torf += 1

        w "Intriguing answer..."

        w "Last, if a row in a matrix is a multiple of another wrong, can this said row be reduced to all 1's?"

        $ weaponanswer3 = renpy.input("TRUE or FALSE?")

        if weaponanswer3 == "FALSE":

            $ torf += 1
        
        w "Thats all the questions, sir!"

        w "Thank you for playing! Your score is [torf]."

        $ atk += torf*5
        $ bonus = torf*5

        w "Your weapon's damage has been increased by [bonus]."
    
        stop music fadeout 2
        $ weapontrack -= 1

    else: 
        hide weaponsmith
        n "Nothing here..."
    jump awm_menu

# Scene when Medic is chosen

label medic:
    stop music 
    scene armorerworkarea

    $ global medictrack
    $ global bandages

    if medictrack == 1:

        stop music fadeout 2
        play music "audio/medic OST.mp3" loop

        show medic

        m "Hello, im the reliable medic!{w} Before you embark on the battle, here are some bandages that heal 20 HP at any time!"

        m "These items are so powerful that it can make you have more than your max HP!"

        m "how many do you want?"
        $ bandcount = None
        python:
            
            while bandcount is None:
                try:
                    bandcount = int(renpy.input("Choose a number from 0 to 5."))
                except:
                    renpy.say(n, "Error, please input a rational integer from 0 to 5.")
                    pass
        $ bandages = bandcount
        if bandcount < -1 or bandcount > 5:
            m "You're too greedy"
            $ bandages = 0
            m "I will give you [bandages] bandages because of that."
        if 0 < bandcount < 6:
            m "I will give you [bandcount] bandages. Use them wisely."
            stop music fadeout 2

        else: 
            m "None? Okay then. Goodluck on your battle, sir!"
        stop music fadeout 2
        $ medictrack -= 1
    
    else:
        hide medic
        n "Nothing here..."
    jump awm_menu

# Scene when user chooses to go west twice (Ivan Encounter)

label goWest2:
    stop music
    $ global gowesttrack
    $ randnum = random.randrange(1,21)

    if gowesttrack == 1:
        play music "Dreamy fish from Subahibi.flac" fadeout 5
        scene trenchHall

        y "Something feels off about this place..."

        

        u "Well, well, well....look who we have here?"

        

        i "Who is this lowly soldier at the behest of the one and only, Ivan! "
    
        i "Anyways, I have a challenge for you and a reward if you are able to beat my challenge!"

        i "The game is very simple!{w} All you have to do is guess the number im thinking of from 1 to 20!"
        stop music fadeout 7
        i "I'll even give you three tries!{w} Let the games begin!"

        play music "audio/guessing OST.mp3" loop
        
        
        python: 
            guess1 = None
            while guess1 is None:
                try:
                    guess1 = int(renpy.input("What's your first guess?"))
                except:
                    renpy.say(i, "Give an integer.")
                    pass

        
        if guess1 != randnum:
            i "HAHAHAHA! Wrong!"
      
            if randnum % 2 == 0:
                i "Clue! The number is an even number!"
      
            else:
                i "Clue! The number is an odd number!"
                
            python: 
                guess2 = None
                while guess2 is None:
                    try:
                        guess2 = int(renpy.input("What's your second guess?"))
                    except:
                        renpy.say(i, "GIVE AN INTEGER!")
                        pass
      
            if guess2 != randnum:
                i "HAHAHAHAHAHAHAHA! Wrong again!"
        
                if randnum % 3 == 0:
                    i "Clue! The number is divisible by 3!"
        
                else:
                    i "Clue! The number is not divisible by 3!"
                
                python: 
                    guess3 = None
                    while guess3 is None:
                        try:
                            guess3 = int(renpy.input("What's your THIRD AND LAST guess?"))
                        except:
                            renpy.say(i, "GIVE AN INTEGER!")
                            pass
        
                if guess3 != randnum:
                    i "Wrong once AGAIN HAHAHAHAAHAHAHAHA! You LOSE!"
          
                    if randnum > 10:
                        i "I'm kidding! I'll give you one last chance! The number is greater than 10"
          
                    else:
                        i "I'm kidding! I'll give you one last chance! The number is less than 10"
                    
                    python: 
                        guess4 = None
                        while guess4 is None:
                            try:
                                guess4 = int(renpy.input("What's your fourth and FINAL guess?"))
                            except:
                                renpy.say(i, "GIVE AN INTEGER!")
                                pass

                    if guess4 == randnum:
                        i "Finally! That is correct!"
                        
                        i "As a reward, here is a legendary badge that I got long ago!{w} It's worth more than a penny!"
                        
                        n "OBTAINED LEGENDARY BADGE"
                        
                        $ gowesttrack -= 1

                        n "You leave the mysterious place and head back East." 
                        
                        n "What will you do now?"               

                    else:
                        i "How could you have not gotten it... Well then, leave this place! You have wasted my time!"

                        $ gowesttrack -= 1

                        scene west trenches 2

                        n "You were banished all the way back East."
    
                        n "What will you do now?"
                
                else: 
                    i "HOW?!? That is correct! As a reward, here is a legendary badge that I got long ago! It's worth more than a penny!"
            
            else: 
                i "HOW?!? That is correct! As a reward, here is a legendary badge that I got long ago! It's worth more than a penny!"

        else: 
            i "HOW?!? That is correct! As a reward, here is a legendary badge that I got long ago! It's worth more than a penny!"

        $ gowesttrack -= 1
        stop music fadeout 2
    
    else:
        
        scene west_trenches_2

       
        
        i "I said LEAVE!!!"
        
    jump menu2

# Allows user to check location before Ivan Encounter (West of the Bunkers)

label checkLocation2:

    scene mainTrench

    n "Your are at the [location2]"

    n "What will you do now?"

    jump menu2

# Allows user to check location after Ivan Encounter (West of the Bunkers)

label checkLocation3:
    play music "audio/HillsofManchuria.mp3" loop
    scene mainTrench

    n "Your are at the [location2]"

    n "What will you do now?"

    jump menu2

# Scene if user chooses to blow whistle / start battle

label blowWhistle:
    play audio "Whislte.mp3"
    scene no mans land

    stop music

    play music "audio/battle ost.mp3" fadein 5.0 loop

    n "You blow the whistle, and give the order to attack!{w} Your men go into the tunnels and out into the Austrian lines."

    n "Your men are prepared for this, but despite that, there’s nothing that can beat the chaos of trench warfare."

    n "The men throw themselves against the Austrian trenches and the Austrians light up with machine gun fire."

    n "Due to the extensive preparations undertaken for this offensive, many men get through this hailstorm and jump into the Austrian trenches."

    n "While following your men into the chaos of the enemy trenches, you encounter an enemy soldier."

    

    n "He is pointing his rifle at you."

    e1 "You coward!"

    e1 "Fight me!"

    n "Even at the face of death, your pride won't let you run away from this threat!"

    n "You decide to confront him!"
    
    jump battle1

# Scene for when the first battle starts

label battle1:
    
    $ global en1
    $ global hp
    $ global atk
    $ global bandages

    scene no mans land
    

    n "Will you attack, heal, or reload your weapon?"
    $ en1HitRate = random.randrange(1,11)
    menu: 
        "ATTACK":
            jump attackEn1 
            
        "HEAL":
            jump healEn1

        "RELOAD":
            jump reloadEn1

# All the codes for attack, heal, and reload for battle 1

    while en1 > 0 and hp > 0:

        label attackEn1: 

           

            n "You shoot."
            play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop
            n "You do [atk] damage."
    
            $ en1 -= atk

            if en1 < 1:
                jump enemy1Defeated

            n "The enemy has [en1] health remaining."

            if en1HitRate <= 5:
                play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop
                n "The enemy does 5 damage to you."
                
                $ hp -= en1atk
        
                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding

            else: 
                n "The enemy misses."

                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding

            jump battle1

        label healEn1:

            
            
            n "You decide to try and heal!"
            
            if bandages > 0:
        
                $ hp += 20
                $ bandages -= 1

                n "HP increased by 20!"

                n "You now have [hp] health."
    
            else:
                n "Unfortunately, you have no bandages left..."

            if en1HitRate <= 5:
                
                
                play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop
                n "The enemy does 5 damage to you."

        
                $ hp -= en1atk

                if hp < 1:
                    jump badEnding

                n "You have [hp] health remaining."
            
            else: 
                
               
                
                n "The enemy misses."

                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding

            jump battle1

        label reloadEn1:

            scene battle_1

            
            
            n "You decide to try and reload!"
            
            jump battle1

# Scene if you die during a battle

label badEnding:

    scene blurry_trenches

    n "You Died..."

    y "Amidst the relentless chaos of the battlefield, as the deafening roar of artillery and the relentless barrage of bullets filled the air, I, a Tsarist Russian soldier, knew that my time was drawing to a close."
    
    y "The war had been brutal, and it had taken its toll on both my body and spirit.{w} I lay on the cold, unforgiving ground, my strength waning with each passing moment." 
    
    y "Thoughts of my family, of my beloved parents, and of my two siblings consumed my mind.{w} How I longed to hold them once more, to see their smiles, to hear their laughter."
    
    y "But the cruel hand of fate had other plans for me.{w} With the faces of my family in my mind and their names on my lips, I closed my eyes for the last time."

    scene black_screen

    y "A profound sense of peace replaced the sounds of battle as they faded into the distance." 
    
    y "In death, I may not have been able to see my family one last time, but I knew that they would carry my memory in their hearts, and I took comfort in the hope that they would find happiness and a future free from the scars of war."

    y "As the world moved on, the memory of the Tsarist Russian soldier who fought hard would remain in the hearts of those who knew him, a testament to the sacrifices made by so many during those tumultuous times."

    scene the_end

    jump end_screen

# Scene if you defeat Enemy 1

label enemy1Defeated:

    scene battle_1

    

    n "After defeating your first enemy, you search his body for any ammunition." 
    
    n "You noticed that the person is barely breathing and is reaching out for something in his pockets.{w} You are weary that it might be his sidearm."

    n "What will you do now?"

    menu:
        "FINISH HIM":
            jump finishHim

        "SPARE HIM":
            jump spareHim

# Scene if you finish the enemy

label finishHim:
    
   

    n "You point your rifle straight to his head!"

    play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop

    hide en1

    n "With a press of your rifle, you finished the wounded enemy."

    y "So it goes, warfare takes its toll."

    jump inTrenches

# Scene if you spare the enemy

label spareHim:

    

    n "You spared the wounded enemy." 

    n "He reveals in his clutches a crumpled photo of him and another figure."

    n "With his last breaths, he asks you to find this person in the image and deliver it to him."

    jump inTrenches

# Scene for when the second battle starts

label inTrenches:
    
    scene trenches

    n "After having finished that initial confrontation, you find yourself within the enemy trenches."

    n "To the north, you hear your men fighting the enemy in brutal hand to hand combat.{w} To the south, surprisingly, you hear nothing.{w} Further west is the enemy officer’s bunkers."
    
    menu:
        "GO NORTH":

            n "You encounter more enemies here.{w} Fearing the risk of friendly fire, you engage in brutal hand to hand combat with them."
            
            n "You draw your sword and fight the enemies in front of you."
            
            jump northEnemyTrenches
        
        "GO WEST":
            
            scene enemy_officer_bunker

            n "You go inside the enemy officer’s bunkers and you find an enemy officer here."
    
            

            n "You both duel to the death."

            jump westEnemyTrenches
        
        "GO SOUTH":

            scene reverse trench hall
           
            n "You decide to go south.{w} You encounter a fearsome monster of hell. It is feasting on the corpses of both your own men and the enemies’."
            
            jump southEnemyTrenches

# Scene for when you go south and encounter the beast

label southEnemyTrenches:

    $ global beasthp
    $ global hp
    $ global atk
    $ global bandages
    $ global beastammo

    scene reverse trench hall
    

    $ beastHitRate = random.randrange(1,6)
    n "Will you pray, attack, heal or reload?"

    menu:
        "PRAY":
            jump southPray

        "ATTACK":

            jump southAttack

        "HEAL":

            jump southHeal

        "RELOAD":

            jump southReload

    while beasthp > 0 and hp > 0:

        label southPray:

            n "You decide to pray."

            n "Your ATK is increased by 20 points."

            $ atk += 20

            if beastHitRate == 1:

                n "The beast does 35 damage to you."

                $ hp -= 35
        
                n "You have [hp] health remaining."

                if hp < 1:

                    jump badEnding
            
            else: 
                n "The enemy misses."

                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding

            jump southEnemyTrenches

        label southAttack: 

          

            if beastammo == 0:

                y "I NEED MORE BOULLETS!"
                jump southEnemyTrenches

            n "You shoot."
    
            n "You do [atk] damage."
    
            $ beasthp -= atk
            $ beastammo -= 1

            if beasthp < 1:
                jump normalRoute

            n "The beast has [beasthp] health remaining."

            if beastHitRate == 1:

                n "The beast does 35 damage to you."

                $ hp -= 35
        
                n "You have [hp] health remaining."

                if hp < 1:

                    jump badEnding
            
            else: 
                n "The enemy misses."

                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding

            jump southEnemyTrenches

        label southHeal:
        
            
            
            n "You decide to try and heal!"
        
            $ beastHitRate = random.randrange(1, 6)
            if bandages > 0:
        
                $ hp += 20
                $ bandages -= 1

                n "HP increased by 20!"

                n "You now have [hp] health."
    
            else:
                
                n "Unfortunately, you have no bandages left..."

            if beastHitRate == 1:
                
                
                
                n "The beast does 5 damage to you."
        
                $ hp -= 35

                if hp < 1:
                    
                    jump badEnding

                n "You have [hp] health remaining."
            
            else: 
                
                
                
                n "The beast misses."

                n "You have [hp] health remaining."

                if hp < 1:
                    
                    jump badEnding

            jump southEnemyTrenches

        label southReload:

            n "You reload your weapon."

            $ beastammo == 6
            jump southEnemyTrenches

#Western Section of the game

label westEnemyTrenches:

    $ global enemyOfficer
    $ global enemyOfficeratk
    
    n "Will you shoot or heal?"
    
    menu:
        "SHOOT":
            jump shootenemyOfficer
        
        "HEAL":
            jump healenofficer
    
    while hp >0 and enemyOfficer > 0:
        
        label shootenemyOfficer:
            $ atk = 25
            
            n "You shoot the enemy officer!"
            play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop
            $ enemyOfficer -=25
            
            n "He has [enemyOfficer] health remaining."
            
            if enemyOfficer <1:
                n "He is defeated now."
                
                n "You may take him prisoner."
                
                menu:
                    "TAKE ENEMY OFFICER AS PRISONER":
                        $ prisoner = True
                        jump normalRoute
                    
                    "KILL HIM":
                        jump normalRoute
           
            $ hp -= 25
            play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop
            n "The enemy officer also shoots back."
            
            if hp < 1:
                    jump badEnding
            
            n "You have [hp] remaining."
            
            jump westEnemyTrenches
        
        label healenofficer:
            
            if bandages >0:
                $ hp += 20
                
                n "You heal to [hp] health."
            
            else:
                n "You have no bandages remaining."
            
            $ hp -= 25
            
            n "The enemy officer attacks."

            play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3"
            
            if hp < 1:
                jump badEnding
            
            n "You have [hp] remaining."
            
            jump westEnemyTrenches

# Scene for when you go north and encounter more enemies

label northEnemyTrenches:
        
    scene reverse trench hall
    
    $ global en2
    $ global hp
    $ global atk
    $ global bandages
        
    $ northenemy1hitrate = random.randrange(1,11)
    $ northenemy2hitrate = random.randrange(1,11)
    $ northenemy3hitrate = random.randrange(1,11)

    n "Will you attack or defend yourself?"

    menu: 
        "ATTACK":
            if northEnemyBool == True: 
                jump attackNorthEnemies 
                
            elif northEnemy2Bool == True:
                jump attackNorthEnemies2
            elif northEnemy3Bool == True:
                jump attackNorthEnemies3
                
        "DEFEND":
            if northEnemyBool == True: 
                jump dfndNorthEnemies 
                
            elif northEnemy2Bool == True:
                jump dfndNorthEnemies2
            elif northEnemy3Bool == True:
                jump dfndNorthEnemies3

# All the codes for attack, heal, and reload for battle 2

    while northEnemy3 > 0 and hp > 0:
        
        label attackNorthEnemies: 
            
            scene reverse trench hall
            

            $ atk = 30
            play audio "audio/Sword SFX 4.opus" noloop
            n "You were able to deal damage!"
    
            n "You do [atk] damage."
            
            $ northEnemy1 -= atk

            

            if northEnemy1 < 1:
                n "Another enemy jumps into the fray!"
                $ northEnemyBool = False
                $ northEnemy2Bool = True
                jump northEnemyTrenches
        
            n "The enemy has [northEnemy1] health remaining."
            

            if northenemy1hitrate <= 7:
                n "The enemy does 20 damage to you."
                play audio "audio/Something being hit - Sound Effect.opus" noloop
                $ hp -= 20
        
                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding
                jump northEnemyTrenches 

            else: 
                n "The enemy misses."

                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding
                jump northEnemyTrenches
            jump northEnemyTrenches
        
        label dfndNorthEnemies:
            
            scene reverse trench hall
           
            
            if northenemy1hitrate <= 7:
                play audio "audio/Something being hit - Sound Effect.opus" noloop
                n "The enemy does 20 damage to you."

                n "You defend and take only 14 damage."
        
                $ hp -= 14
        
                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding
                jump northEnemyTrenches
            else:
                n "The enemy misses."

                n "You have [hp] health remaining."
                jump northEnemyTrenches
            jump northEnemyTrenches

        label attackNorthEnemies2: 
            
            scene reverse trench hall
            

            play audio "audio/Sword SFX 4.opus" noloop
            $ atk = 30
            
            n "You were able to deal damage!"
    
            n "You do [atk] damage."

            $ northEnemy2 -= atk

            if northEnemy2 < 1:
                n "Another enemy jumps into the fray!"
                $ northEnemyBool = False
                $ northEnemy2Bool = False
                $ northEnemy3Bool = True
                jump northEnemyTrenches

            n "The enemy has [northEnemy2] health remaining."
                
            
            if northenemy2hitrate <= 7:
                play audio "audio/Something being hit - Sound Effect.opus" noloop
                
                n "The enemy does 20 damage to you."
        
                $ hp -= 20
        
                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding
                

            else: 
                n "The enemy misses."

                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding
            jump northEnemyTrenches
        
        label dfndNorthEnemies2:
            
            scene reverse trench hall
            

            if northenemy1hitrate <= 7:
                play audio "audio/Something being hit - Sound Effect.opus" noloop
                n "The enemy does 20 damage to you."

                n "You defend and take only 14 damage."
        
                $ hp -= 14
        
                n "You have [hp] health remaining."
                
                jump northEnemyTrenches 
                
                if hp < 1:
                    jump badEnding
                jump northEnemyTrenches
            else:
                n "The enemy misses."

                n "You have [hp] health remaining."
            jump northEnemyTrenches

        label attackNorthEnemies3: 
           
            scene reverse trench hall
           
           

            play audio "audio/Sword SFX 4.opus" noloop
            
            $ atk = 30
            
            n "You were able to deal damage!"
    
            n "You do [atk] damage."

            $ northEnemy3 -= atk

            if northEnemy3 < 1:
                $ northEnemy2Bool = False
                $ northEnemy3Bool = False
                jump normalRoute

            n "The enemy has [northEnemy3] health remaining."

            if northenemy3hitrate <= 7:
                play audio "audio/Something being hit - Sound Effect.opus" noloop
                n "The enemy does 20 damage to you."
        
                $ hp -= 20
        
                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding
                jump northEnemyTrenches 

            else: 
                n "The enemy misses."

                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding
            jump northEnemyTrenches
        
        label dfndNorthEnemies3:

            scene reverse trench hall

           
            
            if northenemy3hitrate <= 7:
                
                play audio "audio/Something being hit - Sound Effect.opus" noloop
                
                n "The enemy does 20 damage to you."

                n "You defend and take only 14 damage."
        
                $ hp -= 14
        
                n "You have [hp] health remaining."

                if hp < 1:
                    jump badEnding
                jump northEnemyTrenches
            else: 
                n "The enemy misses."

                n "You have [hp] health remaining."
            jump northEnemyTrenches

# Normal Route

label normalRoute:
    stop audio
    play music "audio/FarewellOfSlavianka.mp3" loop
    $ choicetrack = 2

    scene battle_1

    n "And thus, the fighting has concluded, your men have secured the enemy trenches." 
    
    n "They will celebrate, but then they must prepare for the counterattack that is to begin in a short while.{w} Looking at the surroundings at the moment, they will need to tend to the wounded."
    
    n "Your men gather up 14 wounded men.{w} Their injuries are life threatening, and they have to get to a field hospital, or they will die." 
    
    n "However, 3 of the wounded men are from the enemy side.{w} You only have 10 stretchers available." 
    label normalRouteChoice1:
        $ enemyStretcher = None
        python:
            while enemyStretcher is None:
                try:
                    enemyStretcher = int(renpy.input("How many of the enemies will you include in the stretcher?"))
                    
                except:
                    renpy.say(n,"Error, that is invalid, input number between 0 and 3.")
                    pass

    if 4 > enemyStretcher > 0:
        n "You send [enemyStretcher] enemies over."

        n "Your men are suspicious of you sending some of the enemies over." 
        
        n "You, on the other hand, claim the Hague conventions, and believe that the enemies that you sent over could be useful to you." 
    else: 
        n "Invalid number. Confused by what you say, your men do not send over any of the men."

    n "You may heal up with the medic, repair your armor with the armorer, upgrade your gun with the weaponsmith, and have the runner run back to home trench to report the capture of the enemy trenches and send for supplies."

    n "NOTE!!!{w} You can only choose two options."

    n "Choose wisely..."

    jump menunormalroute

label menunormalroute: 
    stop music
    play music "audio/HillsOfManchuria.mp3" loop volume 7
    scene mainTrench
    if choicetrack <= 3:
        menu:

            "HEAL UP" if not healupdone:
                jump healUp

            "REPAIR ARMOR" if not repairarmordone:
                jump repairArmor

            "UPGRADE WEAPON" if not upgradeweapondone:
                jump upgradeWeapon

            "REQUEST FOR SUPPLIES" if not runnersent:
                jump requestSupplies
            
    else:
        if prisoner == True:
            n "Now that that's done, you will now interrogate your prisoner."
            jump interrogationRoute 
        jump normalRouteContinuation

# Scene if you choose to heal up

label healUp:
    
    scene weaponsmithworkarea
    show medic 

    stop music fadeout 2
    play music "audio/medic OST.mp3" loop

    n "The medic was able to bump up your hp up by 75 points!"
    $ hp += 75
    $ choicetrack += 1
    n "He also give you 3 bandages."
    $ healupdone = True
    jump menunormalroute


# Scene if you choose to repair armor

label repairArmor:

    scene armorerworkarea
    show armorer

    stop music fadeout 2
    play music "audio/Armorer OST.mp3" loop

    n "You upgrade your armor with the armorer."
    $ hp += 100
    $ choicetrack += 1
    n "The newly upgraded armor bumps your hp up by 100 points!"
    $ repairarmordone = True
    jump menunormalroute

# Scene if you choose to upgrade weapon

label upgradeWeapon:
    
    scene weaponsmithworkarea
    show weaponsmith

    stop music fadeout 2
    play music "audio/weaponsmith OST.mp3" loop

    $ choicetrack += 1
    n "You upgrade your weapon with the weaponsmith."
    $ atk += 15
    n "The newly upgraded weapon bumps your attack up by 15 points!"
    $ upgradeweapondone = True
    jump menunormalroute

# Scene if you choose to request for supplies

label requestSupplies:

    scene no mans land

    n "You send the runner off with a message."

    y "I wish you luck, my friend."
    $ choicetrack += 1
    $ runnersent = True
    jump menunormalroute

# Scene when interrogation happens

label interrogationRoute:
    scene officer_bunker
    
    n "How do you want to speak to the prisoner?"
    
    menu:
        "AGGRESSIVE":
            jump Aggressive
        
        "CALM":
            jump Calm
    
    label Aggressive:
        
        if aggTrack == 0:
            
            y "I believe that you understand your place, Mr. Jakab. Cooperate with us now, lest you want to be tortured and broken."
            
            j " You Russians, no matter how brutal you are, will never break me.{w} I fight for my home country, my loved ones, and giving information to you will kill them."

            y "Fine, well then, last chance before you will be tortured."
            
            j "No, I will not break!"
            
            label torture:
                n "Will you torture?"
                
                menu:
                    "TORTURE":
                        jump torturesequence
                    
                    "DON'T TORTURE":
                        y "He was not of use to us."
                        jump normalRouteContinuation
                
                label torturesequence:
                    y "Fine by me, well then, let’s play a game of Russian roulette.{w} If you survive, then maybe you will tell us some useful information."
                    
                    y "If you die, then you die..."
                    
                    n "Jakab sweats profusely as your revolver is pointed to his head."
                    $ bullet = random.randrange(0,6)
                    
                    if bullet == 5:
                        play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop
                        n "He wasn't of any use to us..."
                        jump normalRouteContinuation
                    
                    else:
                        play audio "audio/misclick.mp3"
                        n "Okay, okay, I concede."
                        jump interrogatedRoute
        
        elif calmtrack == 1:
            y "You should know that you were the ones who started the war against us.{w} You will pay on our terms since you damaged and pillaged our property, our lands."
            
            j "But you did the same to us, you killed many of our people, and our men, such that many children may never see their fathers again.{w} Furthermore, you did that to yourselves with your scorched Earth policy. "

            y "This isn't going anywhere."

            jump normalRouteContinuation

    label Calm:
        
        if calmtrack == 0:
            
            y "I hope that you understand the seriousness of your situation, Mr. Jakab.{w} Your front lines have collapsed, and my men are merrily in your trenches."
            
            y "Now, please cooperate with us and maybe peace will come sooner than we expect."
            
            $ calmtrack += 1
            
            j "Your kind of peace will come, not ours, if I were to share information with you."
            jump interrogationRoute
        
        elif calmtrack == 1:
            y "Peace is peace. Don’t you want to see the children happy again, for their fathers come back home and safe, and have been delivered from death?"
            jump interrogatedRoute

label interrogatedRoute:
    j "Fine, I’ll concede.{w} So, I believe that the counterattack is delayed. Last I heard, they’re waiting for the supplies to get to them. "
    
    y "I see, the artillery?"
    
    j "You should prepare for that one, a spy heard of the plans of the offensive, and the artillery has been stockpiled.{w} They overdid it with their stocks, but they could easily blow up because they’ve been stockpiled."
    
    j "I told them to separate the caches but they haven’t done that yet."
    
    y "Alright, well then, thank you for that information. In accordance with the Hague conventions, we will treat you as our prisoner with honour."
    
    j " Thank you, good sir."
    jump interrogationEnd

label interrogationEnd:
    n "With that over, you tell your men what you learned.{w} One of your men suggested launching a raiding party on the ammunition."
    
    n "It’s very risky, but if all goes well, it could prove good against the counterattack."
    
    n "However, the artillery shelling interrupts the discussion, and you will be forced to continue it later into the night, once it has died down."
    
    scene officer_bunker
    
    n "The shelling has died down, and your men have suffered minimal casualties."
    
    k " Sir, we need to act now, there are three teams who are willing to undergo this operation. Sadly Sir, you may not go with them since you are needed here."
    
    y "Alright, who are these teams? Also, can’t they cooperate with each other?"
    
    k "Sorry Sir but you can only choose one team to go, the other two will have to stay to help with the defense. Furthermore, if we send all of them, they will be spotted easily due to their size."
    
    y " So, again, who are these teams?"
    
    k " Alright Sir, team 1 is made up fully of Ukrainians, Zapporizhian cossacks, in fact. 5 of them. They plan on using horses to get to the artillery quickly.{w} Team 2 is made up of Russians, they’ll get there on foot. It will take a while but it’s quiet and stealthy."
    
    k "Lastly, team 3 is made up of a mix of ethnic groups, but they will get the job done. They plan on digging all the way there but that will take a really long time."
    
    k "So, Sir, who do you choose?"
    
    menu:
        "TEAM 1":
            $ stuff = random.randrange(1,11)
            
            if stuff < 4:
                $ team1 = True
            
            else:
                $ team1 = False
        
        "TEAM 2":
            $ stuff = random.randrange(1,11)
            
            if stuff < 7:
                $ team2 = True
            
            else:
                $ team2 = False
        
        "TEAM 3":
            $ team3 = True
    
    $ interrogated = True
    
    k "Very well then Sir, I shall send that team out."
    jump normalRouteContinuation

label normalRouteContinuation:
    scene no mans land
    
    n "With that done, you and your men prepare for the coming offensive.{w} Perimeter guards and lookouts take the watch for any oncoming offensive."
    
    if interrogated == False:
        play audio "Artillery sfx.opus"
        n "Shelling occurs, you and your men expect this.{w} However, no offensive came, at least for today."
        
        n "Your men keep up with patrols and lookouts, but suffer heavy casualties as the shelling becomes heavy."
        
        $ heavyshelling = True
    
    if team1 == False and team2 == False and team3 == False:
        n "Your men keep up with patrols and lookouts, but suffer heavy casualties as the shelling becomes heavy."
        
        $ heavyshelling = True
    
    elif team1 == True:
        n "You are not certain if the team made it through, until an explosion ruptures into the night.{w} You and your men look in awe at the huge eruption far into the distance, on the austro-hungarian lines."
        
        n "Now, you are certain that they made it through."
    
    elif team2 == True:
        n "You are not certain if the team made it through. A few days have passed and no report comes.{w} However, as you are looking at the Austrian lines across no man’s land, you see a huge explosion that comes overhead."
        
        n "And then the bang comes, and it hits you, they managed it."
    
    elif team3 == True:
        n "The sappers start digging, but ultimately, it proves to be ineffective as it takes too long for them to even get anywhere near the ammo dumps.{w} The heavy shelling continues to affect your men."
        
        $ heavyshelling = True
        
        n "The Austro-Hungarian counteroffensive is coming quickly and you make the decision to abandon the project entirely.{w} But, you do keep the mines around and lay it brimming with explosives so that when it collapses, it takes down with it a lot of the Austro-Hungarian forces."
        
        $ mines = True
    
    if runnersent == True:
        n "Lucky you though, the supplies came through, your men won’t be starving tonight"
    
    else:
        n "Supplies do not come for you and your men. They begin to thirst and starve."
        
        $ starving = True
    
    n "Then the enemy finally comes…"
    
    k "Sir, the enemy is finally starting their attack. They have come to no man’s land."
    
    if starving == True:
        k "The men are starving though."
    
    if heavyshelling == True:
        k "The shelling has taken many of our men."
    
    if heavyshelling == True or starving == True:
        k "I’m not sure if we can take any more of this."
    
    elif heavyshelling == False or starving == False:
        k "We might survive though."
    
    y "Hope we just survive this"
    jump battle3

label battle3:
    $ battleturn = 14
    $ hordehp = 80
    stop music fadeout 3
    play music "ああああ - carnation (BMS差分).opus" loop
    
    scene no mans land
    
    n "The enemy appears on the horizon, charging slowly into your lines. The men open fire."
    
    if heavyshelling == True:
        $ hordehp += 120
        
        n "To soften your defensive positions, the Austro-Hungarian shelling intensifies."
        
        n "More men suffer because of this and the machine guns have become inaccurate"
        
        $ machineguns = False
    
        jump battle3menu

    else:
        n "The snipers start off by taking pot shots at who seem to be enemy officers and NCOs, they are wounded or killed by the fatal shots of the snipers."
        
        n "As soon as they get close enough, the machine guns spring into action, mowing down many of the Austro-Hungarian attackers."

        jump battle3menu

    if team3 == True:
        $ hordehp -= 80
        n "And then they get close enough for the mines to be effective.{w} You give the signal to blow up the mines."
        
        n "They explode and collapse with a loud and terrifying boom. The ground shakes and opens up underneath the attackers, swallowing, and drowning them into mud and mirk."
       
        n "It is a terrible sight to be at the receiving end of this spectacle, but you are thankful that you will not have to fight those who drown in mud today."
        
        n "It’s less men to deal with, after all."
        
        n "And now, it is time for you to fight as you spot an enemy close enough for you to shoot at with your revolver."

        jump battle3menu

    label battle3menu:
        $ horde1hitrate = random.randrange(1,11)

        n "Will you attack, take cover, heal, or reload?"
        while battle3count <= 8:
            menu:
                "ATTACK":
                    jump attackhorde1
            
                "TAKE COVER":
                    jump coverhorde1
            
                "HEAL":
                    jump healhorde1
            
                "RELOAD":
                    jump reloadhorde1
        jump meleeinTrenchesRoute

label attackhorde1:
    $ battle3count +=1
    n "You decide to attack!"
    
    play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop

    $ hordehp -= atk

    n "You deal [atk] damage!"

    n "The horde has [hordehp] hp remaining."

    if hordehp < 1:
        jump battle3End


    if horde1hitrate <= 2:
        
        n "The enemy answers back!"
        
        $ hp -= 50
    
        n "They do 50 damage to you!"

        if hp < 1:
            play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop

            scene black_screen

            with gunshotFade

            n "Game over, you died..."

            jump badEnding

        else:
            n "You have [hp] remaining."

            jump battle3menu
    else: 
        n "The enemy miss."

        n "You still have [hp] remaining."
    jump battle3menu

label coverhorde1:
    $ battle3count +=1
    n "You decide to take cover from incoming fire!"

    n "Your hp remains as [hp]."

    jump battle3menu

label healhorde1:
    $ battle3count +=1
    $ global bandages
    
    if bandages  > 0:
        n "You decide to heal up!"

        $ hp += 20

        n "You now have [hp] hp!"

    else:
        n "Unfortunately, you have no more bandages."

    if horde1hitrate <=2:
        n "The enemy hits you!"
        play audio "audio/Free Gunshot Sound Effects SFX Gunshots.mp3" noloop
        $ hp -= 50
    
        n "They do 50 damage to you!"

        if hp < 1:
            

            scene black_screen

            with gunshotFade

            n "Game over, you died..."

            jump badEnding

        else:
            n "You have [hp] remaining."

    jump battle3menu

label reloadhorde1:

    n "You decide to reload your weapons!"

    n "You are now ready to attack again!"

    jump battle3menu

label meleeinTrenchesRoute:
    
    n "Then, the enemy enters the trenches and begins to engage in chaotic hand to hand combat with your men."
    
    n "You draw your sword and prepare to fight, but you find one of your men who lays in front of you.{w} This man has taken a shot to his right arm, and is missing his entire left arm."
    
    n "His legs are of no use as the shrapnel has pierced and cut deep into them.{w} And yet, he is still alive.{w} You can only end his suffering."
    
    n "Will you kill him or try to send for a medic?"
    stop music fadeout 3
    play music "audio/FarewellOfSlavianka.mp3" loop fadein 10
    
    menu:
        "KILL":
            n "You give him the coup de grace."

            play audio "audio/Sword SFX 4.opus"
            
            n "You cut his throat, ending his misery."
        
        "SEND FOR MEDIC":
            n "You send for a medic, but none arrive."
            
            n "They are too busy dealing with the other men.{w} He speaks to you."
            
            

            s0 "Sir, will I die?"
            
            y " Don’t worry about it, no, no, you will live. The medic is coming don’t worry."
            
            s0 "Sir, please, continue the fight, even without us, so that our sacrifice will not be in vain."
            
            y " Rest quietly now, I assure you that your sacrifice is not in vain."
    
            

    n "With that done, you strengthen your resolve.{w} The war takes its toll on your men."
    
    label mtrm: # melee in trenches menu
        
        n "You fight the enemies in the trenches."
        
        menu:
            "ATTACK":
                jump mtra #melee in trenches attack
            
            "DEFEND":
                jump mtrd #melee in trenches defend

label battle3End:
    if team3 == True:
        n "Your mines were very effective in this battle."
    stop audio
    stop music fadeout 5
    play music "audio/FarewellOfSlavianka.mp3" loop
    n "The fighting has ended, you have lost a number of good men."
    
    n "You mourn your losses."
    
    if heavyshelling == False and starving == False:
        n "Your men praise you for your effective tactics in this battle."
    
    n "You go over your wounded, and find that Konstantin is fatally wounded.{w} His wound is deep, and there is very little chance of him surviving."
    
    k "Sir, I’m very sorry, I wasn’t able to see it to the end. My parents are still waiting for me back home."
    
    y "Shhh, shhh, take it easy now, rest easy now.{w} You’ve done your duty to the motherland."
    
    y "Your sacrifice isn’t in vain."
    
    k "Thank you sir."
    
    n "So it goes, {w}Konstantin is dead."
    
    n "You give him, {w}and many others, {w}a military funeral, {w}right on these trenches, {w}as you watch as their bodies sink deep into the mud. "
    
    n "You can’t mourn for long now.{w} The engineers have set up a direct phone line between you and Headquarters (HQ)."
    
    stop music fadeout 0.5
    play music "audio/Battlecontinues.mp3" loop 
    scene officer_bunker

    n "HQ informs you that a spy has notified them that the Germans are planning a counteroffensive against your lines,{w} and they’re stronger than the Austro-Hungarians."
    
    n "You question them about the northern offensive that was supposed to put pressure on them, but they respond with a shrug."
    
    n "They say that it didn’t work well."
    if enemyStretcher == 3:
        n "On the other hand, HQ informs you that the austro-hungarians have recovered, and they give you information.{w} They know about how the Germans usually conduct their offensive."

        n "They’ll start with a heavy artillery bombardment, firespotted for best effect.{w} After that, they will send in the bombers for cleanup operations."

        n "They don't have that many men, but you will still need anything you can to defeat them."
   
    n "Despite that, it will take a while since they still have to transport troops all the way down south."
    
    n "You have enough time to prepare.{w} The armorer, medic, and weaponsmith have prepared you and given you the rest of the upgrades that they can for the upcoming battle."
    
    n "Your sappers have enough time to build 3 of any of these 7 things:"
    
    label sappingtime:
        while count < 3:
            
            menu:
                "DEEPER TRENCHES" if not deepertrenchesDone:
                    jump deepertrenches
                
                "MORE MACHINE GUN POSITIONS" if not machinegunsDone:
                    jump moremachineguns
                
                "DIG MINES AND LAY THEM WITH EXPLOSIVES" if not digminesDone:
                    jump digmines
                
                "ADD BARBED WIRE" if not barbedwireDone:
                    jump barbedwire
                
                "ADD MORE BUNKERS" if not bunkersaddedDone:
                    jump bunkersadded
                
                "ADD REVETTING" if not revettingAddedDone:
                    jump revetting
                
                "ADD BOOBY TRAPS" if not boobytrapsDone:
                    jump boobytraps
            
            label deepertrenches:
                n "You dig deeper trenches,{w} these ensure that enemy artillery shells are less effective on your men. "
                
                $ deepertrenchesDone = True
                
                $ count += 1
                jump sappingtime
            
            label moremachineguns:
                n "You choose to add more machine gun positions.{w} They turn anything they’re pointed at into minced meat. {w}Best used against hordes of enemies. "
                
                $ machinegunsDone = True
                
                $ count += 1
                jump sappingtime
            
            label digmines: 
                n "Learning from previous experience, you tell your engineers to dig more mines and lay them with explosives.{w} When the enemy gets close enough, you can always rely on these mines. "
                
                $ digminesDone = True
                
                $ count += 1
                jump sappingtime
            
            label barbedwire:
                n "You add barbed wires. These slow down the enemy advance. It will take a while for the Germans to get through these."
                
                $ barbedwireDone = True
                
                $ count += 1
                jump sappingtime
            
            label bunkersadded:
                n "You add bunkers. These are protected fortifications. Good against enemy infantry and artillery. "
                
                $ bunkersaddedDone = True
                
                $ count += 1
                jump sappingtime
            
            label revetting:
                n "Your sappers use revetting techniques to fortify your trenches. They will do well against enemy artillery."
                
                $ revettingAddedDone = True
                
                $ count += 1
                jump sappingtime
            
            label boobytraps:
                n "You add booby traps in your trenches. These will be useful for the melee within the trenches."
                
                $ boobytrapsDone = True
                
                $ count += 1
                jump sappingtime
        
        jump conversation
    
    label conversation:
        n "With that done, you overhear some of your men."
        
        

        s1 "It would have been better if our emperor was dead."
        
      

        s2 "Yeah, what a load of bullshit. We’ve lost about, I’ve lost count of how many men so far. There was:"
        python:
            for i in peopleDead:
                renpy.say(s2, "{}".format(i))
        
        

        s1 "And don’t forget the many others."
        
        menu:
            "IT'S THE AUSTRO-HUNGRIANS THAT FORCED US INTO THIS WAR.":
                y " Hey, don’t say that, he may not be the best, but it’s the austro-hungarians who forced us into this war."
                
                s1 "What a load of shit. He dragged us into this war."
            
            "HE ISN'T ALL THAT BAD.":
                y "Come on now, he’s not all that bad. It’s because of him that we’ve become the Russian people of today."
                
                s1 "What a load of shit. We aren’t even as industrialized as other western nations."
        
        hide s1

        y "Think what you want of the emperor, you’re stuck in here with the rest of us. Damned to a place worse than hell on Earth."
        
        

        s2 "There’s no helping it, then. Let’s go, Rodion."

        

        n "They leave."
        
        n "What’s done is done. You feel bad for talking to your men like that, but such is life in warfare.{w} A few days pass, and the sappers are done building what you have asked them to build."
        
        n "You’ve asked high command for the reinforcements, but none arrive due to the large area that the Germans will attack.{w} “The big front” as it’s called."
        
        n "Good news though, the artillery is here for you.{w} They will commit to heavy shelling to help slow down the German advance."
        
        n "And so, with your preparations done, the German Counteroffensive begins."
        
        jump prebattle4

# When prebattle 4 starts

label prebattle4:
    scene no mans land
    $ men = 100
    $ germanInfantry = 75
    $ enemiesKilled = random.randrange(3, 8)

    while men > 20 and germanInfantry > 15:

        label phase1:
            stop music
            play music "audio/GermanArtillerySegment.mp3" fadein 0.2
            n "It begins with a heavy shower of accurate artillery fire which lasts for a couple of days. "

            if barbedwireDone == True:
                n "The barbed wire is taken out by this artillery fire instantly."

            if deepertrenchesDone == True:
                n "The deeper trenches that you dig protect your men from a lot of the artillery fire."

            else:
                n "Due to your shallow fortifications, your men are easily hit and injured by the heavy artillery shelling."

                $ men -= 25

                n "You lose 25 men because of this."

            if revettingAddedDone == True:
                n "The revetting that sappers add prevents trench sections from collapsing."

            else:
                n "You do not include revetting in sections of the trenches."
            
                $ men -= 23

                n "Some trench sections collapse and because of this, you lose 23 men. "

            if digminesDone == True:
                n "The mines dug hold, and are not affected by the heavy shelling."

            if machinegunsDone == True:
                n "The machine gun positions are protected enough against the shelling to not be heavily affected by it."

            if bunkersaddedDone == True:
                n "The bunkers you add hold well against the enemy artillery and protect the men inside."

            else:
                n " You did not build bunkers.{w} Your men are not protected from the heavy shelling. "
                
                $ men -= 25

                n "You lose 25 men because of this. "
            if men <= 10:
                jump surrenderending
            jump phase2

        label phase2:
            stop music fadeout 0.5
            play music "audio/GermanBombers.mp3" fadein 0.2
            n "And then, the German planes come."

            if machinegunsDone == True:
                n "The machine guns open up on the german planes.{w} They are very effective against them!"

                n "Your battle morale goes up!"
            else:
                n "There were not enough machine guns to shoot down the enemy planes." 
                
                $ men -= 28

                n "They deal heavy casualties to your men.{w} You lose 28 of them."

            if deepertrenchesDone == True:
                n "The deeper trenches protect the men from the bombing."
            else:
                n "The trenches weren’t deep enough to reduce the damage done by the enemy bombs."
                
                $ men -= 15
                
                n "Many of your men are affected by the bombing.{w} You lose 15 men."

            if revettingAddedDone == True:
                n "The revetting added to the trenches stops them from collapsing due to the German bombs."

            if bunkersaddedDone == True:
                n "The bunkers serve their role well against the bombing.{w} They protect the men from the bombing."

            else:
                n "You did not build bunkers.{w} Your men are out in the open."
                
                $ men -= 18

                n "The bombing incurs heavy casualties on your men.{w} You lose 18 of them."
            if men <= 10:
                jump surrenderending
            jump phase3

        label phase3:
            stop music fadeout 0.5
            play music "audio/GermanInfantry.mp3" fadein 0.2
            n "The German infantry finally comes.{w} There are about 75 of them against your [men] men.{w} Your men open fire."

            if machinegunsDone == True:
                
                $ germanInfantry -= 10
                
                n "The machine guns open fire on the Germans.{w} They get pinned down and lose 10 of their men."

            else:
                n "You did not build machine guns."
                
                $ men -= 15

                n "The enemy is not effectively pinned down. You lose 15 of your men."

            if bunkersaddedDone == True:

                n "The bunkers open fire on the Germans."
                
                $ germanInfantry -= 8

                n "They get pinned down.{w} They lose 8 of their men."

            else:
                n "You did not add bunkers."
                
                $ men -= 8

                n "The enemy can easily hit and target your men. You lose 8 of them."

            if digminesDone == True:
                n "You give the signal to the sappers to blow up the mines."
                
                $ germanInfantry -= 30

                n "They cause chaos in the enemy lines and are very effective.{w} The enemy loses 30 of their men."

            n "Even after all the bloodshed, they are relentless.{w} They get closer to you and your lines."

            n "Your artillery fires on the German forces who are now out in the open.{w} They scramble to whatever crater they can find for cover."
            
            n "Some artillery batteries already have those zeroed in.{w} Nowhere is safe."
            
            $ germanInfantry -= 12

            n "The Germans lose 12 of their men.{w} You take pot shots at the enemy, you might have killed [enemiesKilled] of them."
            
            $ germanInfantry -= enemiesKilled

            n "The kill rate of your men to enemies is 4:3. It’s a low kill rate but that’s to be expected." 
            
            $ men -= 20
            $ germanInfantry -= 15

            n "You lose 20 of your men at this point due to enemy fire, but your men are able to kill 15 of them." 
            if men <= 10:
                jump surrenderending
            if germanInfantry <= 15:
                jump finalbattleend
            

            jump phase4

        label phase4:
            stop music fadeout 0.5
            play music "audio/FinalPhase.mp3"
            n "Finally, we arrive at the chaos of melee in the trenches."

            n "The kill ratio at this point is about equal."

            if boobytrapsDone == True:
                n "The booby traps you set up are effective against the enemy soldiers."
                
                $ germanInfantry -= 10

                n "They kill about 10 of them, but are used up in the process."

            if men > germanInfantry:
                n "You have more men than the Germans, so you easily overpower the Germans and take them out!"

                jump finalbattleend

            else:
                n "You feel like you don’t have enough men for the upcoming battle.{w} However, you fight on."
                
                n "You barricade up in your bunker, shooting out at Germans that pass you by."
                
                n "You fight the German horde."

                jump finalbattlemenu

# When battle 4 starts

        label finalbattlemenu: 

            scene final_battle

            $ finalbattlehp = 100
            $ finalbattlebandages = 7
            $ barrierhp = 200
            $ finalbattleatk = 40
            $ finalbattleenemyhp = 5*(germanInfantry)
            $ finalbattleenemyatk = int(0.75*(germanInfantry))
            $ finalbattleenemyhitrate1 = random.randrange(1,5)
            $ finalbattleenemyhitrate2 = random.randrange(1,3)
            
            menu:
                "ATTACK":
                    jump finalbattleattack

                "HEAL":
                    jump finalbattleheal

        label finalbattleattack:
            n "You decide to attack!"

            $ finalbattleenemyhp -= finalbattleatk

            n "You deal 40 damage to the enemies!"

            n "The enemy has [finalbattleenemyhp] remaining."

            if finalbattleenemyhp < 0:
                n "You have defeated the enemy!"

                jump finalbattleend

            n "The enemy tries to retaliate!"

            if barrierhp > 0:
                
                if finalbattleenemyhitrate1 == 1:
                    
                    $ barrierhp -= finalbattleenemyatk
                    
                    n "The enemy does [finalbattleenemyatk] damage to your barriers!"

                    if barrierhp <= 0:
                        n "The enemies overpower you!{w} The barrier you have is now down!"

                        jump finalbattlemenu

                    else:
                        n "The enemy does [finalbattleenemyatk] damage to your barriers!"

                        jump finalbattlemenu

            else:
                if finalbattleenemyhitrate2 == 1:
                    n "The enemy does [finalbattleenemyatk] damage to you!"
                    
                    $ finalbattlehp -= finalbattleenemyatk
                    
                    n "You have [finalbattlehp] remaining."

                    if finalbattlehp <= 0:
                        n "The enemies overpower you!{w} There's no where to run or hide..."

                        jump badEnding

            jump finalbattlemenu

        label finalbattleheal:
            
            if finalbattlebandages > 0:
                n "You use 1 bandage"
                
                $ finalbattlehp += 20
                
                n "You heal to [finalbattlehp] hp."
                
                $ finalbattlebandages -= 1 
                
                n "You have [finalbattlebandages] remaining."
            
            else:
                n "You have no more bandages remaining."
            
            if barrierhp > 0:
                
                if finalbattleenemyhitrate1 == 1:
                    
                    $ barrierhp -= finalbattleenemyatk
                    
                    n "The enemy does [finalbattleenemyatk] damage to your barriers!"

                    if barrierhp <= 0:
                        n "The enemies overpower you!{w} The barrier you have is now down!"

                        jump finalbattlemenu

                    else:
                        n "The enemy does [finalbattleenemyatk] damage to your barriers!"

                        jump finalbattlemenu

            else:
                if finalbattleenemyhitrate2 == 1:
                    n "The enemy does [finalbattleenemyatk] damage to you!"
                    
                    $ finalbattlehp -= finalbattleenemyatk
                    
                    n "You have [finalbattlehp] remaining."

                    if finalbattlehp <= 0:
                        n "The enemies overpower you!{w} There's no where to run or hide..."
                        jump badEnding
    
    jump surrenderending

# Scene if you win final battle

label finalbattleend:
    
    scene battle_1
    
    stop music fadeout 2
    play music "audio/FinalBattleEnd.mp3" 
    
    n "At long last, the battle is over."

    n "Despite that, your victory is short-lived."

    n "HQ orders you to retreat."

    n "The Germans have broken through a trench section, and that must be contained."

    n "Knowing that you’ve already lost many men today, you follow HQ’s orders and prepare for the retreat."
    
    jump goodending


# Surrender Ending

label surrenderending:
    stop music fadeout 2
    play music "surrenderOST.mp3" volume 7
    scene surrender 
    n "With not enough men left to fight, you surrender.{w} You force your men to follow suit."
    
    n "You raise a white flag, and the Germans understand it.{w} Despite that, they are still suspicious of you. They order you to come out, hands in the air, and walk to their lines."
    
    n "You do what they order, and they treat you nicely enough.{w} They take you and your men into custody and transport you and your men on train to different prison camps deeper into Germany."
    
    n "You are separated from your men at this point.{w} The condition of the prison camp that you stay at is horrible.{w} Men starve all year round, food and water shortages are common, labor conditions are terrible, and disease runs rampant."
    
    n "You catch the Spanish flu at one point, but you luckily manage to survive that, in a prison camp of all places.{w} Winter rolls around, the conditions worsen further."
    
    n "At long last, the Germans surrender, and the treaty of Brest-Litovsk has been signed.{w} You are to be repatriated into Russia, but it is embroiled in a civil war."
    
    n "You decide to be repatriated under the white army.{w} You will need to fight once again."
    
    scene the_end

    jump end_screen

# Good Ending

label goodending:
    scene GoodEnding
    play music "Good Ending OST.mp3" volume 7
    "As the sun dipped below the horizon,{w} casting long shadows across the tranquil Russian countryside,{w} I,{w} a weary Tsarist officer,{w} finally approached the familiar village where my family had lived for generations."
    
    "The war had taken me away for what felt like an eternity,{w} and the thought of reuniting with my loved ones filled me with both anticipation and anxiety."

    "As I entered the village,{w} the quaint cottages,{w} the gentle rustling of leaves in the nearby birch grove,{w} and the distant echoes of children playing washed over me."

    "The familiar sights and sounds brought tears to my eyes,{w} for I had dreamt of this moment for so long."

    "In the embrace of my loving family and the warm embrace of our close-knit village,{w} I found solace,{w} healing,{w} and the strength to move forward."

    "The war was now a distant memory,{w} and in the company of those I loved most,{w} I realized that the most profound victories were not won on the battlefield but in the enduring bonds of family. "

    "But this will not last for long."

    "Mother Russia is embroiled in a civil war between the brutal red army and the unforgiving white army."

    "In time,{w} I will have to fight again,{w} in another horrible war,{w} but now is not that time,{w} as I keep to the embrace of my family,{w} and enjoy the peace that surrounds me."
    
    scene the_end

    jump end_screen

# End screen

label end_screen:
    
    scene black_screen
    
    # Display credits
    "Game Credits:"
    "Developer: Jared Villanueva, Stephen Ventanilla, Julian Isidro"
    "Artwork: Urvi Rayudu"
    "Music: Julian Isidro"
    "Marketing: Jasmine Wright"
    
    stop music
    $ renpy.full_restart()

    $ renpy.Quit(confirm = None)
    
    # Add more credits as needed
