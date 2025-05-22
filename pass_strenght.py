import string
import math
import re

password = "helloworld"

def calculate_entropy(pwd):
    charset = 0
    if any(c in string.ascii_lowercase for c in pwd):
        charset += 26
    if any(c in string.ascii_uppercase for c in pwd):
        charset += 26
    if any(c in string.digits for c in pwd):
        charset += 10
    if any(c in string.punctuation for c in pwd):
        charset += len(string.punctuation)
    entropy = len(pwd) * math.log2(charset) if charset else 0
    return round(entropy, 2)

def has_keyboard_patterns(pwd):
    patterns = ["qwerty", "asdf", "zxcv", "1234", "0000"]
    return any(p in pwd.lower() for p in patterns)

def has_repeated_chars(pwd):
    return bool(re.search(r"(.)\1{2,}", pwd))  # 3 or more repeating characters

def leetspeak_to_text(pwd):
    leet_dict = {'0': 'o', '1': 'i', '3': 'e', '4': 'a', '@': 'a', '$': 's', '5': 's', '7': 't'}
    return ''.join(leet_dict.get(c.lower(), c.lower()) for c in pwd)

def contains_dictionary_word(pwd, dictionary):
    lower_pwd = pwd.lower()
    for word in dictionary:
        if word in lower_pwd:
            return True
    return False

# Basic checks
upper_case = any(c in string.ascii_uppercase for c in password)
lower_case = any(c in string.ascii_lowercase for c in password)
special = any(c in string.punctuation for c in password)
digits = any(c in string.digits for c in password)
characters = [upper_case, lower_case, special, digits]

length = len(password)
score = 0

# Load common password list
try:
    with open('common.txt', 'r') as f:
        common = f.read().splitlines()
except FileNotFoundError:
    common = []

if password in common or leetspeak_to_text(password) in common:
    print("Password is in common list. Score: 0/10")
    exit()

# Length scoring
if length > 8: score += 1
if length > 12: score += 1
if length > 17: score += 1
if length > 20: score += 1

# Character type variety
score += sum(characters) - 1

# Advanced scoring
entropy = calculate_entropy(password)
if entropy > 40:
    score += 1
if not has_keyboard_patterns(password):
    score += 1
if not has_repeated_chars(password):
    score += 1
if not contains_dictionary_word(leetspeak_to_text(password), common):
    score += 1

# Output
print(f"Password length: {length}")
print(f"Entropy: {entropy} bits")
print(f"Character types used: {sum(characters)}")
print(f"Keyboard pattern detected: {has_keyboard_patterns(password)}")
print(f"Repeated characters detected: {has_repeated_chars(password)}")
print(f"Leetspeak translated: {leetspeak_to_text(password)}")
print(f"Dictionary word detected: {contains_dictionary_word(leetspeak_to_text(password), common)}")

# Final Verdict
print(f"\nFinal Score: {score} / 10")
if score < 4:
    print("🔴 Password is Very Weak!")
elif score < 6:
    print("🟠 Password is Weak!")
elif score < 8:
    print("🟡 Password is Decent.")
elif score < 10:
    print("🟢 Password is Strong.")
else:
    print("🟢💪 Password is Extremely Strong!")
