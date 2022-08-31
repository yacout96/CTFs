import codecs
import binascii
import random

inputN = input("Enter Input!\n")
inputB = input("Enter Base Of Input! ('all' to show all possible)\n")
outputB = input("Enter Format/Base Of Output! ('all' to show all possible)\n")

def ToASCII(OutputL,fOutput):
    fOutput.clear()
    for i in OutputL :
        x= chr(int(i))
        fOutput.append(x)
    print("ASCII Representation For",''.join(InputL),"is : ",fOutput," As ",''.join(fOutput))

def ToDec(OutputL,fOutput):
        print("Decimal Representation For",''.join(InputL),"is : ",OutputL," As ",' '.join(OutputL))

def ToBin(OutputL,fOutput):
    for i in OutputL :
        x = bin(int(i))
        fOutput.append(str(x))
    print("Binary Representation For",''.join(InputL),"is : ",fOutput," As ",' '.join(fOutput).replace('0b',''))

def ToHex(OutputL,fOutput):
    for i in OutputL :
        x = hex(int(i))
        fOutput.append(str(x))
    print("Hex Representation For",''.join(InputL),"is : ",fOutput," As ",' '.join(fOutput).replace('0x',''))

def ToOct(OutputL,fOutput):
    for i in OutputL :
        x = oct(int(i))
        fOutput.append(str(x))
    print("Octal Representation For",''.join(InputL),"is : ",fOutput," As ",' '.join(fOutput).replace('0o',''))    

InputL = inputN.split()
OutputL = []

if (len(InputL)==1) :
    x = (codecs.decode(InputL[0],"hex")).decode('utf-8')
    print("ASCII Representation For",InputL[0],"is : ","\033[1;93m",x,"\033[ ")
    quit()

fOutput=[]

if(inputB.lower()=="all"):
    for i in range(2,37) :
        print("Converting from", i)
        OutputT = []
        sOutput = []
        for j in InputL :
            try :
                dec0 = int(j, i)
                OutputT.append(str(dec0))
            except Exception :
                print("Base ",i, "Failed")
        ToASCII(OutputT,sOutput)
    quit()

#Convert to Decimal
for i in InputL :
    dec = int(i, int(inputB))
    OutputL.append(str(dec))

#To ASCII
if (outputB.lower() == "ascii") :
    ToASCII(OutputL,fOutput)

#To Dec
elif (int(outputB)==10) :
    ToDec(OutputL,fOutput)
#TO BIN
elif (int(outputB)==2) :
    ToBin(OutputL,fOutput)
    
#TO HEX
elif (int(outputB)==16) :
    ToHex(OutputL,fOutput)
#TO OCT
elif (int(outputB)==8) :
    ToOct(OutputL,fOutput)
