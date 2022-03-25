
def pkcs7_padding(block, target_length):
    text = []
    diff = bytes(target_length - len(block))
    for i in block:
        text.append(i)
        if len(text) == len(block):
            if len(block) < target_length:
                text.append(str(diff)[2:-1])
    plain = [str(i) for i in text]
    plaintext = ''.join(plain)
    return plaintext

print(pkcs7_padding('YELLOW SUBMARINE', 20))

