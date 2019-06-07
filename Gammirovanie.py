import random

def str2bits(s):
    x = bin(int.from_bytes(s.encode(), byteorder = 'big'))[2:]
    while len(x) % 8 != 0:
        x = '0' + x
    return x

def generationkey(mes):
    bin_key = '{0:b}'.format(random.getrandbits(mes))
    with open('Key.txt', 'w') as f:
        f.write(bin_key)
    return bin_key

def xormes(mes, key):
    afterxor = []
    for i, j in zip(mes, key):
        temp = bin(int(i, 2) ^ int(j, 2))[2:]
        afterxor.append(temp)
    return ''.join(afterxor)

def bits2str(b):
    bits = []
    for i,value in enumerate([b[i : i + 8] for i in range(0, len(b), 8)]):
        bits.append(chr(int(value, 2)))
    return ''.join(bits)

def bits2hex(b):
    return hex(int(b, 2))[2:]

def output(encrmes):
    print('''Represent the encrypted message in :
    0 - binary code;
    1 - in symbolic form;
    2 - in hexadecimal code''')
    fl = 0
    while fl != 1:
        try:
            mode = int(input())
            if mode == 0:
                encmes = encrmes
                fl = 1
            elif mode == 1:
                encmes = bits2str(encrmes)
                fl = 1
            elif mode == 2:
                encmes = bits2hex(encrmes)
                fl = 1
            else:
                print('Write a number in range 0-2 !')
        except Exception:
            print('Write a number!')
    with open('Cipher text.txt', 'w') as f:
        try:
            f.write(encmes)
        except Exception:
            print("\nMessage can't be written to this file in symbolic form!")
            f.write(encrmes)
            print('Message written to file in binary form.')
    print(f'Encrypted message :\n{encmes}\n')
    return encrmes

def encryption():
    with open('Open text.txt', 'r') as f:
        mes = str2bits(f.read())
    key = generationkey(len(mes))
    encrmes = xormes(mes, key)
    enc_bits = output(encrmes)

def decryption():
    with open('Cipher text.txt', 'r') as f:
        mes = f.read()
    with open('Key.txt', 'r') as f:
        key = f.read()
    dec_bits = xormes(mes, key)
    decmes = bits2str(dec_bits)
    print(f'Decrypted message:\n{decmes}\n')

def main():
    mode = 0
    while mode != 2:
        print('Type 0 - to encrypt message;\n     1 - to decrypt message.\n'
        +'     2 - to end work with program.')
        try:
            mode = int(input())
            if mode == 0:
                encryption()
            elif mode == 1:
                decryption()
            elif mode != 2:
                print('Program works in only 2 modes. Type 0 or 1 !')
        except Exception:
            print('Write a number!')

if __name__ == '__main__':
    main()
