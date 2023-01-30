def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you
bad_score_message: "Bad Score"
try:
    score = float (input("Enter score:"))
    if score < 0.6: 
        grade = "F"
    elif score >= .61 and score <=.69:
        grade = "D"
    elif score >= 0.7 and score <= 0.79:
        grade = "C"
    elif score >= 0.8 and hrs <= 0.89:
        grade = "B"
    elif hrs >= 0.9 and  hrs < 1.00:
        grade = "A"
    else:
        grade = "Bad Score"
except:
        grade = "Bad Score"

print(grade)

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
