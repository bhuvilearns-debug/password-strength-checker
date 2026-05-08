import random
password = input("Enter your password: ")

# List of commonly used passwords
common_passwords = [
    "123456",
    "password",
    "123456789",
    "qwerty",
    "admin",
    "admin123",
    "welcome",
    "password123"
]

score = 0

# Check password length
if len(password) >= 8:
    score += 1
else:
    print("Password should be at least 8 characters long.")

# Check for uppercase letters
if any(char.isupper() for char in password):
    score += 1
else:
    print("Add at least one uppercase letter.")

# Check for numbers
if any(char.isdigit() for char in password):
    score += 1
else:
    print("Add at least one number.")

# Check for special characters
if any(char in "!@#$%^&*" for char in password):
    score += 1
else:
    print("Add at least one special character.")

# Check if password is common
is_common = password.lower() in common_passwords

print("\nPassword Strength Result:")

if is_common:
    print("This password is commonly used and insecure.")
    print("Choose a more unique password.")

# Password strength evaluation
if score == 1:
    print("Strength: Very Weak")

elif score == 2:
    print("Strength: Weak")

elif score == 3:
    print("Strength: Medium")

elif score == 4:
    print("Strength: Strong")
# Passphrase Generator

words = [
    "Tiger",
    "Moon",
    "Coffee",
    "Cyber",
    "Shadow",
    "Rocket",
    "Secure",
    "Matrix"
]

special_chars = "!@#$%^&*"

generated_password = (
    random.choice(words) +
    random.choice(words) +
    str(random.randint(10, 99)) +
    random.choice(special_chars)
)

print("\nSuggested Secure Passphrase:")
print(generated_password)