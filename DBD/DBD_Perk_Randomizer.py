# "DBD Perk Randomizer"
# Perks broken up by survivor and Killer categories- COMPLETE

# Further divided by type of perk (aura, notification, 
# escape, regression, etc....) - NOT YET STARTED

# Randomly chooses four perks with no repeat selection- COMPLETE

# Add random offerings and add-ons later- NOT YET STARTED
import random as rnd
import time
from role_skills import survivor,killer
from dbd_art import logo

print(logo)
print("Welcome to Rob's Dead By Daylight Perk Randomizer!")
Survivor_perks = rnd.sample(survivor, 4)
Killer_perks = rnd.sample(killer, 4)
role = input("What role are you playing?  Killer or Survivor?: \n")
if role.lower() == "survivor":
    print("Working on finding you four random Survivor perks!")
    time.sleep(3)
    print(f"Your Loadout for Survival has Arrived!\n {Survivor_perks}")
    reroll_surv = input("Would you like to reroll (Y or N)?:\n")
    while reroll_surv.lower() == "y":
        print("Lets give this another try!")
        time.sleep(3)
        print(rnd.sample(survivor, 4))
        final_reroll_surv = input("Are you satisfied with your loadout (Y or N)?\n")
        if final_reroll_surv.lower() == "n":
            print("Maybe round three will have what you want!")
            time.sleep(3)
            print(rnd.sample(survivor, 4))
            print("Please come again!")
        else:
            print("Goodluck out there against the entity!")
        break    

elif role.lower() == "killer":
    print("Working on finding you four random killer perks!")
    time.sleep(3)
    print(f"Your Loadout for the hunt has arrived!\n {Killer_perks}")
    reroll_killer = input("Would you like to reroll (Y or N)?:\n")
    while reroll_killer.lower() == "y":
        print("Lets give this another try!")
        time.sleep(3)
        print(rnd.sample(killer, 4))
        final_reroll_killer = input("Are you satisfied with your loadout (Y or N)?\n")
        if final_reroll_killer.lower() == "n":
            print("Maybe round three will have what you want!")
            time.sleep(3)
            print(rnd.sample(killer, 4))
            print("Please come again!")
        else:
            print("Goodluck out there, bring the Entity bountiful tribute!")
        break
else:
    print("Invalid entry!  Be gone with you!")

