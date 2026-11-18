# spam_rules.py
#
# Your job: write RULES that decide whether a text message is spam.
#
# A rule is an if statement YOU write. For example:
#
#     if "winner" in text:
#         return True
#
# That rule says: if the message contains the word "winner", call it spam.
#
# How to test your rules:   python check_rules.py
# How to test tricky ones:  python check_rules.py tricky


def is_spam(message):
    """Return True if the message is spam. Return False if it is not."""

    # This line makes the message all lowercase,
    # so "WINNER" and "winner" look the same to your rules.
    text = message.lower()

    # ----- STEP 8 FIXES: exceptions that say NOT spam (run before spam rules) -----
    if "free throw" in text:
        return False
    if "class chat" in text:
        return False

    # ----- STEP 3: write your first rule below this line -----
    if "winner" in text:
        return True

    # ----- add more rules above this line -----
    # Step 4 & 6 rules:
    if "claim" in text:
        return True
    if "urgent" in text:
        return True
    if "click" in text:
        return True
    if "prize" in text:
        return True
    if "free" in text:
        return True
    if "warranty" in text:
        return True
    if "account" in text:
        return True

    # If no rule above said "spam", we decide it is NOT spam.
    return False


# This part lets you test one message by hand.
# Run:  python spam_rules.py
if __name__ == "__main__":
    sample = "CONGRATULATIONS you have been selected to win a free gift card"
    print("Message:", sample)
    print("Spam?  ", is_spam(sample))
