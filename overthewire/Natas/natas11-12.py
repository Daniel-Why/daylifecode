import base64
from operator import xor
data = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="
origin_data ='{"showpassword":"no","bgcolor":"#ffffff"}'

data_base64 = base64.b64decode(data)

ord_list=[ord(x) for x in origin_data]

zipped = zip(data_base64,ord_list)

key = map(lambda x:chr(x[0]^x[1]),zipped)

key = [i for i in key]

print(''.join(key))


data2 = '{"showpassword":"yes","bgcolor":"#ffffff"}'

key2 = 'qw8J'

key_derive = key2*(int(len(data2)/len(key2)))+key2[0:len(data2)%len(key2)+1]

print("len of data2:{}".format(len(data2)))

print("len of pre:{}".format(int(len(data2)/len(key2))))

print("len of suf:{}".format(len(data2)%len(key2)+1))

print("len of key_derive:{}".format(len(key_derive)))

print(key_derive)

def xor_cal(m,n):
    return map(lambda x: chr(ord(x[0])^ord(x[1])),zip(m,n))

cipher = bytes("".join(xor_cal(data2,key_derive)),encoding='utf-8')
print(cipher)
text = base64.b64encode(cipher)
print(text)

