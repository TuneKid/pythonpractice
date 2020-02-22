import random
print("hello grades")
grades = ["A+", "A", "A-", "B"]
people = ["Abey", "Sindhu", "Joshua", "Hunter"]
for x in people:
  grade = random.choice(grades)
  if x == "Abey":
    grade = "F- in all subjects"
  if x == "Joshua":
    grade = "A+++ in English"
  print(x + " got an " + grade )
  