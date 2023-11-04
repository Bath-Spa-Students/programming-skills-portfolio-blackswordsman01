#Average and Perceentage
num_courses = int(input("Enter the number of courses: "))
total_score = 0

for i in range(num_courses):
    mark = float(input(f"Enter the mark for course {i + 1}: "))
    total_score += mark

average_mark = total_score / num_courses
percentage = (total_score / (num_courses * 100)) * 100

print(f"Average Mark: {average_mark:.2f}")
print(f"Percentage: {percentage:.2f}%")