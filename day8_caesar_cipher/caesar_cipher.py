def caesar(msg, direction, shift):
    global alphabet
    result = ''
    if direction == 'encode':
        for i in msg:
            result += (chr(((ord(i)+shift-65) % 26)+65))
        return result
    elif direction == 'decode':
        return "Not implemented yet"
    else:
        return "Invalid direction"

alphabet = [chr(x) for x in range(65, 91)]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").upper()
shift = int(input("Type the shift number:\n"))

print(caesar(text, direction, shift))



