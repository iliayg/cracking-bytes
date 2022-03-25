import base64
from Crypto.Cipher import AES


blocksize = 16
key = b'YELLOW SUBMARINE'
IV = b'\x00' * blocksize


def aes128_decrypt(block, key, IV):
    if len(block) != 16:
        block = pad_message(block)
    cipher = AES.new(key, AES.MODE_CBC, IV)
    return cipher.decrypt(block)


def pad_message(block):
    while len(block) % 16 != 0:
        block = block + " "
    return block


# with open("4.txt", "rb") as e:
#     encrypted_text = base64.b64decode(e.read())
with open("encrypted", "rb") as e:
    encrypted_text = e.read()

with open('decrypted', 'w') as d:
    for i in range(0, len(encrypted_text), blocksize):
        block = encrypted_text[i:i+blocksize]
        decrypted_block = str(aes128_decrypt(block, key, IV))[2:-1]
        IV = block
        print(f'{str(decrypted_block)[2:-1]}')
        d.write(decrypted_block)
