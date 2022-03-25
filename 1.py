import base64
from Crypto.Cipher import AES


def aes128_decrypt(block, key):
    if len(block) != 16:
        return None
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(block)

key = b'YELLOW SUBMARINE'
blocksize = 16
res = []
with open("1.txt", "r") as file:
    text = file.read()
    text = base64.b64decode(text)
    for i in range(0, len(text), blocksize):
        block = text[i:i+blocksize]
        string = str(aes128_decrypt(block, key))[2:-1]
        print(f'{str(string)}', end='')

