# defining the encryption
def encrypt_1(word):
    dict1 = {'a': '£', 'b': '*', 'c': '%', 'd': '&', 'e': '>', 'f': '<', 'g': '!', 'h': ')', 'i': '\"', 'j': '(',
             'k': '@', 'l': 'a', 'm': 'b', 'n': 'c', 'o': 'd', 'p': 'e', 'q': 'f', 'r': 'g', 's': 'h', 't': 'i',
             'u': 'j', 'v': 'k', 'w': 'l', 'x': 'm', 'y': 'n', 'z': 'o'
             }
    result = ""
    for li in word:
        result += dict1[li]
    return result


# defining the decryption
def decrypt_2(words):
    dict2 = {'£': 'a', '*': 'b', '%': 'c', '&': 'd', '>': 'e', '<': 'f', '!': 'g', ')': 'h', '\"': 'i', '(': 'j',
             '@': 'k', 'a': 'l', 'b': 'm', 'c': 'n', 'd': 'o', 'e': 'p', 'f': 'q', 'g': 'r', 'h': 's', 'i': 't',
             'j': 'u', 'k': 'v', 'l': 'w', 'm': 'x', 'n': 'y', 'o': 'z'
             }
    result2 = ""
    for li_1 in words:
        result2 += dict2[li_1]
    return result2


ques = input("Are you trying to encrypt or decrypt? > ")
here = input("Enter word >  ")

if ques.upper() == "ENCRYPT":
    print(encrypt_1(here))

elif ques.upper() == "DECRYPT":
    print(decrypt_2(here))

else:
    print("Enter either encrypt or decrypt")
