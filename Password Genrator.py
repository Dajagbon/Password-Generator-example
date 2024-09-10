import os
import random
import string
import datetime

# Function to generate a memorable password
def generate_memorable_password(num_words, cases):
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    password = []
    for _ in range(num_words):
        word = random.choice(words)
        if cases == "upper":
            word = word.upper()
        elif cases == "lower":
            word = word.lower()
        elif cases == "title":
            word = word.title()
        word += str(random.randint(0, 9))
        password.append(word)
    return "-".join(password)

# Function to generate a random password
def generate_random_password(length, include_punctuation, exclude_chars):
    characters = string.ascii_letters + string.digits
    if include_punctuation:
        characters += string.punctuation
    characters = ''.join([c for c in characters if c not in exclude_chars])
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to save password to file
def save_password(password, password_type):
    now = datetime.datetime.now()
    timestamp = now.strftime("%A, %B %d, %Y %I:%M:%S %p")
    directory = password_type.capitalize()
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, "Generated_Passwords.txt")
    with open(file_path, "a") as file:
        file.write(f"{password} - {timestamp}\n")

# Main function to generate passwords
def main():
    for _ in range(1000):
        password_type = random.choice(["memorable", "random"])
        if password_type == "memorable":
            num_words = random.randint(2, 5)
            cases = random.choice(["upper", "lower", "title"])
            password = generate_memorable_password(num_words, cases)
        else:
            length = random.randint(8, 16)
            include_punctuation = random.choice([True, False])
            exclude_chars = random.choice(["", "aeiou", "12345", "!@#$%"])
            password = generate_random_password(length, include_punctuation, exclude_chars)
        save_password(password, password_type)

if __name__ == "__main__":
    main()
