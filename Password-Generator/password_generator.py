import random
import string

def generate_password(length, use_numbers, use_symbols):
    characters = string.ascii_letters  # a-z A-Z

    if use_numbers:
        characters += string.digits  # 0-9

    if use_symbols:
        characters += string.punctuation  # !@#$...

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be positive.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    numbers = input("Include numbers? (y/n): ").lower() == "y"
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, numbers, symbols)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
