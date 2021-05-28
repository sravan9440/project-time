import aes1
import base64
# A 256 bit (32 byte) key
key = "This_key_for_demo_purposes_only!"
plaintext = "Text may be any length you wish, no padding is required"

# key must be bytes, so we convert it
key = key.encode('utf-8')

aes = aes1.AESModeOfOperationCTR(key)
ciphertext = aes.encrypt(plaintext)
ciphertext = str(base64.b64encode(ciphertext),'utf-8')
# show the encrypted data
print (ciphertext)
# DECRYPTION
# CRT mode decryption requires a new instance be created
aes = aes1.AESModeOfOperationCTR(key)

# decrypted data is always binary, need to decode to plaintext

ciphertext = (base64.b64decode(ciphertext))
decrypted = aes.decrypt(ciphertext).decode('utf-8')

# True
print (decrypted)
