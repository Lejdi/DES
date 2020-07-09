startPermutation=[58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
                  62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
                  57, 49, 41, 33, 25, 17, 9,  1, 59, 51, 43, 35, 27, 19, 11, 3,
                  61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

endPermutation=[40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9,  49, 17, 57, 25]

keyPermutation=[57, 49, 41, 33, 25, 17,  9,  1, 58, 50, 42, 34, 26, 18,
                10,  2, 59, 51, 43, 35, 27, 19, 11,  3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,  7, 62, 54, 46, 38, 30, 22,
                14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 28, 20, 12,  4]

roundShift=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

compressPermutation=[14, 17, 11, 24,  1,  5,  3, 28, 15,  6 ,21, 10,
                     23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,
                     41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
                     44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

extendPermutation=[32,  1,  2,  3,  4,  5,  4,  5,  6,  7,  8,  9,
                    8,  9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
                   16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
                   24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32,  1]

P_box=[16, 7, 20, 21, 29, 12, 28, 17,  1, 15, 23, 26,  5, 18, 31, 10,
        2, 8, 24, 14, 32, 27,  3,  9, 19, 13, 30,  6, 22, 11,  4, 25]

S_box = [[
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],[
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],[
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],[
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        ],[
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ],[
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        ],[
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        ],[
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ]
    ]

def stringXOR(str1,str2):
    strXOR = ""
    for i in range(0,min(len(str1), len(str2))):
        strXOR += str(int(str1[i]) ^ int(str2[i]))
    return strXOR

def getKey():
    recSize = 22
    mask = 0b111
    threeBits = []

    samples = sd.rec(int(recSize), channels=1, dtype='int16')
    sd.wait()

    for i in range(int(recSize)):
        threeBits.append('00')
        threeBits[i] += (bin(samples[i][0] & mask)[2:5])
        threeBits[i] = threeBits[i][-3:]

    allBits = ''
    for i in threeBits:
        allBits += i
    return (allBits[:-2])

def rotateKey(key):
    key_left=(key.copy())[:28]
    key_right=(key.copy())[28:]
    
    temp_left=key_left[0]
    temp_right=key_right[0]
    for i in range(27):
        key_left[i]=key_left[i+1]
        key_right[i]=key_right[i+1]
    key_left[27]=temp_left
    key_right[27]=temp_right
    resKey_left=''.join(key_left)
    resKey_right=''.join(key_right)
    resKey_left+=resKey_right
    return resKey_left

def generateKeys(key):
    res=[]
    #key 64 bits -> 56 bits
    key_56bit=list(range(56))
    for i in range(56):
        idx=keyPermutation[i]
        key_56bit[i]=key[idx-1]
    for i in range(16):
        #rotate key
        for j in range(roundShift[i]):
            key_56bit=list(rotateKey(key_56bit))
        #key 56bits -> 48bits compression
        key_48bit=list(range(48))
        for j in range(48):
            idx=compressPermutation[j]
            key_48bit[j]=key_56bit[idx-1]
        key_48bit=''.join(key_48bit)
        res.append(key_48bit)
    return res

#key=getKey() #key from trng
key=list('0000111000110010100100100011001011101010011011010000110101110011') #0E329232EA6D0D73 in hex

message=list('1000011110000111100001111000011110000111100001111000011110000111') #8787878787878787 in hex

#expected result: 0000000000000000000000000000000000000000000000000000000000000000

keys=generateKeys(key)
    
#start permutation
permuted_msg=list(range(64))
for i in range(64):
    idx=startPermutation[i]
    permuted_msg[i]=message[idx-1]

message_left=(permuted_msg.copy())[:32]
message_right=(permuted_msg.copy())[32:]
#16 rounds of simple math operations
for r in range(16):
    #new left side of message
    new_message_left=message_right.copy()
        
    #message 32bits -> 48bits extension
    message_right_48bit=list(range(48))
    for i in range(48):
        idx=extendPermutation[i]
        message_right_48bit[i]=message_right[idx-1]
    
    #message XOR with key
    msg_to_xor=''.join(message_right_48bit)
    xored_msg_right=stringXOR(msg_to_xor,keys[r])

    #48bits -> 32bits using S-boxes
    result_msg_right=''
    xored_msg_right=list(xored_msg_right)
    sliced_msg_right=[]
    for i in range(8):
        #get 6 bits
        sliced_msg_right=(xored_msg_right.copy())[i*6:i*6+6]
        sliced_msg_right=''.join(sliced_msg_right)
        #calculate row
        row=''
        row+=sliced_msg_right[0]
        row+=sliced_msg_right[5]
        row=int(row,2)
        #calculate column
        column=''
        for j in range(1, 5):
            column+=sliced_msg_right[j]
        column=int(column,2)
        #get element from S-box
        sliced_msg_right=bin(S_box[i][row][column])[2:]
        #format string and add to result message
        sliced_msg_right=("0000"+sliced_msg_right)[-4:]
        result_msg_right+=sliced_msg_right
        
    #right msg p-box permutation
    P_box_msg_right=list(range(32))
    for i in range(32):
        idx=P_box[i]
        P_box_msg_right[i]=result_msg_right[idx-1]
        
    #left message XOR with right message
    left_msg_str=''.join(message_left)
    right_msg_str=''.join(P_box_msg_right)
    new_right_message=list(stringXOR(left_msg_str,right_msg_str))
    message_left=new_message_left.copy()
    message_right=new_right_message.copy()
    
#merge left and right message parts
right_part=''.join(message_right)
left_part=''.join(message_left)
message=''
message+=left_part
message+=right_part
message=list(message)

#end permutation
permuted_msg=list(range(64))
for i in range(64):
    idx=endPermutation[i]
    permuted_msg[i]=message[idx-1]

print(''.join(permuted_msg))















    

