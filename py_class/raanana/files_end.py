# קליטת נתיב לקובץ מהמשתמש
file_path = input("please enter path:\n ")

# פתיחת הקובץ לקריאה
with open(file_path, 'r') as file:
    # קריאת כל השורות של הקובץ
    lines = file.readlines()
    # מספר התווים בקובץ
    num_chars = sum(len(line) for line in lines)
    # מספר השורות בקובץ
    num_lines = len(lines)

# הדפסת הנתונים
print("file name: ", file_path)
print("chars in file: ", num_chars)
print("lines in file", num_lines)