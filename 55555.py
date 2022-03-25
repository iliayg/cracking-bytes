import string
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def random_bytes(range):
    with open("/dev/urandom", 'rb') as f:
        return f.read(range)


def encrypt_aes_ecb(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(data)
    return ciphertext


def encryption_oracle(data):
    ciphertext = encrypt_aes_ecb(pad(data, blocksize), key)
    return ciphertext


def main():
    char = 'A'
    blocks = []
    goodchars = ''
    char_crack = ''
    data = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

    for b in range(0, len(data), blocksize):
        datablock = data[b:b+blocksize]
        for i in range(1, blocksize+1):
            length = blocksize-i
            crack = char*length
            char_crack = encryption_oracle(crack.encode('ascii') + datablock)
            crack += goodchars
            blocks.append(char_crack[:blocksize])
            for j in range(0, len(string.printable)):
                chars = string.printable[j]
                iter_crack = (crack + chars).encode('ascii')
                decoded_crack = encryption_oracle(iter_crack + datablock)
                for k in range(0, len(string.printable)):
                    block = decoded_crack[k:blocksize]
                    if block in blocks:
                        goodchars += chars
            blocks.clear()
        print(goodchars, end='')
        goodchars = ''


if __name__ == '__main__':
    blocksize = AES.block_size
    key = random_bytes(blocksize)
    main()
