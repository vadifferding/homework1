import sys
import argparse
import urllib.request

/myscript encrypt < myFile.txt > ciphered.txt

__author__ = "Virginia Differding"
__assignement__ = "homework 1: Classic Ciphers"
__description__ = "Takes input textf files from command line and encrypts or decrypts files based on user flags"
"""Program should be run on most recent version of python3""""


def main():
    if (len(sys.argv) != 2):
            print("format:classicCyphers plaintext.txt encryt/decrypt -<cipher flag> <key(if relavent)>")
            print("-a for affine , -c for caesar, -t for transpositional, -v for vigenere, -m for modded casear)
           
    else:
        filename = sys.argv[1]
        action = sys.argv[2]
        cipher = sys.argv[3]

        if cipher == "-a":
            affineCipher(inputFileName, action)
        if cipher == "-c":
            caesarCipher(filename, action)
        if cipher == "-v":
            vigenereCipher(filename, action, key)
        if cipher == "-t":
            transpositionalCipher(filename, action)                 
        if cipher == "-m":
            moddedCaesarCipher(filename, action, key)
        
        
#        caesarCipherTest(filename)
        key = "DUH"
 
#        vigenereCipherTest(filename, key)
        affineCipher(filename)



def railFenceCipher(inputFileName):

    
    


"""substitution and mono-alphabetic cipher wherein each letter in an alphabet is mapped to its numeric equivalent,"""
"""encrypted using a simple mathematical function, and converted back to a letter"""

def affineCipher(inputFileName, action):

    a = 3  #coprime number with 26
    b = 5  #number between 0 and (N-1)
    n = 26 #size of alphabet
    mi = 9 #multiplicative inverse
    newWord = ""

    #Encryption

    
    inputFile = open(inputFileName, "r")
    output = open("affineEncrypt.txt", "w+")

    if action == "encrypt":
        for line in inputFile:
            newWord = ""
            for c in line:
            
            #Encryption equation
            #E(x) = (Ax + B) % N
                if 65 > ord(c) or (97 >ord(c) > 90) or (122 < ord(c)) or ord(c) == "/n" or ord(c) == 32: #skip spaces
                    newWord = newWord + c
                    
            #Encryption of lowercase letters
                if ord(c) > 96 and ord(c) < 123 :
                    lcShift = 97
                    x = ord(c) - lcShift
                    e = ((a*x) + b) % n
                    e = e + lcShift
                    newWord = newWord + chr(e)
                    
            #Encryption of uppercase letters
                if ord(c) < 91 and ord(c) > 64:
                    ucShift = 65
                    x = ord(c) - ucShift
                    e = ((a*x) + b) % n
                    e = e + ucShift
                    newWord = newWord + chr(e)

            #write encrypted line to new file
            output.write(newWord)

        
 #       inputFile = open("affineEncrypt.txt", "r")
        output = open("decryptedAffine.txt", "w+")

        
        #multiplicative inverse and Decrypting
        #D(L) = Mi(L-B) % N

    if action == "decrypt":
        for line in inputFile:
            newWord = ""
            for c in line:
            
            #Decryption equation
            #E(x) = (Ax + B) % N
                if 65 > ord(c) or (97 >ord(c) > 90) or (122 < ord(c)) or ord(c) == "/n" or ord(c) == 32:    #skip spaces
                    newWord = newWord + c
                    
            #Decryption of lowercase letters
                if ord(c) > 96 and ord(c) < 123 :
                    lcShift = 97
                    x = ord(c) - lcShift
                    
                    d = mi*(x - b) % n
                    d = d + lcShift
                    newWord = newWord + chr(d)
                    
            #Decryption of uppercase letters
                if ord(c) < 91 and ord(c) > 64:
                    ucShift = 65
                    x = ord(c) - ucShift
                    d = mi*(x - b) % n
                    d = d + ucShift
                    newWord = newWord + chr(d)

    #write encrypted line to new file
            output.write(newWord)

        
    

    



def caesarCipher(inputFileName, action):
    
    foo = ""
    foo2 = ""
    ##A->65, Z->90

    print("casar ciper encrypt")

    #Encryption
    if action == "encrypt":
        for c in a:

            if ord(c) == 32:        #skip spaces
                foo = foo + c

        #Encryption of lowercase letters
            if ord(c) > 90:
                
                if (ord(c) + 3) > 122 and ord(c) != 32 :
                    change = (ord(c) + 3) - 26
                    foo = foo + chr(change)
                if (ord(c) + 3) < 123 and ord(c) != 32:
                    change = ord(c) + 3
                    foo = foo + chr(change)

        #Encryption of uppercase letters
            if ord(c) < 91:

                if (ord(c) + 3) > 90 and ord(c) != 32 :
                    change = (ord(c) + 3) - 26
                    foo = foo + chr(change)
                if (ord(c) + 3) < 91 and ord(c) != 32:
                    change = ord(c) + 3
                    foo = foo + chr(change)
                

       if action == "decrypt":
                  

    #Decryption
    for c in foo:

        if ord(c) == 32:
            foo2 = foo2 + c

    #Decryption of lowercase letters
        if ord(c) > 90:

            if (ord(c) - 3) > 96 and ord(c) != 32:
                change = (ord(c) - 3)
                foo2 = foo2 + chr(change)
                
            if (ord(c) - 3) < 97 and ord(c) != 32:
                change = (ord(c) - 3) + 26
                foo2 = foo2 + chr(change)

    #Decryption of uppercase letters
        if ord(c) < 91:
        
            if (ord(c) - 3) > 64 and ord(c) != 32:
                change = (ord(c) - 3) 
                foo2 = foo2 + chr(change)
                
            if (ord(c) - 3) < 65 and ord(c) != 32:
                change = (ord(c) - 3) + 26
                foo2 = foo2 + chr(change)

            
   

    print("cipher file test")

    inputFile = open(inputFileName, "r")
    output = open("output.txt", "w+")

    
    for line in inputFile:
        newline = ""
        for c in line:

            if ord(c) == 32 or c=="/n":     #skip spaces
                newline = newline + c

        #Encryption of lowercase letters";
            if ord(c) > 90:
                
                if (ord(c) + 3) > 122 and ord(c) != 32 :
                    change = (ord(c) + 3) - 26
                    newline = newline + chr(change)
                if (ord(c) + 3) < 123 and ord(c) != 32:
                    change = ord(c) + 3
                    newline = newline + chr(change)

        #Encryption of uppercase letters
            if ord(c) < 91:

                if (ord(c) + 3) > 90 and ord(c) != 32 :
                    change = (ord(c) + 3) - 26
                    newline = newline + chr(change)
                if (ord(c) + 3) < 91 and ord(c) != 32:
                    change = ord(c) + 3
                    newline = newline + chr(change)

        output.write(newline)
    

    
"""The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers,"""
"""based on the letters of a keywor"""
                  
def vigenereCipher(ifile, key, action):
    
    print("Vigenère cipher Test")
    ve = ""
    vd = ""
    k = "DUH"
    k2 = "duh"
    word1 = "CRYPTO"
    word2 = "crypto"
    word3 = "THEY DRINK THE TEA"
    word4 = "they drink the tea"


    # first get number of spaces to shift from key
    keylen = len(key)
    i = 0        

    inputFile = open(ifile, "r")
    output = open("voutput.txt", "w+")

    if action == "encrypt":
                  
        for line in inputFile:
            newline = ""
            for c in line:

                if i == keylen:
                    i = 0

                if ord(c) == 32 or c=="/n":        #skip spaces
                    newline = newline + c

                #establish shift
                if 123 > ord(key[i]) > 96:
                    shift = ord(key[i]) - 97
                    

                if 91 > ord(key[i]) > 64:
                    shift = ord(key[i]) - 65

            #Encryption of lowercase letters";
                if ord(c) > 96 and ord(c) < 123:
                   
                    if ord(c) + shift > 122 and ord(c) != 32 :
                        change = ord(c) + shift - 26
                        newline = newline + chr(change)
                        
                    if ord(c) + shift < 123 and ord(c) != 32:
                        
                        change = ord(c) + shift
                        newline = newline + chr(change)
                        
                    i = i + 1

            #Encryption of uppercase letters
                if 91 > ord(c) and ord(c) > 64:
                        
                    if ord(c) + shift > 90 and ord(c) != 32 :
                        change = ord(c) + shift - 26
                        newline = newline + chr(change)
                        
                    if ord(c) + shift < 91 and ord(c) != 32:
                        change = ord(c) + shift
                        newline = newline + chr(change)
                        
                    i = i + 1
                    
        

        #write encrypted line to new file
        output.write(newline)



    inputFile = open(ifile, "r")
    dout = open("vigenereDecrypt.txt", "w+")

    if action == "decrypt":
        for line in output:
            newline = ""
            for c in line:

                if i == keylen:
                    i = 0

                if ord(c) == 32 or c == "/n":        #skip spaces
                    newline = newline + c

                #establish shift
                if 123 > ord(key[i]) > 96:
                    shift = ord(key[i]) - 97
                    

                if 91 > ord(key[i]) > 64:
                    shift = ord(key[i]) - 65

            #Decryption of lowercase letters";
                if ord(c) > 96 and ord(c) < 123:
                   
                    if ord(c) - shift < 97 and ord(c) != 32 :
                        change = ord(c) - shift + 26
                        newline = newline + chr(change)
                        
                    if ord(c) - shift > 96 and ord(c) != 32:
                        
                        change = ord(c) - shift
                        newline = newline + chr(change)
                        
                    i = i + 1

            #Encryption of uppercase letters
                if 91 > ord(c) and ord(c) > 64:
                        
                    if ord(c) - shift < 65 and ord(c) != 32 :
                        change = ord(c) - shift + 26
                        newline = newline + chr(change)
                        
                    if ord(c) - shift > 64 and ord(c) != 32:
                        change = ord(c) - shift
                        newline = newline + chr(change)
                        
                    i = i + 1

            #write decrypted line to new file
            dout.write(newline)

        




if __name__=="__main__":
    main()
