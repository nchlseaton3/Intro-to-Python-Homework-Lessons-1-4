# Grade average calculator
# Functions
def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

def get_letter_grade(average):
    if average >= 90:
        return "A, Pass congrats"
    elif average >= 80:
        return "B, Keep up the good work"
    elif average >= 70:
        return "C, not quite but almost there "
    elif average >= 60:
        return "D, study a little harder"
    else:
        return "F, see me after class"

#Collect scores  
scores = []
num_scores = int(input("How many test scores do you wish to enter?"))

count = 0
while count < num_scores:
    score = float(input(f"enter score {count + 1}: "))
    scores.append(score)
    count += 1

# Calculate results
average = calculate_average(scores)
letter = get_letter_grade(average)

# Report 
print("\n===Grade Report===")
print(f"Test Scores : {scores}")
print(f"Average Score: {average:.2f}")
print(f"Letter Grade: {letter}")