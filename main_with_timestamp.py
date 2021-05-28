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
        timestamp = datetime.timestamp(now)
        timestamp = int(timestamp * (10 ** 6))
        s16 = str(timestamp)
        odd8 = []
        even8 = []
        for i in range(0, 16):
            if (i % 2 == 0):
                even8.append(int(s16[i]))
            elif (i % 2 == 1):
                odd8.append(int(s16[i]))
        aa=even8[7]+even8[2]+even8[3]+odd8[0]
        bb=even8[0]+odd8[7]+even8[2]+odd8[5]
        cc=odd8[6]+odd8[5]
        dd=even8[5]+even8[7]
        fliename="{}.txt"
        #if hour is even des will work
        if((7*aa**2+11*bb**3+5*cc**5+6*dd)%3==0):
            key = get_key.key_gen(even8[7],odd8[7])
            key=key[:8]
            print("DES IS WORKING NOW:\n")
            text = input("enter your secret message: ")
            d = des1.des()
            r = (d.encrypt(key, text))
            with io.open(fliename.format(timestamp), "a", encoding="utf-8") as f:
                f.write(r)
                f.close()
            print("Ciphered: ",r)
        #if hour is odd aes will work
        elif((7*aa**2+11*bb**3+5*cc**5+6*dd)%3==1):
            key = get_key.key_gen(even8[7],odd8[7])
            key=key[:32]
            print("AES IS WORKING NOW:\n")
            plaintext =input("enter your secret message: ")
            key = key.encode('utf-8')
            aes = aes1.AESModeOfOperationCTR(key)
            ciphertext = aes.encrypt(plaintext)
            ciphertext = str(base64.b64encode(ciphertext), 'utf-8')
            f=open(fliename.format(timestamp),"w")
            f.write(ciphertext)
            f.close()
            print(ciphertext)
        #here idea will work
        elif((7*aa**2+11*bb**3+5*cc**5+6*dd)%3==2):
            # key size is 128 bits
            key=get_key.key_gen(even8[7],odd8[7])
            a=key[:16]
            nchars = len(a)
            key = sum(ord(a[byte]) << 8 * (nchars - byte - 1) for byte in range(nchars))
            print("IDEA IS WORKING:\n")
            plain = input("enter your secret message: ")
            foridea=plain
            nchars = len(plain)
            plain = sum(ord(plain[byte]) << 8 * (nchars - byte - 1) for byte in range(nchars))
            my_IDEA = idea.IDEA(key)
            encrypted = my_IDEA.encrypt(plain)
            nchars = len(str(encrypted))
            encrypted = ''.join(chr((encrypted >> 8 * (nchars - byte - 1)) & 0xFF) for byte in range(nchars))
            with io.open(fliename.format(timestamp), "a", encoding="utf-8") as f:
                f.write(encrypted)
                f.close()
            print((encrypted))
    elif(c==2):
        flie=input("enter your flie name : ")
        timestamp = flie[:-4]
        s16 = str(timestamp)
        jx=0
        ix=0
        for i in range(0, 16):
            if (i % 2 == 0):
                even8[jx]=(int(s16[i]))
                jx=jx+1
            elif (i % 2 == 1):
                odd8[ix]=(int(s16[i]))
                ix=ix+1
        aa = even8[7] + even8[2] + even8[3] + odd8[0]
        bb = even8[0] + odd8[7] + even8[2] + odd8[5]
        cc = odd8[6] + odd8[5]
        dd = even8[5] + even8[7]
        if((7*aa**2+11*bb**3+5*cc**5+6*dd)%3==0):
            d = des1.des()
            key = get_key.key_gen(even8[7],odd8[7])
            with io.open(flie, "r", encoding="utf-8") as f:
                x=f.read()
            r2 = d.decrypt(key,x)
            print("Deciphered: ", r2)
        elif((7*aa**2+11*bb**3+5*cc**5+6*dd)%3==1):
            key = get_key.key_gen(even8[7],odd8[7])
            key=key[:32]
            key = key.encode('utf-8')
            aes = aes1.AESModeOfOperationCTR(key)
            with io.open(flie, "r", encoding="utf-8") as f:
                x=f.read()
            x = (base64.b64decode(x))
            decrypted = aes.decrypt(x).decode('utf-8')
            print(decrypted)
        elif(((7*aa**2+11*bb**3+5*cc**5+6*dd)%3==2)):
            key = get_key.key_gen(even8[7],odd8[7])
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