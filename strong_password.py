#תוכנה שבודקת חוזק סיסמא לפי קריטריונים מסויימים.
print("hello choose your password.")
print("Your password must be at least 6 characters long and contain at least one uppercase letter, one lowercase letter, one digit, one special character, no space, no sequential characters or numbers and no repeated characters or numbers in a row.")
#בודק אם הסיסמא מכילה רצפים של תווים או מספרים
sequences = ["0123456789", "9876543210", "abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"]
def is_sequential(password):
    password = password.lower()
    for seq in sequences:
        for i in range(len(seq) - 2):
            if seq[i:i+3] in password:
                return True
    return False
while True: 
    input_password = input("Enter your password: ")
    #בדיקה אם הסיסמא עומדת בכל הקריטריונים
    if len(input_password) < 6:
        print("Password is too short. It must be at least 6 characters long.")
    elif not any(char.isupper() for char in input_password):
        print("Password must contain at least one uppercase letter.")
    elif not any(char.islower() for char in input_password):
        print("Password must contain at least one lowercase letter.")
    elif not any(char.isdigit() for char in input_password):
        print("Password must contain at least one digit.")
    elif not any(char in "!@#$%^&*()-+" for char in input_password):
        print("Password must contain at least one special character.")
    elif " " in input_password:
        print("Password must not contain spaces.")
    elif any(input_password[i] == input_password[i+1] for i in range(len(input_password)-1)):
        print("Password must not contain repeated characters or numbers in a row.")
    elif is_sequential(input_password):
        print("Password must not contain sequential characters or numbers.")
    else:
        print("Password is strong.")
        break
