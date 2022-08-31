import codecs
import binascii
import random

inputN = input("Enter Input!\n")
inputB = int(input("Enter Base Of Input!\n"))
outputB = input("Enter Format/Base Of Output! (all to show all possible)\n")

if(outputB.lower()=="all"):
   

InputL = inputN.split()
OutputL = []

if (len(InputL)==1) :
    x = (codecs.decode(InputL[0],"hex")).decode('utf-8')
    print("ASCII Representation For",InputL[0],"is : ","\033[1;93m",x,"\033[ ")
    quit()

#Convert to Decimal
for i in InputL :
    dec = int(i, inputB)
    OutputL.append(str(dec))

fOutput=[]
#To ASCII
if (outputB.lower() == "ascii") :
    for i in OutputL :
        x= chr(int(i))
        fOutput.append(x)
    print("ASCII Representation For",''.join(InputL),"is : ",fOutput," As ",''.join(fOutput))

#To Dec
elif (int(outputB)==10) :
    print("Decimal Representation For",''.join(InputL),"is : ",OutputL," As ",' '.join(OutputL))
#TO BIN
elif (int(outputB)==2) :
    for i in OutputL :
        x = bin(int(i))
        fOutput.append(str(x))
    print("Binary Representation For",''.join(InputL),"is : ",fOutput," As ",' '.join(fOutput).replace('0b',''))
#TO HEX
elif (int(outputB)==16) :
    for i in OutputL :
        x = hex(int(i))
        fOutput.append(str(x))
    print("Hex Representation For",''.join(InputL),"is : ",fOutput," As ",' '.join(fOutput).replace('0x',''))
#TO OCT
elif (int(outputB)==8) :
    for i in OutputL :
        x = oct(int(i))
        fOutput.append(str(x))
    print("Octal Representation For",''.join(InputL),"is : ",fOutput," As ",' '.join(fOutput).replace('0o',''))    

