# "DBD Perk Randomizer"
# Perks broken up by survivor and Killer categories

# Further divided by type of perk (aura, notification, 
# escape, regression, etc....)

# Randomly chooses four perks with no repeat selection

# Add random offerings and add-ons later
import random as rnd
import time

survivor = ["Windows of Opportunity", "Adrenaline", "Resilience", "Made for This", "Lithe", "Sprint Burst", "Deja Vu", "Dead Hard",
            "Bond", "Prove Thyself", "Distortion", "Unbreakable", "Kindred", "Off the Record", "Self-Care", "We'll Make It", "Hope",
            "Balanced Landing", "Botany Knowledge", "Inner Strength", "Decisive Strike", "Quick & Quiet", "Blast Mine", "Iron Will", 
            "Flashbang","Boil Over", "Background Player", "Alert", "Empathy", "Lightweight", "Deliverance", "Fixated", "Calm Spirit", 
            "Buckle Up", "Saboteur", "Head On", "Urban Evasion", "For the People", "Boon: Circle of Healing", "Spine Chill", "Borrowed Time"
            , "Technician", "Stake Out", "Flip-Flop", "Any Means Necessary", "Built to Last", "Plot Twist", "Vigil", "Breakout",
            "Hyperfocus", "Wiretap", "Second Wind", "Tenacity", "Bite the Bullet", "Reassurance", "Left Behind", "Plunderer's Instinct", 
            "Lucky Break", "Babysitter", "Fogwise", "Dark Sense", "Overcome", "Desperate Measures", "Dramaturgy", "Power Struggle", 
            "Slippery Meat", "Boon: Shadow Step", "Leader", "We're Gonna Live Forever", "No One Left Behind", "Dance With Me", "Overzealous", 
            "Diversion", "Boon: Exponential", "Light-footed", "Smash Hit", "Autodidact", "Small Game", "Better Together", "Streetwise", 
            "Wake Up!", "Deception", "Open-Handed", "Breakdown", "Troubleshooter", "Premonition", "Sole Survivor", "Residual Manifest", 
            "Chemical Trap", "Ace in the Hole", "Detective's Hunch", "Soul Guard", "Resurgence", "Reactive Healing", "Clairvoyance", 
            "This Is Not Happening", "Object of Obsession", "Potential Energy", "Camaraderie", "Aftercare", "Mettle of Man", "Parental Guidance", 
            "Fast Track", "Repressed Alliance", "Counterforce", "Empathic Connection", "No Mither", "Appraisal", "Scavenger", "Scene Partner", 
            "Lucky Star", "Boon: Dark Theory", "Friendly Competition", "Low Profile", "Solidarity", "Visionary", "Blood Rush", "Blood Pact",
            "Better Than New", "Cut Loose", "Rookie Spirit", "Quick Gambit", "Pharmacy", "Self-Preservation", "Poised", "Teamwork: Power of Two", 
            "Red Herring", "Inner Focus", "Up the Ante", "Corrective Action", "Teamwork: Collective Stealth"]

killer = ["Scourge Hook: Pain Resonance", "Pop Goes the Weasel", "Surge", "Corrupt Intervention", "Lethal Pursuer", "barbecue & Chili", "Save the Best for Last", 
          "Nowhere to Hide", "Sloppy Butcher", "Deadlock", "Bamboozle", "No Way Out", "Brutal Strength", "Hex: No One Escapes Death", "Shadowborn", "Ultimate Weapon", 
          "Eruption", "Discordance", "Enduring", "A Nurse's Calling", "Agitation", "Mindbreaker", "Overcharge", "Hex: Plaything", "Lightborn", "Dead Man's Switch", "Rapid Brutality", 
          "Call of Brine", "Tinker", "Hex: Devour Hope", "Hex: Ruin", "Thanatophobia", "Iron Grasp", "Spirit Fury", "Scourge Hook: Floods of Rage", "Franklin's Demise", "I'm All Ears", 
          "Thrilling Tremors", "Iron Maiden", "Play With Your Food", "Darkness Revealed", "Coup de Grace", "Bitter Murmur", "Hex: Pentimento", "Hex: Undying", "Trail of Torment", 
          "Infectious Fright", "Merciless Storm", "Blood Warden", "Spies from the Shadows", "Hex: Bloodfavor", "Distressing", "Friends 'Til the End", "Monitor & Abuse", "Scourge Hook: Gift of Pain", 
          "Superior Anatomy", "Hex: Face the Darkness", "Unrelenting", "Cruel Limits", "Blood Echo", "Starstruck", "Oppression", "Gearhead", "Hex: Huntress Lullaby", "Dissolution", "Alien Instinct", 
          "Furtive Chase", "Nemesis", "Hex: Thrill of the Hunt", "Hubris", "Surveillance", "Fire Up", "Zanshin Tactics", "Rancor", "hex: Haunted Ground", "Mad Grit", "Dying Light", "Scourge Hook: Monstrous Shrine", 
          "Unnerving Presence", "Make Your Choice", "Deerstalker", "Batteries Included", "Hex: Two Can Play", "Awakened Awareness", "Remember Me", "Coulrophobia", "Dragon's Grip", "Hysteria", "Forced Hesitation", 
          "Knockout", "Whispers", "Beast of Prey", "Terminus", "Dark Devotion", "Game Afoot", "Hex: The Third Seal", "Insidious", "Forced Penance", "Hex: Retribution", "THWACK!", "Hex: Crowd Control", "Grim Embrace", 
          "Bloodhound", "Machine Learning", "Predator", "Deathbound", "Stridor", "Leverage", "Overwhelming Presence", "Genetic Limits", "Territorial Imperative", "Scourge Hook: Hangman's Trick", "Septic Touch", "Hoarder", 
          "Shattered Hope"]

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

