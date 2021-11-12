import decode
import encode
from cryptography.fernet import Fernet

a = int(input(":: Welcome to Steganography ::\n"
              "1. Encode\n2. Decode\n"))

ans = ''

# key is generated
key = Fernet.generate_key()

# value of key is assigned to a variable
f = Fernet(key)

if (a == 1):

    b = input("Enter String to be encoded: ")

    arr = bytes(b, 'utf-8')

    token = f.encrypt(arr)
    output = token.decode()

    ans = token

    decr = f.decrypt(token)

    encode.main(output)

    print("Your key is: ", output)

elif (a == 2):

    c = input("Enter key: ")



    str1 = decode.main()

    if (str1 == c):
        print("Your encoded string was ->  ", f.decrypt(str1))

    else:
        print("Check your key!")


else:

    raise Exception("Enter correct input")
