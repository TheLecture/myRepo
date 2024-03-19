import sys

def solve_exercise(expression):
    try:
        # פיצול הביטוי למספרים ולסימן הפעולה
        parts = expression.split()
        num1 = int(parts[0])
        operator = parts[1]
        num2 = int(parts[2])
        
        # חישוב התוצאה
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            return "Invalid operator"
        
        # החזרת התוצאה
        return f"{num1} {operator} {num2} = {result}"
    except Exception as e:
        return f"Error solving expression: {str(e)}"

def solve_exercises(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            exercises = infile.readlines()
        
        with open(output_file, 'w') as outfile:
            for exercise in exercises:
                result = solve_exercise(exercise.strip())
                outfile.write(result + '\n')
        
        print(f"Solved exercises saved to {output_file}")
    except Exception as e:
        print(f"Error solving exercises: {str(e)}")

# קריאה לפונקציה והשימוש בפרמטרים מהפקודה שהתבצעה
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        solve_exercises(input_file, output_file)
 