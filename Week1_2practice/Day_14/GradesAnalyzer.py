 # Grade analyzer

def claculate_Grade(score):
    if score > 100:
        return "Invalid score"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
students ={}

while True:
    name = input("Enter student name (or 'done' to finish) : ")
    if name.lower() == 'done':
        break
    score = input(f"Enter {name}'s score (0-100) : ")
    if not score.isdigit() or (0 <= int(score) > 100):
        print("Invalid score. Please enter a number from 0 to 100.")
        continue

    students[name] = int(score)
    print(students)
    break