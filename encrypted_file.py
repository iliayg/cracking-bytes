import base64
from Crypto.Cipher import AES
import hashlib


# password = "mypassword".encode()
# key = hashlib.sha256(password).digest()
# IV = 'This is an IV456'
key = 'YELLOW SUBMARINE'
IV = '\x00' * 16
mode = AES.MODE_CBC
cipher = AES.new(key, mode, IV)


def pad_message(file):
    while len(file) % 16 != 0:
        file = file + b'0'
    return file


with open("decrypted", "rb") as d:
    file = d.read()
padded_file = pad_message(file)
encrypted_file = cipher.encrypt(padded_file)
with open('encrypted', 'wb') as e:
    e.write(encrypted_file)
