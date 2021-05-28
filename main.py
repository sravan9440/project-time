from datetime import datetime
import aes1
import des1
import idea
import io
import base64
import get_key
c=4
while(c!=0):
    print("choose the following options \n 1: encryption \n 2: decryption \n 0: to exit")
    c=int(input(""))
    if(c==1):

        now = datetime.now()
        h = int(now.strftime("%H"))
        m = int(now.strftime("%M"))
        fliename="{}{}.txt"
        #if hour is even des will work
        if((5*h**3+m**2)%3==0):
            key = get_key.key_gen(h,m)
            key=key[:8]
            print("DES IS WORKING NOW so enter the plain text in 8 times:\n")
            text = input("enter your secret message: ")
            d = des1.des()
            r = (d.encrypt(key, text))
            with io.open(fliename.format(h, m), "a", encoding="utf-8") as f:
                f.write(r)
                f.close()
            print("Ciphered: ",r)
        #if hour is odd aes will work
        elif((5*h**3+m**2)%3==1):
            key = get_key.key_gen(h,m)
            key=key[:32]
            print("AES IS WORKING NOW plain text can be like anything:\n")
            plaintext =input("enter your secret message: ")
            key = key.encode('utf-8')
            aes = aes1.AESModeOfOperationCTR(key)
            ciphertext = aes.encrypt(plaintext)
            ciphertext = str(base64.b64encode(ciphertext), 'utf-8')
            f=open(fliename.format(h, m),"w")
            f.write(ciphertext)
            f.close()
            print(ciphertext)
        #here idea will work
        elif((5*h**3+m**2)%3==2):
            # key size is 128 bits
            key=get_key.key_gen(h,m)
            a=key[:16]
            nchars = len(a)
            key = sum(ord(a[byte]) << 8 * (nchars - byte - 1) for byte in range(nchars))
            print("IDEA IS WORKING enter the plaint text in 8 multiples:\n")
            plain = input("enter your secret message: ")
            foridea=plain
            nchars = len(plain)
            plain = sum(ord(plain[byte]) << 8 * (nchars - byte - 1) for byte in range(nchars))
            my_IDEA = idea.IDEA(key)
            encrypted = my_IDEA.encrypt(plain)
            nchars = len(str(encrypted))
            encrypted = ''.join(chr((encrypted >> 8 * (nchars - byte - 1)) & 0xFF) for byte in range(nchars))
            with io.open(fliename.format(h, m), "a", encoding="utf-8") as f:
                f.write(encrypted)
                f.close()
            print((encrypted))
    elif(c==2):
        flie=input("enter your flie name : ")
        h = int(flie[:-6])
        m = int(flie[2:-4])
        if((5*h**3+m**2)%3==0):
            d = des1.des()
            key = get_key.key_gen(h, m)
            with io.open(flie, "r", encoding="utf-8") as f:
                x=f.read()
            r2 = d.decrypt(key,x)
            print("Deciphered: ", r2)
        elif((5*h**3+m**2)%3==1):
            key = get_key.key_gen(h, m)
            key=key[:32]
            key = key.encode('utf-8')
            aes = aes1.AESModeOfOperationCTR(key)
            with io.open(flie, "r", encoding="utf-8") as f:
                x=f.read()
            x = (base64.b64decode(x))
            decrypted = aes.decrypt(x).decode('utf-8')
            print(decrypted)
        elif((5*h**3+m**2)%3==2):
            key = get_key.key_gen(h, m)
            a = key[:16]
            nchars = len(a)
            key = sum(ord(a[byte]) << 8 * (nchars - byte - 1) for byte in range(nchars))
            # plain text size is 64bits
            with io.open(flie, "r", encoding="utf-8") as f:
                x=f.read()
            plain = x
            nchars = len(plain)
            plain = sum(ord(plain[byte]) << 8 * (nchars - byte - 1) for byte in range(nchars))
            my_IDEA = idea.IDEA(key)
            encrypted = my_IDEA.encrypt(plain)
            nchars = len(str(encrypted))
            encrypted = ''.join(chr((encrypted >> 8 * (nchars - byte - 1)) & 0xFF) for byte in range(nchars))
            print("your original message ",foridea)