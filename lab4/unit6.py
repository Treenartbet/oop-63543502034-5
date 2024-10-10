# Given a list of student grades, calculate the average grade for each student and store them in a dictionary.

grades = {'Alice': [85, 90, 92], 'Bob': [88, 87, 85], 'Charlie': [90, 91, 89]}  # Dictionary of student grades
average_grades = {}  # Dictionary to store average grades

# Calculate the average grade for each student
for student, grade_list in grades.items():
    average_grades[student] = sum(grade_list) / len(grade_list)

# Print the result
print("Average Grades:", average_grades)
