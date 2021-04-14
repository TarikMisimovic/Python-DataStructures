#BLOOM FILTERS:



# Bit Vector in python is really just a list of bits ( A list of components that can be either 0 or 1)

import PyHash

bit_vector = [0] * 20
print(bit_vector)

# Non cryptographic hash functions (Murmur and FNW)

rnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()
 
# Calculate the output of FNV and Murmur hash functiosns for Pikachu and Charmander

fnv_pika = fnv("Pikachu") % 20
fnv_char = fnv("Charmander") % 20

murmur_pika = murmur("Pikachu") % 20
murmur_char = murmur("Charmander") % 20

print(fnv_pika)
print(fnv_char)

print(murmur_pika)
print(murmur_char)

