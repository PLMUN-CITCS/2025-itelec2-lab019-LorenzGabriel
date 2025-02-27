def get_student_score():
    # Prompt the user to enter their score
    score_input = input("Please enter your score: ")
        
def calculate_grade(score):
    # Determine the letter grade based on the score
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
