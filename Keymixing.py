def string2bits(par=""):
    return [bin(ord(x))[2:].zfill(8) for x in par]
def xor_two_str(a,b):
    return ''.join([hex(ord(a[i%len(a)]) ^ ord(b[i%(len(b))]))[2:] for i in range(max(len(a), len(b)))])

def Master_Key_128(K1,K2):
    #Key Mixing-Start
    K1_1=string2bits(K1)[0:8]
    K1_2=string2bits(K2)[8:16]
    K2_1=string2bits(K2)[0:8]
    K2_2=string2bits(K2)[8:16]
    result=[]
    for i in range(8):
        result.append(xor_two_str(K2_1[i],xor_two_str(K1_1[i],xor_two_str(K1_2[i],K2_2[i]))))
    #Key Mixing-End
    #Key Expansion-Start
    K1_1_result=''.join(i for i in K1_1)
    K1_2_result=''.join(i for i in K1_2)
    K2_1_result=''.join(i for i in K2_1)
    K2_2_result=''.join(i for i in K2_2)
    temp=""

    for i in range(1,17):
        temp=temp+"".join(K1_1_result[4*i-1])+"".join(K1_2_result[4*i-1])+"".join(K2_1_result[4*i-1])+"".join(K2_2_result[4*i-1])

    for i in range(8):
        result.append(("".join(j for j in list(temp)[8*i:8*i+8])))
    #KeyExpansion-End
    #Converting Final Key into characters from binary
    finalkey=''
    for i in range(16):
        if(int(result[i],2)<32):
            finalkey=finalkey+chr(int(result[i],2)+33)
        else:
            finalkey=finalkey+chr(int(result[i],2))
    return finalkey




