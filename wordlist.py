import itertools
import pyfiglet
from termcolor import colored

def banner():
    print(colored(pyfiglet.figlet_format("73j45-Wordlists"), "cyan"))
    print(colored("[+] Created by 73j45 - A Personalized Wordlist Generator [+]", "yellow"))
    print(colored("============================================================", "red"))
    print(colored("|      Custom Wordlist Creator for Password Cracking       |", "magenta"))
    print(colored("|            Generate Smart & Strong Passwords             |", "magenta"))
    print(colored("============================================================", "red"))

def substitute_special_chars(word):
    substitutions = {
        'a': ['@', '4'],
        'A': ['@', '4'],
        's': ['$', '5'],
        'S': ['$', '5'],
        'i': ['!', '1'],
        'I': ['!', '1'],
        'o': ['0'],
        'O': ['0'],
        'e': ['3'],
        'E': ['3'],
        't': ['7'],
        'T': ['7']
    }
    
    word_variations = set([word])
    word_chars = list(word)
    
    for i, char in enumerate(word_chars):
        if char in substitutions:
            for sub in substitutions[char]:
                temp_word = word_chars[:]
                temp_word[i] = sub
                word_variations.add("".join(temp_word))
    
    return word_variations

def generate_passwords(name, dob, city, pet, special_chars="!@#$%", max_length=12):
    words = [name, dob, city, pet]
    variations = set()
    
    for word in words:
        if word:
            basic_variations = {word, word.lower(), word.upper(), word.capitalize()}
            for variation in basic_variations:
                variations.update(substitute_special_chars(variation))
                variations.update([variation + str(i) for i in range(10)])  # Add small numbers for variations
                for i in range(0, len(dob), 2):
                    variations.add(variation + dob[i:])  # Add part of DOB to name
                for char in special_chars:
                    variations.add(variation + char + dob[-2:])  # Creative combinations
    
    meaningful_combinations = set()
    for a, b in itertools.combinations(variations, 2):
        meaningful_combinations.add(a + b)
        meaningful_combinations.add(b + a)
    
    with_specials = set()
    for pwd in meaningful_combinations:
        for char in special_chars:
            with_specials.add(pwd + char)
            with_specials.add(char + pwd)
    
    final_wordlist = [pwd for pwd in (variations | meaningful_combinations | with_specials) if len(pwd) <= max_length]
    
    return final_wordlist

def save_wordlist(wordlist, filename):
    with open(filename, "w") as f:
        for password in wordlist:
            f.write(password + "\n")
    print(colored(f"[+] Wordlist saved as {filename}", "green"))

def main():
    banner()
    
    print(colored("Enter the details to generate a personalized wordlist:", "yellow"))
    name = input(colored("[?] Enter target's name: ", "cyan")).strip()
    dob = input(colored("[?] Enter date of birth (e.g., 1995, 01011995): ", "cyan")).strip()
    city = input(colored("[?] Enter favorite city: ", "cyan")).strip()
    pet = input(colored("[?] Enter favorite pet/animal: ", "cyan")).strip()
    max_length = input(colored("[?] Enter max password length (default 12): ", "cyan")).strip()
    max_length = int(max_length) if max_length else 12
    output_file = input(colored("[?] Enter output file name (default: custom_wordlist.txt): ", "cyan")).strip()
    output_file = output_file if output_file else "custom_wordlist.txt"
    
    wordlist = generate_passwords(name, dob, city, pet, max_length=max_length)
    save_wordlist(wordlist, output_file)
    
    print(colored("[+] Wordlist generation complete!", "green"))
    print(colored(f"[+] Saved to: {output_file}", "yellow"))

if __name__ == "__main__":
    main()
