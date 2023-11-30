import csv
from datetime import date
import random
today = date.today()
house_hold = ["Mom", "Dad", "Alex"]
date = today.strftime("%m/%d/%y")
print("Welcome to the Cat Box Cleaner Tool, may the odds ever be in your favor.")
user_number = random.randint(0, 2)
cleaner = house_hold[int(user_number)]
print("The unfortunate soul who has to clean the cat box today is.......")
chosen_cleaner = f"{cleaner}:{date}"
print(chosen_cleaner)
with open('cleaner_history1.csv', 'a', newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerow(chosen_cleaner)
cleaner_history = input("Would you like to view cleaning history? (Y or N)?\n")
if cleaner_history.lower() == 'y':
    with open("cleaner_history1.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)

else:
    print("Goodbye!")