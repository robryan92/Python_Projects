# # student_scores = {
# #   "Harry": 81,
# #   "Ron": 78,
# #   "Hermione": 99, 
# #   "Draco": 74,
# #   "Neville": 62,
# # }
# # student_grades = {}

# # for student in student_scores:
# #   score = student_scores[student]
# #   if score > 90:
# #     student_grades[student] = "Outstanding"
# #   elif score > 80:
# #     student_grades[student] = "Exceeds Expectations"
# #   elif score > 70:
# #     student_grades[student] = "Acceptable"
# #   else:
# #     student_grades[student] = "Fail"

# # print(student_grades)

# # Travel log challenge

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
}

# Retrieve data from a dictionary
# print(programming_dictionary["Bug"])

# Adding a new item into a dictionary

programming_dictionary["Human"] = "Sentient lifeform from planet earth"
# print(programming_dictionary)

# Create new dictionary that is empty
empty_dictionary = {}

# Wiping a dictionary
# programming_dictionary = empty_dictionary
# print(programming_dictionary)

# Edit an item in a dictionary
# programming_dictionary["Bug"] = "An moth in your computer"
# print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
# #######################################################
# Nesting
  capitals = {
    "France": "Paris",
    "Germany": "Berlin",
  }

# Nesting a list in a dictionary

travel_log = {
  "France": ["Paris, Lille, Dijon"],
  "Germany": ["Berlin, Munich, Stuttgart"],
}

# Nesting a dictionary in a dictionary

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12,
  },
  "Germany": {
    "cities_visited": ["Berlin", "Munich", "Stuttgart"],
    "total_visits": 5,
  },
}

# Nesting dictionary in a list
travel_log = [
  {"Country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12,
  },
  {"Country": "Germany",
    "cities_visited": ["Berlin", "Munich", "Stuttgart"],
    "total_visits": 5,
  },
]