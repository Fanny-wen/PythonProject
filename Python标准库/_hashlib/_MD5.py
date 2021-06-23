import hashlib
"""
md5, similar as sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), and blake2s() 
"""
input_str = "I'm learning the md5 function from hashlib"

# hexdigest(), 返回16进制字符串
output_str = hashlib.md5(input_str.encode('utf-8')).hexdigest().upper()
# digest(), 返回2进制字符串
output_str2 = hashlib.md5(input_str.encode('utf-8')).digest().upper()

print(output_str, len(output_str))
print(output_str2)

my_hash = hashlib.new('md5')
print(my_hash, my_hash.hexdigest())
print(my_hash.digest_size)
print(my_hash.block_size)
print(my_hash.name)
my_hash.update('sdf'.encode('utf-8'))
print(my_hash, my_hash.hexdigest())
