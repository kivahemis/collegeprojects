def encode(mess, key):
    encoded = ''
    for i in range(len(mess)):
        a = ord(mess[i])
        b = key
        if (a > 122 - b):
            encoded += chr(a + b - 26)
        if mess[i] == (' '):
            encoded += (' ')
        else:
           encoded += chr(a + b)
    print("Encoded message is: ",encoded)

mess = input("Enter mess: ")
key = int(input("enter key: "))
encode(mess, key)

def decoded(mess, key):
    decoded = ''
    for i in range(len(mess)):
          a = ord(mess[i])
          b = key
          if((a - b) < 33):
              decoded += chr((a - b) + 64)
          if mess[i] == (' '):
              decoded += (' ')
          else:
              decoded += chr(a - b)
    print("deszyfr: ", decoded)

mess = input("Enter message to decode: ")
key = int(input("Enter key: "))
decoded(mess, key)


#Szyfr cezara. Do udoskonalenia