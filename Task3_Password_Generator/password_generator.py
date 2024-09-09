import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # a-z, A-Z
    if use_digits:
        characters += string.digits  # 0-9
    if use_symbols:
        characters += string.punctuation  # special symbols

    if not characters:
        raise ValueError("No character types selected!")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    
    length = int(input("Enter the desired password length: "))
    
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    try:
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
