# Password Strength Checker

password = input("Enter your password: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check for numbers
has_number = False
for char in password:
    if char.isdigit():
        has_number = True
        score += 1
        break

# Check for uppercase letters
has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
        score += 1
        break

# Check for symbols
symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

has_symbol = False
for char in password:
    if char in symbols:
        has_symbol = True
        score += 1
        break

# Display result
if score <= 1:
    print("Weak Password")
elif score <= 3:
    print("Medium Password")
else:
    print("Strong Password")