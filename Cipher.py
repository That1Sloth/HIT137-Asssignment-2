dct = {}

def lettershift(letter, shift1, shift2, offset):
    if letter.isupper() == True:
        if 'A' <= letter <= 'N':
            amount = shift1
            return chr((ord(letter) - 65 - (shift1)) % 26 + 65).upper()
        else:
            return chr((ord(letter) - 65 + (shift2**2)) % 26 + 65).upper()
    elif letter.islower():
        if ('a' <= letter <= 'n'):
            return chr((ord(letter) - 97 + (shift1*shift2)) % 26 + 97)
        else:
            return chr((ord(letter) - 97 - (shift1+shift2)) % 26 + 97)

def decrypter(letter, shift1, shift2, dct):
    pass

def numbershift(number, shift1, shift2, offset):
    return chr((ord(number) - 48 + (shift1-shift2)*offset) % 10 + 48)

with open("raw_text.txt", "r", encoding="utf-8") as text:
    raw_text = text.read()

encrypted = ""
decrypted = ""
offset = 1

shift1 = int(input("Enter First Shift Amount: "))
shift2 = int(input("Enter Second Shift Amount: "))

for letter in raw_text:
    if letter.isalpha() == True:
        encrypted += str(lettershift(letter, shift1, shift2, offset))
        
    elif letter.isdigit() == True:
        encrypted += str(numbershift(letter, shift1, shift2, offset))
    else:
        encrypted += str(letter)

print(encrypted)

with open("encrypted_text.txt", "w", encoding="utf-8") as text:
    encrypted_file = text.write(encrypted)

offset = -1

for letter in encrypted:
    if letter.isalpha() == True:
        decrypted += str(lettershift(letter, shift1, shift2, offset))
    elif letter.isdigit() == True:
        decrypted += str(numbershift(letter, shift1, shift2, offset))
    else:
        decrypted += str(letter)

print(decrypted)

with open("decrypted_text.txt", "w", encoding="utf-8") as text:
    decrypted_file = text.write(decrypted)

if decrypted == raw_text:
    print("Decryption Successful")
else:
    print("Unsuccessful, try again")