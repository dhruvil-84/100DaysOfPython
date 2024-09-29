#------------------------------------------------------- SHORT METHOD -----------------------------------------------------------------------
from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1
    text1 = list(text)
    for i in range(len(text)):
        if text1[i] in alphabet:
            idx = alphabet.index(text1[i])
            new_idx = (idx + shift) % len(alphabet)
            text1[i] = alphabet[new_idx]
        else:
            continue
    text1 = "".join(text1)
    print(f"\nHere's the encoded result: {text1}")

print('''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88 
   
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')
iscontinue = 'yes'
while iscontinue.lower() == 'yes':
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    text = input("\nType your message:\n").strip().lower()
    shift = int(input("\nType the shift number:\n").strip())
    if shift > 0 and shift % len(alphabet) != 0:
        if direction == "encode" or direction == "decode":
            caesar(text = text, shift = shift, direction = direction)
        else:
            print("\nInvalid direction!")
    else:
        print(f"\nShift cannot be {shift}")
    iscontinue = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").strip().lower()
    clear()

#------------------------------------------------------- SHORT METHOD -----------------------------------------------------------------------

method1 = '''
# with "for i in text"

def encode(text, shift):
    count = 0
    text = list(text)
    for i in text:
        if i in alphabet:
            idx = alphabet.index(i)
            new_idx = (idx + shift) % len(alphabet)
            text[count] = alphabet[new_idx]
            count += 1
        else:
            count += 1
            continue
    text = "".join(text)
    print(f"Here's the encoded result: {text}")

def decode(text, shift):
    count = 0
    text = list(text)
    for i in text:
        if i in alphabet:
            idx = alphabet.index(i)
            new_idx = (idx - shift) % len(alphabet)
            text[count] = alphabet[new_idx]
            count += 1
        else:
            count += 1
            continue
    text = "".join(text)
    print(f"Here's the decoded result: {text}")

'''

method2 = '''
# with "for i in range(len(text))"

def encode(text, shift):
    text1 = list(text)
    for i in range(len(text)):
        # if ord(text1[i]) >= ord('a') and ord(text1[i]) <= ord('z'):
        # OR
        if text1[i] in alphabet:
            idx = alphabet.index(text1[i])
            new_idx = (idx + shift) % len(alphabet)
            text1[i] = alphabet[new_idx]
        else:
            continue
    text1 = "".join(text1)
    print(f"\nHere's the encoded result: {text1}")

def decode(text, shift):
    text1 = list(text)
    for i in range(len(text)):
        # if ord(text1[i]) >= ord('a') and ord(text1[i]) <= ord('z'):
        # OR
        if text1[i] in alphabet:
            idx = alphabet.index(text1[i])
            new_idx = (idx - shift) % len(alphabet)
            text1[i] = alphabet[new_idx]
        else:
            continue
    text1 = "".join(text1)
    print(f"\nHere's the decoded result: {text1}")

'''

short_method1_and_method2s_drivercode = '''
iscontinue = 'yes'
while iscontinue.lower() == 'yes':
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    text = input("\nType your message:\n").strip().lower()
    shift = int(input("\nType the shift number:\n").strip())
    if shift > 0 and shift % len(alphabet) != 0:
        if direction == "encode":
            encode(text = text, shift = shift)
        elif direction == "decode":
            decode(text = text, shift = shift)
        else:
            print("\nInvalid direction!")
    else:
        print(f"\nShift cannot be {shift}")
    iscontinue = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").strip().lower()
'''

#--------------------------------------------------------------------------------------------------------------------------------------------
