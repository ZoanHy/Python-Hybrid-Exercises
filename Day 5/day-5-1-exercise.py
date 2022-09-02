
student_heights = input("Input a list of student heights ").split(" ")
total_height = 0
total_length = 0

for student_height in student_heights:
    total_height += int(student_height)
    total_length += 1
    
average = round(total_height / total_length)
    
print(average)
