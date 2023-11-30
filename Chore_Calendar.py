# Robert's Chore Calendar
# Calendar to track chores by day of the week and who is performing each chore
# Will use date and time along with two lists:  "family" and "chores"
# This will then be output to a table for viewing/ modification
from datetime import date
import random

today = date.today()
date = today.strftime("%A %d, %b, %y") #day <numb>, mon, yr
family_list = ["Aimee", "Alex", "Robert"]
chores_list = ["Do the Dishes", "Empty the Dishwasher", "Clean the Cat Box", "Take Out the Trash",
          "Change the Trash Bag", "Breakdown the Recycling", "Sweep the Floor", "Do the Laundry"]
random_family = random.randint(0, 2)    #randomly chooses a number from 0 - 2 matching family_list index values.
random_chore = random.randint(0, 7)     #randomly chooses a number from 0 - 7 matching chores_list index values.
worker = family_list[int(random_family)]    #Variable calling randomly chosen index in family_list.
chore = chores_list[int(random_chore)]      #Variable calling randomly chosen index in chores_list.

print("Welcome to Robert Ryan's Chore Picker.")
automated = input("Would you like a completely random output? (Y or N).\n")     #Randomly chooses a worker and chore.
if automated.lower() == "y":
    print(f"{worker} will {chore} today, {date}.")
else:
    victim = input("Who will be doing chores? 0 for Mom, 1 for Alex, and 2 for Dad.\n")
    if int(victim) == 0:        #Random chore for Mom.
        print(f"Mom will {chore} today, {date}.")
    elif int(victim) == 1:      #Random chore for Alex.
        print(f"Alex will {chore} today, {date}.")
    elif int(victim) == 2:      #Random chore for Dad.
        print(f"Dad will {chore} today, {date}.")