Rainbow Table Password Cracker
The Rainbow Table Password Cracker is a Python program that generates a rainbow table and allows you to crack hashed passwords using the table. It supports the MD5, SHA-1, and SHA-256 hashing algorithms.

Prerequisites:
Python 3.x installed on your system

Usage:

1.Clone or download the repository to your local machine.

2.Open a terminal or command prompt and navigate to the project directory.

3.Run the rainbow_table.py file using the following command:

(python rainbow_table.py)

4.You will be prompted to enter the hashing algorithm to generate the rainbow table. You can choose from MD5, SHA-1, or SHA-256.

5.The program will generate the rainbow table based on the chosen algorithm. This process may take some time, depending on the specified parameters.

6.Once the rainbow table is generated, it will be displayed in the terminal. Note the hash values and corresponding passwords.

7.To crack a hash, enter the desired hash value when prompted.

8.The program will search the rainbow table for a matching password. If a match is found, it will be displayed in the terminal. If not, a message indicating that the password was not found will be shown.

9.You can repeat steps 7-8 to crack additional hashes.

Customization:
You can customize the parameters of the rainbow table generation by modifying the following variables in the rainbow_table.py file:

CHARACTER_SET: The character set used to generate passwords.
PASSWORD_LENGTH: The length of each password.
CHAIN_COUNT: The number of chains in the rainbow table.
CHAIN_LENGTH: The length of each chain.

Feel free to adjust these parameters according to your needs, but keep in mind that larger values may significantly increase the time and computational resources required for rainbow table generation.
