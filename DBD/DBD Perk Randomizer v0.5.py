# # DBD Perk Randomizer v0.5
# # Version should include expanded roles where perks are retrievable by purpose randomy.
# # Intended to allow user to keep rerolling "loadouts" as much as they wish.

from dbd_art import logo
from Expanded_roles import survivor, killer, unrestricted_survivor, unrestricted_killer
import time
import random as rnd

def Perk_Randomizer():
#  random_all = True
   loadout = []
#    while  random_all:
#     role_selection = input("Will you be playing Survivor or Killer?: \n")
#     full_random = input("Would you like to create a fully random Loadout? (Y or N): \n")
#     while full_random.lower() == "y":
#         if role_selection.lower() == "survivor" and full_random.lower() == "y":
#             random_unrestricted_survivor()
#         elif role_selection.lower() == "killer" and full_random.lower() == "y":
#             random_unrestricted_killer()
#     else: 
#         random_all = False
#     if role_selection.lower() == "survivor":
#         for type in survivor:
#             print(type)
#         print("No Preference")


perk_slots = 4
loadout = []
while perk_slots > 0:
    perk_category  = input("Please choose a perk category (1=Survival, 2=Healing, 3=Aura, 4=Teamwork, 5=Endgame, or 6=No Preference):\n")
    if perk_category == "6":
        loadout += (rnd.sample(unrestricted_survivor, 1))
    elif perk_category == "1":
        loadout += (rnd.sample(survivor["Survival"], 1))
    elif perk_category == "2":
        loadout += (rnd.sample(survivor["Healing"], 1))
    elif perk_category == "3":
        loadout += (rnd.sample(survivor["Aura"], 1))
    elif perk_category == "4":
        loadout += (rnd.sample(survivor["Teamwork"], 1))
    else:
        loadout += (rnd.sample(survivor["Endgame"], 1))
perk_slots - 1
print(f"Your loadout is {loadout}!")

        

# Function to do a full random selection of Survivor perks.
def random_unrestricted_survivor():
    survivor_perks = rnd.sample(unrestricted_survivor, 4)
    time.sleep(3)
    print(f" Your loadout is {survivor_perks}")
    reroll = input("Do you wish to reroll your loadout? (Y or N): \n")
    if reroll.lower() == "y":
        random_unrestricted_survivor()
    else:
        Perk_Randomizer()

# Function to do a full random seletion of Killer perks.
def random_unrestricted_killer():
    killer_perks = rnd.sample(unrestricted_killer, 4)
    time.sleep(3)
    print(f" Your loadout is {killer_perks}")
    reroll = input("Do you wish to reroll your loadout? (Y or N): \n")
    if reroll.lower() == "y":
        random_unrestricted_killer()
    else:
        Perk_Randomizer()
        

print(logo)
print("Welcome to DBD Perk Randomizer Utility v0.5")
Perk_Randomizer()


print(survivor["Survival"])
