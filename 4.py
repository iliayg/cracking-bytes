import base64
from Crypto.Cipher import AES

# def binary_xor(buf1, buf2):
#     bin1 = bin(int(buf1, 16))[2:]
#     bin2 = bin(int(buf2, 16))[2:]

#     optimal_length = len(bin1) if len(bin2) > len(bin2) else len(bin2)
#     bin1 = bin1.zfill(optimal_length)
#     bin2 = bin2.zfill(optimal_length)

#     result = [int(x) ^ int(y) for x,y in zip(bin1, bin2)]
#     result = "".join([str(i) for i in result])
#     result = hex(int(result, 2))[2:]
#     print(result

def binary_digits(cipher1, cipher2):
    buffer1 = bytes(cipher1)
    buffer2 = bytes(cipher2)
    result = [x ^ y for x,y in zip(buffer1, buffer2)]
    result = bytes(result)
    print(result)


def aes128_decrypt(block, key):
    if len(block) != 16:
        return None
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(block)

key = (b'YELLOW SUBMARINE')
# key2 = (b'\xcc\xd31\x95\x0f\xad\x7f\xb2C\x0e\xf7\xe3u\xbf\xe8\xc3')
# key2 = (b"\t\x120\xaa\xde>\xb30\xdb\xaaCX\xf8\x8d*l")
IV = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
blocksize = 16
res = []
with open("4.txt", "r") as file:
    text = file.read()
    text = base64.b64decode(text)
    for i in range(0, len(text), blocksize):
        block = text[i:i+blocksize]
        # block = b'\xcc\xd31\x95\x0f\xad\x7f\xb2C\x0e\xf7\xe3u\xbf\xe8\xc3'
        key2 = b"D\xb8\\OMq\xa3|~\x92\xbe\xc4\x87\x0e\xcf\x00"
        block = str(aes128_decrypt(block, key))[2:-1]
        print(f'{str(block)}')


# binary_digits(key, key2)
