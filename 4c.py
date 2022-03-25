import base64
from Crypto.Cipher import AES


blocksize = 16
key = b'YELLOW SUBMARINE'
IV = b'\x00' * blocksize


def aes128_encrypt(block, key, IV):
    if len(block) != 16:
        block = pad(block)
    cipher = AES.new(key, AES.MODE_CBC, IV)
    return cipher.encrypt(block)


def pad(block):
    while len(block) % 16 != 0:
        block = block + ' '
    return block


with open('decrypted', 'r') as d:
    decrypted_text = (d.read())
n = 0
with open('encrypted', 'wb') as e:
    for i in range(0, len(decrypted_text), blocksize):
        block = decrypted_text[i:i+blocksize]
        encrypted_block = (aes128_encrypt(block, key, IV))
        IV = block
        e.write(encrypted_block)
