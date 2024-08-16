from sboxes import *

def XOR_str(str1,str2):
    result = ''
    for i in range(len(str1)):
        result += str( (int(str1[i]) + int(str2[i])) % 2 )
    return result

def NUM_to_BIN(str1,scale,num_of_bits):
    return bin(int(str1, scale))[2:].zfill(num_of_bits)

def shiftleft(str1,k):
    temp = ''
    temp += str1[k:]
    temp += str1[:k]
    return temp

def sub_mod(str1,str2):
    n = 2**32
    return str( ( int(str1) - int(str2) ) % n )

def add_mod(str1,str2):
    n = 2**32
    return str( ( int(str1) + int(str2) ) % n )

def BIN_to_DEC(str1):
    return str(int(str1, 2))


def F1(D,Kmi,Kri):
    dec_add = add_mod( BIN_to_DEC(Kmi) , BIN_to_DEC(D) )
    bin_add = NUM_to_BIN(dec_add,10,32)
    dec_k = int(BIN_to_DEC(Kri))
    I = shiftleft(bin_add , dec_k)
    
    Ia, Ib, Ic, Id = I[:8], I[8:16], I[16:24], I[24:32]
    S1_res, S2_res, S3_res, S4_res = NUM_to_BIN(S1(Ia),16,32), NUM_to_BIN(S2(Ib),16,32), NUM_to_BIN(S3(Ic),16,32), NUM_to_BIN(S4(Id),16,32)
    
    xor = XOR_str(S1_res, S2_res)
    xor_dec = BIN_to_DEC(xor)
    S3_res_dec = BIN_to_DEC(S3_res)
    sub = sub_mod(xor_dec, S3_res_dec)
    S4_res_dec = BIN_to_DEC(S4_res)
    add = add_mod(sub, S4_res_dec)
    return NUM_to_BIN(add, 10, 32)



def F2(D,Kmi,Kri):
    bin_xor = XOR_str( Kmi, D )
    dec_k = int(BIN_to_DEC(Kri))
    I = shiftleft(bin_xor , dec_k)
    
    Ia, Ib, Ic, Id = I[:8], I[8:16], I[16:24], I[24:32]
    S1_res, S2_res, S3_res, S4_res = NUM_to_BIN(S1(Ia),16,32), NUM_to_BIN(S2(Ib),16,32), NUM_to_BIN(S3(Ic),16,32), NUM_to_BIN(S4(Id),16,32)
    
    S1_res_dec, S2_res_dec = BIN_to_DEC(S1_res),BIN_to_DEC(S2_res)
    sub = sub_mod(S1_res_dec, S2_res_dec)
    S3_res_dec = BIN_to_DEC(S3_res)
    add = add_mod(sub, S3_res_dec)
    add_bin = NUM_to_BIN(add, 10, 32)
    xor = XOR_str(add_bin, S4_res)
    return xor



def F3(D,Kmi,Kri):
    dec_sub = sub_mod( BIN_to_DEC(Kmi) , BIN_to_DEC(D) )
    bin_sub = NUM_to_BIN(dec_sub,10,32)
    dec_k = int(BIN_to_DEC(Kri))
    I = shiftleft(bin_sub , dec_k)
    
    Ia, Ib, Ic, Id = I[:8], I[8:16], I[16:24], I[24:32]
    S1_res, S2_res, S3_res, S4_res = NUM_to_BIN(S1(Ia),16,32), NUM_to_BIN(S2(Ib),16,32), NUM_to_BIN(S3(Ic),16,32), NUM_to_BIN(S4(Id),16,32)
    
    S1_res_dec, S2_res_dec = BIN_to_DEC(S1_res),BIN_to_DEC(S2_res)
    add = add_mod(S1_res_dec, S2_res_dec)
    add_bin = NUM_to_BIN(add, 10, 32)
    xor = XOR_str(add_bin, S3_res)
    xor_dec = BIN_to_DEC(xor)
    S4_res_dec = BIN_to_DEC(S4_res)
    sub = sub_mod(xor_dec, S4_res_dec)
    return NUM_to_BIN(sub, 10, 32)


def XOR_4_times(key,X1,X2,X3,X4):
    temp = XOR_str(key, NUM_to_BIN( S5(X1) ,16 , 32 ))
    temp = XOR_str(temp, NUM_to_BIN( S6(X2) ,16 , 32 ))
    temp = XOR_str(temp, NUM_to_BIN( S7(X3) ,16 , 32 ))
    temp = XOR_str(temp, NUM_to_BIN( S8(X4) ,16 , 32 ))
    return temp

def char_to_hex(char):
    return hex(ord(char))[2:]

def hex_to_char(hex):
    return chr(int(hex,16))

def pad(message, mul):
    diff = math.ceil(len(message)/mul)*mul - len(message)
    temp = message
    for i in range(diff):
        temp += ' '
    return temp


def hex_to_message(original):
    message = ''
    for i in range(len(original)//2):
        message += hex_to_char(original[2*i] + original[2*i+1])
    return message

def message_to_hex(message):
    hex_message = ''
    for i in range(len(message)):
        hex_message += char_to_hex(message[i])
    return hex_message