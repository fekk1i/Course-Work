import hashlib
import os
import time
import random


# Define the character set for passwords
CHARACTER_SET = "aA1!bB2@cC3#dD4$eE5^fF6&gG7*hH8(iI9)jJ0_kKl+LmM-nNo=OpP?qQr<RsS>tTuUvVwWxXyYzZ"

# Define the number of characters in each password
PASSWORD_LENGTH = 6

# Define the number of chains in the rainbow table
CHAIN_COUNT = 10000

# Define the chain length
CHAIN_LENGTH = 1000

start_reduction = time.time()
# Define the reduction function
def reduce_function(hash_value, iteration_number):
    reduced_value = ""
    for i in range(PASSWORD_LENGTH):
        index = (iteration_number + i) % len(hash_value)
        char_index = int(hash_value[index], 16)
        reduced_value += CHARACTER_SET[char_index % len(CHARACTER_SET)]
    return reduced_value
end_reduction = time.time()

# Ask the user for the hashing algorithm
hashing_algorithm = input("Enter the hashing algorithm used to generate the rainbow table (MD5, SHA-1, or SHA-256): ")

start_rainbow = time.time()
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
        if current_hash not in rainbow_table:
            rainbow_table[current_hash] = current_password
end_rainbow = time.time()

# Print the rainbow table to the terminal output
print("Rainbow table:")
for hash_value, password in rainbow_table.items():
    print("%s,%s" % (hash_value, password))

start_save = time.time()
# Save the rainbow table to a file in the Documents folder
file_path = os.path.join(os.path.expanduser("~"), "Documents", "Log1.txt")
with open(file_path, "w") as file:
    for hash_value, password in rainbow_table.items():
        file.write("%s,%s\n" % (hash_value, password))
print("Rainbow table saved to %s" % file_path)

end_save = time.time()

start_output = time.time()
# Read the rainbow table file and create a dictionary
rainbow_dict = {}
with open(file_path, "r") as file:
    for line in file:
        hash_value, password = line.strip().split(",")
        rainbow_dict[hash_value] = password
        rainbow_table[hash_value] = password
end_output = time.time()

# Ask the user for a hash to crack
hash_to_crack = input("Enter the hash to crack: ")

start_crack = time.time()
# Try to crack the hash
if hash_to_crack in rainbow_dict:
    print("Password found: %s" % rainbow_dict[hash_to_crack])
else:
    print("Password not found in the rainbow table")
end_crack = time.time()

reduction_time = end_reduction - start_reduction
rainbow_time = end_rainbow - start_rainbow
save_time = end_save - start_save
output_time = end_output - start_output
crack_time = end_crack - start_crack

print(f"Reduction function execution time: {reduction_time:.2f} seconds")
print(f"Rainbow table creation time: {rainbow_time:.2f} seconds")
print(f"File Save Time: {save_time:.2f} seconds")
print(f"Rainbow table output to terminal time: {output_time:.2f} seconds")
print(f"Password cracking execution time: {crack_time:.2f} seconds")
