#PicoCTF 2021 - Transformation


#Encoded
# flag = "picoCTF{"
# enc = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
# print(enc)

#Encoded Simplified
# flag2 = "picoCTF{"
# app=[]
# for i in range(0, len(flag2), 2) :
#     print("character : ",flag2[i])
#     a1=(ord(flag2[i]) << 8)
#     print("a1 : ",a1)
#     a2=ord(flag2[i + 1])
#     print("a2 : ",a2)
#     a=a1+a2
#     print("a : ",a)
#     enc=chr(a)
#     print("enc : ",enc)
#     app.append(enc)
#     print("app : ",app)
# flag= ''.join(app)
# print(flag)

#Decoded
flag="灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"
for i in range(0, len(flag), 1) :
    a= ord(flag[i])
    ba=bin(a)
    fba=int(ba,2) >> 8
    sba=int(ba[9:],2)
    print(chr(fba)+chr(sba), end='')
