import base64
from Crypto.Cipher import AES
import hashlib


# password = b"mypassword"
# key = hashlib.sha256(password).digest()
# IV = 'This is an IV456'

key = 'YELLOW SUBMARINE'
IV = '\x00' * 16

mode = AES.MODE_CBC
cipher = AES.new(key, mode, IV)

with open('encrypted', 'rb') as e:
    encrypted_file = e.read()
# with open('4.txt', 'rb') as e:
#     encrypted_file = base64.b64decode(e.read())

decrypted_file = cipher.decrypt(encrypted_file)
print(decrypted_file)
with open('decrypted', 'wb') as d:
    d.write(decrypted_file.rstrip(b'0'))
