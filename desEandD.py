import des1
key = "secret_k"
text= "lebgokulakegfyuf"
d = des1.des()
r = d.encrypt(key,text)
r2 = d.decrypt(key,r)
print("Ciphered: %r" %r)
print("Deciphered: ", r2)