import hashlib
 
input = "ckczppom"
i=0

while hashlib.md5((input+str(i)).encode()).hexdigest()[0:6] != '000000':
    i+=1

print(hashlib.md5((input+str(i)).encode()).hexdigest(), i)
