import hashlib
import random

# Define the character set for passwords
CHARACTER_SET = "aA1!bB2@cC3#dD4$eE5^fF6&gG7*hH8(iI9)jJ0_kKl+LmM-nNo=OpP?qQr<RsS>tTuUvVwWxXyYzZ"

# Define the number of characters in each password
PASSWORD_LENGTH = 6

# Define the number of chains in the rainbow table
CHAIN_COUNT = 10000

# Define the chain length
CHAIN_LENGTH = 1000

# Define the reduction function
def reduce_function(hash_value, iteration_number):
    reduced_value = ""
    for i in range(PASSWORD_LENGTH):
        index = (iteration_number + i) % len(hash_value)
        char_index = int(hash_value[index], 16)
        reduced_value += CHARACTER_SET[char_index % len(CHARACTER_SET)]
    return reduced_value

# Ask the user for the hashing algorithm
hashing_algorithm = input("Enter the hashing algorithm used to generate the rainbow table (MD5, SHA-1, or SHA-256): ")

# Generate the rainbow table with a random starting password
rainbow_table = {}
if hashing_algorithm.lower() == "md5":
    hash_function = hashlib.md5
elif hashing_algorithm.lower() == "sha-1":
    hash_function = hashlib.sha1
elif hashing_algorithm.lower() == "sha-256":
    hash_function = hashlib.sha256
else:
    print("Invalid hashing algorithm.")
    exit()
for i in range(CHAIN_COUNT):
    print("Generating chain %d of %d" % (i + 1, CHAIN_COUNT))
    current_password = ''.join(random.choice(CHARACTER_SET) for _ in range(PASSWORD_LENGTH))
    current_hash = hash_function(current_password.encode()).hexdigest()
    for j in range(CHAIN_LENGTH):
        current_password = reduce_function(current_hash, j)
        current_hash = hash_function(current_password.encode()).hexdigest()
    rainbow_table[current_hash] = current_password

# Print the rainbow table to the terminal output
print("Rainbow table:")
for hash_value, password in rainbow_table.items():
    print("%s,%s" % (hash_value, password))

# Ask the user for a hash to crack
hash_to_crack = input("Enter the hash to crack: ")

# Try to crack the hash using the rainbow table
found_password = rainbow_table.get(hash_to_crack)

if found_password:
    print("Password found: %s" % found_password)
else:
    print("Password not found in the rainbow table")
