# check_rules.py
#
# This program tests YOUR rules in spam_rules.py.
# You do not need to change this file.
#
# Run:  python check_rules.py          (tests messages.csv)
# Run:  python check_rules.py tricky   (tests tricky_messages.csv)

import csv
import sys

from spam_rules import is_spam

file_name = "tricky_messages.csv" if "tricky" in sys.argv else "messages.csv"

with open(file_name, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

right = 0
missed_spam = []    # spam your rules let through
false_alarm = []    # normal texts your rules called spam

for row in rows:
    guess = is_spam(row["message"])
    actually_spam = row["label"] == "spam"
    if guess == actually_spam:
        right += 1
    elif actually_spam:
        missed_spam.append(row["message"])
    else:
        false_alarm.append(row["message"])

print(f"Testing your rules on {file_name}")
print(f"Right: {right} out of {len(rows)}")
print()
print(f"MISSED SPAM ({len(missed_spam)}): spam your rules let through")
for m in missed_spam:
    print("   ", m)
print()
print(f"FALSE ALARMS ({len(false_alarm)}): normal texts your rules called spam")
for m in false_alarm:
    print("   ", m)
