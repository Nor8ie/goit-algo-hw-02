from collections import deque


def is_palindrome(user_input):

    d = deque(user_input)

    while len(d) > 1:
        # Checking if characters removed from both ends are different; if yes -> not a palidrome, if matching the loop finishes
        if d.popleft() != d.pop():
            print("The string is NOT a palindrome.\n")
            return
    print("The string is a PALINDROME.\n")


# Initializing an infinte loop to allow user to check multiple strings in one session
while True:
    print("If you wish to exit, please type close.\n")
    user_input = input("Please provide input to verify if a palindrome: ")
    user_input = user_input.lower().replace(" ", "")
    if user_input == "close":
        break
    is_palindrome(user_input)
