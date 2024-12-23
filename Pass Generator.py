import random
import string

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase + uppercase + digits + special_characters

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    password = generate_password(length)

    print("Generated Password:", password)

if __name__ == "__main__":
    main()