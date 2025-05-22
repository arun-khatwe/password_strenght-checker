# password_strenght-checker
This script analyzes and scores the strength of a given password based on multiple realistic criteria. It's designed with simplicity in mind while incorporating practical security checks like length, character variety, and common password list validation.
✅ Features:

    🧠 Checks against a common password list (like rockyou.txt)

    🔤 Character diversity analysis – detects use of upper/lowercase, digits, and special characters

    📏 Smart length scoring – longer passwords earn more points

    📉 Real-time feedback – classifies as Weak, OK, Pretty Good, or Strong

    🛠️ Try/except error handling for file reading and edge cases

    📃 Written in plain, readable Python – easy to extend or embed in other apps

📊 Scoring Logic:
Criteria	Points
Length > 8	+1
Length > 12	+1
Length > 17	+1
Length > 20	+1
Uses 2+ character types	+1
Uses 3+ character types	+1
Uses all 4 character types	+1

Max Score: 7
If the password is found in common.txt, it is instantly disqualified (score: 0/7).
🚀 Usage:

$ python pass_strength.py
Enter password to evaluate: MyStr0ng!Pass
Password has 4 different character types, adding 3 points!
Password is strong! Score: 6 / 7

📄 Example Output:

Password length is 13, adding 2 points!
Password has 3 different character types, adding 2 points!
The password is pretty good! Score: 5 / 7
