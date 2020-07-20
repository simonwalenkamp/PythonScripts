# Takes a string as input to decode
# Takes a key to decode with
# Decodes strig
# Outputs decoded string
import base64

string_to_decode = input("Enter a string to decode: ")
key = input("Enter a key: ")


def decode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string


decoded_string = decode(key, string_to_decode)

print("Decoded string: " + decoded_string)
