# Initialize variables to hold the marks for three subjects
subject1 = -1
subject2 = -1
subject3 = -1

# Loop to ensure the user enters marks within the valid range (0-100)
while subject1 < 0 or subject1 > 100:
    # Prompt the user to enter marks for subject1
    subject1 = int(input("Enter marks for subject1 (0-100): "))
    
while subject2 < 0 or subject2 > 100:
    subject2 = int(input("Enter marks for subject2 (0-100): "))

while subject3 < 0 or subject3 > 100:
    subject3 = int(input("Enter marks for subject3 (0-100): "))

# Calculate the average score
average_score = (subject1 + subject2 + subject3) / 3

# Determine the grade based on the average score
if average_score >= 70 and average_score <= 100:
    grade = "A"
elif average_score >= 60:
    grade = "B"
elif average_score >= 50:
    grade = "C"
elif average_score >= 40:
    grade = "D"
else:
    grade = "Fail"

# Print the grade
print("Your grade is:", grade)
