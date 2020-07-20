# Takes a string as input to encode
# Takes a key to encode with
# Encodes strig
# Outputs encoded string
import base64

string_to_encode = input("Enter a string to encode: ")
key = input("Enter a key: ")


def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string


encoded_string = encode(key, string_to_encode)

print("Encoded string: " + encoded_string)
