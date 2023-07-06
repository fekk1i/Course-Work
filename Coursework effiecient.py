import hashlib
import random

class RainbowTable:
    def __init__(self, hashing_algorithm, character_set, password_length, chain_count, chain_length):
        self.hashing_algorithm = hashing_algorithm
        self.character_set = character_set
        self.password_length = password_length
        self.chain_count = chain_count
        self.chain_length = chain_length
        self.rainbow_table = {}

    def generate_rainbow_table(self):
        if self.hashing_algorithm.lower() == "md5":
            hash_function = hashlib.md5
        elif self.hashing_algorithm.lower() == "sha-1":
            hash_function = hashlib.sha1
        elif self.hashing_algorithm.lower() == "sha-256":
            hash_function = hashlib.sha256
        else:
            raise ValueError("Invalid hashing algorithm.")

        for i in range(self.chain_count):
            print("Generating chain %d of %d" % (i + 1, self.chain_count))
            current_password = ''.join(random.choice(self.character_set) for _ in range(self.password_length))
            current_hash = hash_function(current_password.encode()).hexdigest()
            for j in range(self.chain_length):
                current_password = self.reduce_function(current_hash, j)
                current_hash = hash_function(current_password.encode()).hexdigest()
            self.rainbow_table[current_hash] = current_password

    def reduce_function(self, hash_value, iteration_number):
        reduced_value = ""
        for i in range(self.password_length):
            index = (iteration_number + i) % len(hash_value)
            char_index = int(hash_value[index], 16)
            reduced_value += self.character_set[char_index % len(self.character_set)]
        return reduced_value

    def print_rainbow_table(self):
        print("Rainbow table:")
        for hash_value, password in self.rainbow_table.items():
            print("%s,%s" % (hash_value, password))

    def crack_hash(self, hash_to_crack):
        found_password = self.rainbow_table.get(hash_to_crack)
        if found_password:
            return found_password
        else:
            return None


# Define the parameters
hashing_algorithm = input("Enter the hashing algorithm used to generate the rainbow table (MD5, SHA-1, or SHA-256): ")
character_set = "aA1!bB2@cC3#dD4$eE5^fF6&gG7*hH8(iI9)jJ0_kKl+LmM-nNo=OpP?qQr<RsS>tTuUvVwWxXyYzZ"
password_length = 6
chain_count = 10000
chain_length = 1000

# Create a RainbowTable instance and generate the table
rainbow_table = RainbowTable(hashing_algorithm, character_set, password_length, chain_count, chain_length)
rainbow_table.generate_rainbow_table()

# Print the rainbow table
rainbow_table.print_rainbow_table()

# Ask the user for a hash to crack
hash_to_crack = input("Enter the hash to crack: ")

# Try to crack the hash using the rainbow table
found_password = rainbow_table.crack_hash(hash_to_crack)

if found_password:
    print("Password found: %s" % found_password)
else:
    print("Password not found in the rainbow table")
