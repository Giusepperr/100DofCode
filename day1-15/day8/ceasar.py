def deOrencrypt(choice,msg, shiftV):
    msgList = list(msg)
    index = 0
    for letter in msgList:
        if(choice == 'encrypt'):
            msgList[index] = chr(ord(msgList[index])+shiftV)
        if(choice == 'decrypt'):
            msgList[index] = chr(ord(msgList[index])-shiftV)
        index+=1
    encryptedMsg = "".join(msgList)
    print(encryptedMsg)
def decrypt(msg, shift):
    encryptedMsg = msg
    print(encryptedMsg)
while True:
    choice = input('Do you want to encrypt or decrypt a message?')
    msg = input('What is your message?')
    shift = int(input('How much shift you want to insert?'))
    deOrencrypt(choice,msg,shift)