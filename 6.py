from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def random_bytes(range):
    with open("/dev/urandom", 'rb') as f:
        return f.read(range)


def encrypt_aes_ecb(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(data)
    return ciphertext


def encrypt_aes_cbc(data, key, IV):
    cipher = AES.new(key, AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(data)
    return ciphertext


def encryption_oracle(data):
    # Append a prefix and suffix to the data
    prefix = random_bytes(len(range(5,11)))
    suffix = random_bytes(len(range(5,11)))
    data_to_encrypt = prefix + data + suffix
    # Randomly determine the mode
    mode = len(bin(int.from_bytes(random_bytes(1), 'little')))
    if (mode) > 9:
        mode = 'ECB'
        ciphertext = encrypt_aes_ecb(pad(data_to_encrypt, blocksize), key)
    else:
        mode = 'CBC'
        ciphertext = encrypt_aes_cbc(pad(data_to_encrypt, blocksize), key, IV)
    print(f'Mode to encrypt: {mode}')
    print(f'Total of bytes: {len(ciphertext)}')
    return ciphertext


def detect_encryption_mode(ciphertext):
    n=0
    c = 0
    chunks = []
    for i in range(0, len(ciphertext), blocksize):
        chunks.append(ciphertext[i:i+blocksize])
        n+=1
    for num,ch in enumerate(chunks):
        count = chunks.count(ch)
        if count > 1:
            print(num, ch)
            c += 1
    print(f'Total of chunks of {blocksize} bytes: {n}')
    if  c > 1:
        return 'ECB'
    else:
        return 'CBC'


def main():
    with open("open_text", "rb") as f:
        data = f.read()
    data = b'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg YnkK'
    print(f'{len(data)} bytes')
    encrypted_text = encryption_oracle(data)
    detected_mode = detect_encryption_mode(encrypted_text)
    print(f"Mode Detected: {detected_mode}")


if __name__ == '__main__':
    blocksize = AES.block_size
    key = random_bytes(blocksize)
    IV = random_bytes(blocksize)
    main()
