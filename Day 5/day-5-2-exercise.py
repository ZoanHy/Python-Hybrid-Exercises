import os
os.system("cls")

student_scores = input("Input a list of student scores ").split()
score_max = int(student_scores[0])
for n in student_scores:
  if int(n) > score_max:
      score_max = int(n)

print(f"The highest score in the class is: {score_max}") 
  