from util import *
from key_scheduler import *
import math


def encrypt_message_CAST(message,key,IV='NULL'):
    if len(key) != 32:
        raise Exception('Key isnt 128 bits')
        
    if IV == 'NULL':
            key_binary = NUM_to_BIN(key, 16, 128)
            
            
            message_hex = message_to_hex(message)
            block_size_hex = 16
            blocks = math.ceil(len(message_hex)/block_size_hex)
            
            encrypted_message = []
            
            for i in range(blocks):
                binary_block = NUM_to_BIN(message_hex[i*block_size_hex:(i+1)*block_size_hex],16,block_size_hex*4)
                encrypted_message.append(encrypt(binary_block, key_binary))
                
            # Turn ecrypted message into hex
            
            cipher_hex = ''
            for i in encrypted_message:
                for block in range(len(i)//4):
                    cipher_hex += hex(int(i[block*4:(block+1)*4],2))[2:]
            
            return cipher_hex

    else:
        if len(IV) != 16:
            raise Exception('IV vector isnt 64 bits')
        
        key_binary = NUM_to_BIN(key, 16, 128)
        IV_binary = NUM_to_BIN(IV,16,64)
    
        message_hex = message_to_hex(message)
        block_size_hex = 16
        blocks = math.ceil(len(message_hex)/block_size_hex)
        
        encrypted_message = []
        old_c = IV_binary
        
        for i in range(blocks):
            binary_block = NUM_to_BIN(message_hex[i*block_size_hex:(i+1)*block_size_hex],16,block_size_hex*4)
            x = XOR_str(binary_block,old_c)
            x = encrypt(x, key_binary)
            old_c = x
            encrypted_message.append(x)
            
        # Turn ecrypted message into hex
        
        cipher_hex = ''
        for i in encrypted_message:
            for block in range(len(i)//4):
                cipher_hex += hex(int(i[block*4:(block+1)*4],2))[2:]
        
        return cipher_hex


def decrypt_message_CAST(ciphertext,key,IV='NULL'):
    if len(key) != 32:
        raise Exception('Key isnt 128 bits')
    
    if IV == 'NULL':
        key_binary = NUM_to_BIN(key, 16, 128)
        
        block_size_hex = 16
        blocks = math.ceil(len(ciphertext)/block_size_hex)
        
    
        binary_message = NUM_to_BIN(ciphertext, 16, len(ciphertext)*4)
        
        original_message_binary = []
        for i in range(blocks):
            original_message_binary.append(decrypt(binary_message[i*64:(i+1)*64],key_binary))
        
        for i in range(len(original_message_binary)):
            original_message_binary[i] = original_message_binary[i].replace('00000000','')
        
        original_message_hex = []
        result = ''
        for i in original_message_binary:
            for block in range(len(i)//4):
                result += hex(int(i[block*4:(block+1)*4],2))[2:]
        
        result = hex_to_message(result)
        return result
    
    else:
        if len(IV) != 16:
            raise Exception('IV vector isnt 64 bits')
        
        key_binary = NUM_to_BIN(key, 16, 128)
        IV_binary = NUM_to_BIN(IV,16,64)
    
        
        block_size_hex = 16
        blocks = math.ceil(len(ciphertext)/block_size_hex)
        
    
        binary_message = NUM_to_BIN(ciphertext, 16, len(ciphertext)*4)
        old_c = IV_binary
        
        original_message_binary = []
        for i in range(blocks):
            x = decrypt(binary_message[i*64:(i+1)*64],key_binary)
            original_message_binary.append(XOR_str(x,old_c))
            old_c = binary_message[i*64:(i+1)*64]
        
        for i in range(len(original_message_binary)):
            original_message_binary[i] = original_message_binary[i].replace('00000000','')
        
        original_message_hex = []
        result = ''
        for i in original_message_binary:
            for block in range(len(i)//4):
                result += hex(int(i[block*4:(block+1)*4],2))[2:]
        
        result = hex_to_message(result)
        return result

def encrypt(plaintext,key):
    kmi, kri = key_scheduler(key)

    l,r = plaintext[:32], plaintext[32:]
    for i in range(16):
        old_l = l
        l = r 
        if i == 0 or i == 3 or i == 6 or i == 9 or i == 12 or i == 15:
            r = F1(l, kmi[i], kri[i])
        elif i == 1 or i == 4 or i == 7 or i == 10 or i == 13:
            r = F2(l, kmi[i], kri[i])
        elif i == 2 or i == 5 or i == 8 or i == 11 or i == 14:
            r = F3(l, kmi[i], kri[i])
        r = XOR_str(old_l, r)
    return r+l


def decrypt(ciphertext,key):
    kmi, kri = key_scheduler(key)

    l,r = ciphertext[:32], ciphertext[32:]
    
    for i in range(15,-1,-1):
        old_l = l
        l = r 
        if i == 0 or i == 3 or i == 6 or i == 9 or i == 12 or i == 15:
            r = F1(l, kmi[i], kri[i])
        elif i == 1 or i == 4 or i == 7 or i == 10 or i == 13:
            r = F2(l, kmi[i], kri[i])
        elif i == 2 or i == 5 or i == 8 or i == 11 or i == 14:
            r = F3(l, kmi[i], kri[i])
        r = XOR_str(old_l, r)
    return r+l


"""
TO USE ECB MODE GIVE THE MESSAGE AND THE KEY AS HEX TO BOTH FUNCTIONS
TO USE CBC MODE GIVE THE MESSAGE, KEY AS HEX AND IV AS HEX TO BOTH FUNCTIONS
RESPECTIVELY 
"""

"""
hex_key = '0123456712345678234567893456789A'
hex_original = input('enter message: ')
IV = 'ABCDEF0123456789'
x = encrypt_message_CAST(hex_original, hex_key, IV)
y = decrypt_message_CAST(x, hex_key, IV)
print('Encrypted Message: ' + str(x))
print('Decrypted Message: ' + str(y))
print('Are the two messages equal? ' + str(y == hex_original))
"""