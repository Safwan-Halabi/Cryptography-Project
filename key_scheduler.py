from sboxes import *
from util import *

def key_scheduler(key):
    keys = []
    byte = 8
    X0,X1,X2,X3,X4,X5,X6,X7,X8,X9,XA,XB,XC,XD,XE,XF = key[0:1*byte],key[1*byte:2*byte],key[2*byte:3*byte],key[3*byte:4*byte],key[4*byte:5*byte],key[5*byte:6*byte],key[6*byte:7*byte],key[7*byte:8*byte],key[8*byte:9*byte],key[9*byte:10*byte],key[10*byte:11*byte],key[11*byte:12*byte],key[12*byte:13*byte],key[13*byte:14*byte],key[14*byte:15*byte],key[15*byte:16*byte]
    
    # Keys 1 - 4
    
    temp = X0 + X1 + X2 + X3
    temp = XOR_str(temp, NUM_to_BIN( S7(X8) ,16 , 32 ))
    Z0to3 = XOR_4_times(temp,XD, XF, XC, XE)  
    Z0, Z1, Z2, Z3 = Z0to3[0:1*byte],Z0to3[1*byte:2*byte],Z0to3[2*byte:3*byte],Z0to3[3*byte:4*byte]
    
    temp = X8 + X9 + XA + XB
    temp = XOR_str(temp, NUM_to_BIN( S8(XA) ,16 , 32 ))
    Z4to7 = XOR_4_times(temp, Z0, Z2, Z1, Z3)
    Z4, Z5, Z6, Z7 = Z4to7[0:1*byte],Z4to7[1*byte:2*byte],Z4to7[2*byte:3*byte],Z4to7[3*byte:4*byte]

    temp = XC + XD + XE + XF
    temp = XOR_str(temp, NUM_to_BIN( S5(X9) ,16 , 32 ))
    Z8toB = XOR_4_times(temp, Z7, Z6, Z5, Z4)
    Z8, Z9, ZA, ZB = Z8toB[0:1*byte],Z8toB[1*byte:2*byte],Z8toB[2*byte:3*byte],Z8toB[3*byte:4*byte]

    temp = X4 + X5 + X6 + X7
    temp = XOR_str(temp, NUM_to_BIN( S6(XB) ,16 , 32 ))
    ZCtoF = XOR_4_times(temp, ZA, Z9, ZB, Z8)
    ZC, ZD, ZE, ZF = ZCtoF[0:1*byte],ZCtoF[1*byte:2*byte],ZCtoF[2*byte:3*byte],ZCtoF[3*byte:4*byte]

    # Now we're ready to compute K1 to K4

    # K1
    temp = NUM_to_BIN( S5(Z2) ,16 , 32 )
    keys.append(XOR_4_times(temp, Z8, Z9, Z7, Z6))

    # K2
    temp = NUM_to_BIN( S6(Z6) ,16 , 32 )
    keys.append(XOR_4_times(temp, ZA, ZB, Z5, Z4))

     # K3
    temp = NUM_to_BIN( S7(Z9) ,16 , 32 )
    keys.append(XOR_4_times(temp, ZC, ZD, Z3, Z2))

    # K4
    temp = NUM_to_BIN( S8(ZC) ,16 , 32 )
    keys.append(XOR_4_times(temp, ZE, ZF, Z1, Z0))

    # Keys 5 - 8
    
    temp = Z8 + Z9 + ZA + ZB
    temp = XOR_str(temp, NUM_to_BIN( S7(Z0) ,16 , 32 ))
    X0to3 = XOR_4_times(temp,Z5, Z7, Z4, Z6)  
    X0, X1, X2, X3 = X0to3[0:1*byte],X0to3[1*byte:2*byte],X0to3[2*byte:3*byte],X0to3[3*byte:4*byte]
    
    temp = Z0 + Z1 + Z2 + Z3
    temp = XOR_str(temp, NUM_to_BIN( S8(Z2) ,16 , 32 ))
    X4to7 = XOR_4_times(temp, X0, X2, X1, X3)
    X4, X5, X6, X7 = X4to7[0:1*byte],X4to7[1*byte:2*byte],X4to7[2*byte:3*byte],X4to7[3*byte:4*byte]

    temp = Z4 + Z5 + Z6 + Z7
    temp = XOR_str(temp, NUM_to_BIN( S5(Z1) ,16 , 32 ))
    X8toB = XOR_4_times(temp, X7, X6, X5, X4)
    X8, X9, XA, XB = Z8toB[0:1*byte],Z8toB[1*byte:2*byte],Z8toB[2*byte:3*byte],Z8toB[3*byte:4*byte]

    temp = ZC + ZD + ZE + ZF
    temp = XOR_str(temp, NUM_to_BIN( S6(Z3) ,16 , 32 ))
    XCtoF = XOR_4_times(temp, XA, X9, XB, X8)
    XC, XD, XE, XF = XCtoF[0:1*byte],XCtoF[1*byte:2*byte],XCtoF[2*byte:3*byte],XCtoF[3*byte:4*byte]

    # Now we're ready to compute K5 to K8
    
    # K5
    temp = NUM_to_BIN( S5(X8) ,16 , 32 )
    keys.append(XOR_4_times(temp, X3, X2, XC, XD))

    # K6
    temp = NUM_to_BIN( S6(XD) ,16 , 32 )
    keys.append(XOR_4_times(temp, X1, X0, XE, XF))

     # K7
    temp = NUM_to_BIN( S7(X3) ,16 , 32 )
    keys.append(XOR_4_times(temp, X7, X6, X8, X9))

    # K8
    temp = NUM_to_BIN( S8(X7) ,16 , 32 )
    keys.append(XOR_4_times(temp, X5, X4, XA, XB))
    
    # Keys 9 - 12
    
    temp = X0 + X1 + X2 + X3
    temp = XOR_str(temp, NUM_to_BIN( S7(X8) ,16 , 32 ))
    Z0to3 = XOR_4_times(temp,XD, XF, XC, XE)  
    Z0, Z1, Z2, Z3 = Z0to3[0:1*byte],Z0to3[1*byte:2*byte],Z0to3[2*byte:3*byte],Z0to3[3*byte:4*byte]
    
    temp = X8 + X9 + XA + XB
    temp = XOR_str(temp, NUM_to_BIN( S8(XA) ,16 , 32 ))
    Z4to7 = XOR_4_times(temp, Z0, Z2, Z1, Z3)
    Z4, Z5, Z6, Z7 = Z4to7[0:1*byte],Z4to7[1*byte:2*byte],Z4to7[2*byte:3*byte],Z4to7[3*byte:4*byte]

    temp = XC + XD + XE + XF
    temp = XOR_str(temp, NUM_to_BIN( S5(X9) ,16 , 32 ))
    Z8toB = XOR_4_times(temp, Z7, Z6, Z5, Z4)
    Z8, Z9, ZA, ZB = Z8toB[0:1*byte],Z8toB[1*byte:2*byte],Z8toB[2*byte:3*byte],Z8toB[3*byte:4*byte]

    temp = X4 + X5 + X6 + X7
    temp = XOR_str(temp, NUM_to_BIN( S6(XB) ,16 , 32 ))
    ZCtoF = XOR_4_times(temp, ZA, Z9, ZB, Z8)
    ZC, ZD, ZE, ZF = ZCtoF[0:1*byte],ZCtoF[1*byte:2*byte],ZCtoF[2*byte:3*byte],ZCtoF[3*byte:4*byte]
    
    # Now we're ready to compute K9 to K12

    # K9
    temp = NUM_to_BIN( S5(Z9) ,16 , 32 )
    keys.append(XOR_4_times(temp, Z3, Z2, ZC, ZD))

    # K10
    temp = NUM_to_BIN( S6(ZC) ,16 , 32 )
    keys.append(XOR_4_times(temp, Z1, Z0, ZE, ZF))

     # K11
    temp = NUM_to_BIN( S7(Z2) ,16 , 32 )
    keys.append(XOR_4_times(temp, Z7, Z6, Z8, Z9))

    # K12
    temp = NUM_to_BIN( S8(Z6) ,16 , 32 )
    keys.append(XOR_4_times(temp, Z5, Z4, ZA, ZB))
    
    # Keys 9 - 12
    
    temp = Z8 + Z9 + ZA + ZB
    temp = XOR_str(temp, NUM_to_BIN( S7(Z0) ,16 , 32 ))
    X0to3 = XOR_4_times(temp,Z5, Z7, Z4, Z6)  
    X0, X1, X2, X3 = X0to3[0:1*byte],X0to3[1*byte:2*byte],X0to3[2*byte:3*byte],X0to3[3*byte:4*byte]
    
    temp = Z0 + Z1 + Z2 + Z3
    temp = XOR_str(temp, NUM_to_BIN( S8(Z2) ,16 , 32 ))
    X4to7 = XOR_4_times(temp, X0, X2, X1, X3)
    X4, X5, X6, X7 = X4to7[0:1*byte],X4to7[1*byte:2*byte],X4to7[2*byte:3*byte],X4to7[3*byte:4*byte]

    temp = Z4 + Z5 + Z6 + Z7
    temp = XOR_str(temp, NUM_to_BIN( S5(Z1) ,16 , 32 ))
    X8toB = XOR_4_times(temp, X7, X6, X5, X4)
    X8, X9, XA, XB = Z8toB[0:1*byte],Z8toB[1*byte:2*byte],Z8toB[2*byte:3*byte],Z8toB[3*byte:4*byte]

    temp = ZC + ZD + ZE + ZF
    temp = XOR_str(temp, NUM_to_BIN( S6(Z3) ,16 , 32 ))
    XCtoF = XOR_4_times(temp, XA, X9, XB, X8)
    XC, XD, XE, XF = XCtoF[0:1*byte],XCtoF[1*byte:2*byte],XCtoF[2*byte:3*byte],XCtoF[3*byte:4*byte]
    
    # Now we're ready to compute K13 to K16

    # K13
    temp = NUM_to_BIN( S5(X3) ,16 , 32 )
    keys.append(XOR_4_times(temp, X8, X9, X7, X6))

    # K14
    temp = NUM_to_BIN( S6(X7) ,16 , 32 )
    keys.append(XOR_4_times(temp, XA, XB, X5, X4))

     # K15
    temp = NUM_to_BIN( S7(X8) ,16 , 32 )
    keys.append(XOR_4_times(temp, XC, XD, X3, X2))

    # K16
    temp = NUM_to_BIN( S8(XD) ,16 , 32 )
    keys.append(XOR_4_times(temp, XE, XF, X1, X0))
    
    ######################################################################################
    #### KEYS 17 - 32
    ######################################################################################
    
    # Keys 17 - 20
    
    temp = X0 + X1 + X2 + X3
    temp = XOR_str(temp, NUM_to_BIN( S7(X8) ,16 , 32 ))
    Z0to3 = XOR_4_times(temp,XD, XF, XC, XE)  
    Z0, Z1, Z2, Z3 = Z0to3[0:1*byte],Z0to3[1*byte:2*byte],Z0to3[2*byte:3*byte],Z0to3[3*byte:4*byte]
    
    temp = X8 + X9 + XA + XB
    temp = XOR_str(temp, NUM_to_BIN( S8(XA) ,16 , 32 ))
    Z4to7 = XOR_4_times(temp, Z0, Z2, Z1, Z3)
    Z4, Z5, Z6, Z7 = Z4to7[0:1*byte],Z4to7[1*byte:2*byte],Z4to7[2*byte:3*byte],Z4to7[3*byte:4*byte]

    temp = XC + XD + XE + XF
    temp = XOR_str(temp, NUM_to_BIN( S5(X9) ,16 , 32 ))
    Z8toB = XOR_4_times(temp, Z7, Z6, Z5, Z4)
    Z8, Z9, ZA, ZB = Z8toB[0:1*byte],Z8toB[1*byte:2*byte],Z8toB[2*byte:3*byte],Z8toB[3*byte:4*byte]

    temp = X4 + X5 + X6 + X7
    temp = XOR_str(temp, NUM_to_BIN( S6(XB) ,16 , 32 ))
    ZCtoF = XOR_4_times(temp, ZA, Z9, ZB, Z8)
    ZC, ZD, ZE, ZF = ZCtoF[0:1*byte],ZCtoF[1*byte:2*byte],ZCtoF[2*byte:3*byte],ZCtoF[3*byte:4*byte]

    # Now we're ready to compute K17 to K20

    # K17
    temp = NUM_to_BIN( S5(Z2) ,16 , 32 )
    keys.append(XOR_4_times(temp, Z8, Z9, Z7, Z6))

    # K18
    temp = NUM_to_BIN( S6(Z6) ,16 , 32 )
    keys.append(XOR_4_times(temp, ZA, ZB, Z5, Z4))

     # 19
    temp = NUM_to_BIN( S7(Z9) ,16 , 32 )
    keys.append(XOR_4_times(temp, ZC, ZD, Z3, Z2))

    # K20
    temp = NUM_to_BIN( S8(ZC) ,16 , 32 )
    keys.append(XOR_4_times(temp, ZE, ZF, Z1, Z0))

    # Keys 21 - 24
    
    temp = Z8 + Z9 + ZA + ZB
    temp = XOR_str(temp, NUM_to_BIN( S7(Z0) ,16 , 32 ))
    X0to3 = XOR_4_times(temp,Z5, Z7, Z4, Z6)  
    X0, X1, X2, X3 = X0to3[0:1*byte],X0to3[1*byte:2*byte],X0to3[2*byte:3*byte],X0to3[3*byte:4*byte]
    
    temp = Z0 + Z1 + Z2 + Z3
    temp = XOR_str(temp, NUM_to_BIN( S8(Z2) ,16 , 32 ))
    X4to7 = XOR_4_times(temp, X0, X2, X1, X3)
    X4, X5, X6, X7 = X4to7[0:1*byte],X4to7[1*byte:2*byte],X4to7[2*byte:3*byte],X4to7[3*byte:4*byte]

    temp = Z4 + Z5 + Z6 + Z7
    temp = XOR_str(temp, NUM_to_BIN( S5(Z1) ,16 , 32 ))
    X8toB = XOR_4_times(temp, X7, X6, X5, X4)
    X8, X9, XA, XB = Z8toB[0:1*byte],Z8toB[1*byte:2*byte],Z8toB[2*byte:3*byte],Z8toB[3*byte:4*byte]

    temp = ZC + ZD + ZE + ZF
    temp = XOR_str(temp, NUM_to_BIN( S6(Z3) ,16 , 32 ))
    XCtoF = XOR_4_times(temp, XA, X9, XB, X8)
    XC, XD, XE, XF = XCtoF[0:1*byte],XCtoF[1*byte:2*byte],XCtoF[2*byte:3*byte],XCtoF[3*byte:4*byte]

    # Now we're ready to compute K21 to K24
    
    # K21
    temp = NUM_to_BIN( S5(X8) ,16 , 32 )
    keys.append(XOR_4_times(temp, X3, X2, XC, XD))

    # K22
    temp = NUM_to_BIN( S6(XD) ,16 , 32 )
    keys.append(XOR_4_times(temp, X1, X0, XE, XF))

     # K23
    temp = NUM_to_BIN( S7(X3) ,16 , 32 )
    keys.append(XOR_4_times(temp, X7, X6, X8, X9))

    # K24
    temp = NUM_to_BIN( S8(X7) ,16 , 32 )
    keys.append(XOR_4_times(temp, X5, X4, XA, XB))
    
    # Keys 25 - 28
    
    temp = X0 + X1 + X2 + X3
    temp = XOR_str(temp, NUM_to_BIN( S7(X8) ,16 , 32 ))
    Z0to3 = XOR_4_times(temp,XD, XF, XC, XE)  
    Z0, Z1, Z2, Z3 = Z0to3[0:1*byte],Z0to3[1*byte:2*byte],Z0to3[2*byte:3*byte],Z0to3[3*byte:4*byte]
    
    temp = X8 + X9 + XA + XB
    temp = XOR_str(temp, NUM_to_BIN( S8(XA) ,16 , 32 ))
    Z4to7 = XOR_4_times(temp, Z0, Z2, Z1, Z3)
    Z4, Z5, Z6, Z7 = Z4to7[0:1*byte],Z4to7[1*byte:2*byte],Z4to7[2*byte:3*byte],Z4to7[3*byte:4*byte]

    temp = XC + XD + XE + XF
    temp = XOR_str(temp, NUM_to_BIN( S5(X9) ,16 , 32 ))
    Z8toB = XOR_4_times(temp, Z7, Z6, Z5, Z4)
    Z8, Z9, ZA, ZB = Z8toB[0:1*byte],Z8toB[1*byte:2*byte],Z8toB[2*byte:3*byte],Z8toB[3*byte:4*byte]

    temp = X4 + X5 + X6 + X7
    temp = XOR_str(temp, NUM_to_BIN( S6(XB) ,16 , 32 ))
    ZCtoF = XOR_4_times(temp, ZA, Z9, ZB, Z8)
    ZC, ZD, ZE, ZF = ZCtoF[0:1*byte],ZCtoF[1*byte:2*byte],ZCtoF[2*byte:3*byte],ZCtoF[3*byte:4*byte]
    
    # Now we're ready to compute K25 to K28

    # K25
    temp = NUM_to_BIN( S5(Z9) ,16 , 32 )
    keys.append(XOR_4_times(temp, Z3, Z2, ZC, ZD))

    # K26
    temp = NUM_to_BIN( S6(ZC) ,16 , 32 )
    keys.append(XOR_4_times(temp, Z1, Z0, ZE, ZF))

     # K27
    temp = NUM_to_BIN( S7(Z2) ,16 , 32 )
    keys.append(XOR_4_times(temp, Z7, Z6, Z8, Z9))

    # K28
    temp = NUM_to_BIN( S8(Z6) ,16 , 32 )
    keys.append(XOR_4_times(temp, Z5, Z4, ZA, ZB))
    
    # Keys 29 - 32
    
    temp = Z8 + Z9 + ZA + ZB
    temp = XOR_str(temp, NUM_to_BIN( S7(Z0) ,16 , 32 ))
    X0to3 = XOR_4_times(temp,Z5, Z7, Z4, Z6)  
    X0, X1, X2, X3 = X0to3[0:1*byte],X0to3[1*byte:2*byte],X0to3[2*byte:3*byte],X0to3[3*byte:4*byte]
    
    temp = Z0 + Z1 + Z2 + Z3
    temp = XOR_str(temp, NUM_to_BIN( S8(Z2) ,16 , 32 ))
    X4to7 = XOR_4_times(temp, X0, X2, X1, X3)
    X4, X5, X6, X7 = X4to7[0:1*byte],X4to7[1*byte:2*byte],X4to7[2*byte:3*byte],X4to7[3*byte:4*byte]

    temp = Z4 + Z5 + Z6 + Z7
    temp = XOR_str(temp, NUM_to_BIN( S5(Z1) ,16 , 32 ))
    X8toB = XOR_4_times(temp, X7, X6, X5, X4)
    X8, X9, XA, XB = Z8toB[0:1*byte],Z8toB[1*byte:2*byte],Z8toB[2*byte:3*byte],Z8toB[3*byte:4*byte]

    temp = ZC + ZD + ZE + ZF
    temp = XOR_str(temp, NUM_to_BIN( S6(Z3) ,16 , 32 ))
    XCtoF = XOR_4_times(temp, XA, X9, XB, X8)
    XC, XD, XE, XF = XCtoF[0:1*byte],XCtoF[1*byte:2*byte],XCtoF[2*byte:3*byte],XCtoF[3*byte:4*byte]
    
    # Now we're ready to compute K29 to K32

    # K29
    temp = NUM_to_BIN( S5(X3) ,16 , 32 )
    keys.append(XOR_4_times(temp, X8, X9, X7, X6))

    # K30
    temp = NUM_to_BIN( S6(X7) ,16 , 32 )
    keys.append(XOR_4_times(temp, XA, XB, X5, X4))

     # K31
    temp = NUM_to_BIN( S7(X8) ,16 , 32 )
    keys.append(XOR_4_times(temp, XC, XD, X3, X2))

    # K32
    temp = NUM_to_BIN( S8(XD) ,16 , 32 )
    keys.append(XOR_4_times(temp, XE, XF, X1, X0))

    kmi, kri = [],[]
    
    for i in range(16):
        kmi.append(keys[i])
        kri.append(keys[i+16][27:])

    return kmi, kri

