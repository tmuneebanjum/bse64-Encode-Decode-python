#choice decoding and encoding base64

import base64

choice = input("1. Encode \n2. Decode \nEnter Your Choice = ")
#Encode
if (choice == '1'):
    message = input("Enter string to Encode : " )
    encode = message.encode('ascii')
    message_encode = base64.b64encode(encode)
    print(message_encode)

#decode

elif (choice == '2'):
    message = input("Enter string to Decode : " )
    message_decode = base64.b64decode(message)
    decode = message_decode.decode('ascii')
    print(decode)

else:
    print("PLease Chosse correct option")