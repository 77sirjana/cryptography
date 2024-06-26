#WAP to create MD5 hash for bob and alice

import hashlib
md5hasher = hashlib.md5(b'alice')
alice_hash=md5hasher.hexdigest()
print("hash of text,alice is:",alice_hash)

md5hasher=hashlib.md5(b'bob')
bob_hash=md5hasher.hexdigest()
print("hash of text,alice is",bob_hash)