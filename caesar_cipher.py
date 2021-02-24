import string
import re

field = string.ascii_uppercase


def encrypt():
    try:
        text = input("Enter plain-text to encrypt: ")
        text = text.upper().replace(" ", "")
        key = int(input("Enter key [0-25]: "))
        if key > 25 or key < 0:
            print("invalid key")
        else:
            encrypted = ""
            for i in text:
                if i in text:
                    index = (field.find(i) + key) % len(field)
                    encrypted = encrypted + field[index]

            print()
            print("Plain text:\n" + text)
            print("Encrypted text:\n" + encrypted)
            print("Key used:\n" + str(key))
            print()

    except ValueError:
        print("invalid entry")


def decrypt():
    try:
        text = input("Enter encrypted-text to decrypt: ")
        text = text.upper()
        key = int(input("Enter key [0-25]: "))
        if key > 25 or key < 0:
            print("invalid key")
        else:
            decrypted = ""
            for i in text:
                if i in text:
                    index = (field.find(i) - key) % 26
                    decrypted = decrypted + field[index]
            print()
            print("Encrypted text:\n" + text)
            print("Plain text:\n" + decrypted)
            print("Key used:\n" + str(key))
            print()

    except ValueError:
        print("invalid entry")


def crack():
    try:
        text = input("Enter encrypted text to crack: ")
        text = text.upper()

        for ind, char in enumerate(field):
            print("Attempt with key " + str(ind) + ": ", end="")
            for i in text:
                cracked = ""
                if i in text:
                    index = (field.find(i) - ind) % 26
                    cracked = cracked + field[index]
                    print(cracked, end="")
            print()

    except ValueError:
        print("invalid entry")


print("---------------------------- Caesar Cipher -----------------------------")
print("Author: Mohammad Sulayman Rezaie                             Python 3.8.5")
print("Description:\nThis is a tool for encrypting and decrypting plain text and encrypted\n"
      "text of only alphabetical letters from A-Z using keys 0-25.")
print()
print("1: Encrypt")
print("2: Decrypt")
print("3: Crack")
print("0: Exit")
print("\n")

condition = True
while condition:
    response = input("Enter choice: ")
    if not re.match("[0-3]", response):
        print("invalid choice")
    elif response == '1':
        encrypt()
    elif response == '2':
        decrypt()
    elif response == '3':
        crack()
    elif response == '0':
        condition = False
