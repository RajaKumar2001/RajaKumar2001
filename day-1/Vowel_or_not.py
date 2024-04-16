def check_vowel(ch):
    if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
        print(f"{ch} is a vowel.")
    else:
        print(f"{ch} is not a vowel.")

# Example usage:
character = input("Enter a character: ")
check_vowel(character)
