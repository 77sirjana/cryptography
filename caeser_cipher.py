# ceaser cipher
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# DEFINE A FUNCTION that checks if input message contains alphabets only
def contains_only_alphabets(input_str):
    for char in input_str:
        if not char.isalpha():
            return False
    return True

#input plaintext containing only alphabets
while True:
    try:
        msg=input("Input message")

        #checking if input string contains alphabaets only:
        if contains_only_alphabets(msg):
            break
        else:
            print("Input message does not contains aLPhabets only!!")
    except ValueError:
        print("Input is not alphabetic.Try again!!")
  #input a positive integer (between 1 to 26) as key(shift)  
while True:
    try:
        key= int(input("enter a number between 1 and 26"))
        if 1<= key <=26:
            break #Exit he loop if the input is valid
        else:
            print("Input is not between 1 and 26.Try again.")
    except ValueError:
        print("Input is not an integer.Try again.")  

def caeser_encryption(text,shift):
    encrypted_text=''
#changing text to upper case
    text=text.upper()
    n=len(text)
    #encrypt text
    for i in range(n):
        c=text[i]
        loc=alpha.find(c)
        newloc=(loc+shift)%26
        encrypted_text += alpha[newloc]
    return encrypted_text    
                                  
def caeser_decryption(encrypted_text,shift):
    decrypted_text=''
#length of encrypted text
    n=len(encrypted_text)

    #decrypt text
    for i in range(n):
        c=encrypted_text[i]
        loc=alpha.find(c)
        newloc=(loc+shift)%26
        decrypted_text += alpha[newloc]
    return decrypted_text  

cipheretxt= caeser_encryption(msg,key)
decrypted_text= caeser_decryption(cipheretxt,key)
print("plaintext",msg)
print("shift key:",key)
print("ciphertext:",cipheretxt)
print ("Decrypted text:",decrypted_text)  
       
    
