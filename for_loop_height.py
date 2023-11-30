student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height

Number_Students = 0
for student in student_heights:
  Number_Students += 1

average_height = round(total_height / Number_Students)
print(f"total height = {total_height}")
print(f"number of students = {Number_Students}")
print(f"average height = {average_height}")