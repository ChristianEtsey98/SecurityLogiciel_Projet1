import hashlib

def simple_bruteforce(target_hash, charset, max_length):
    # Initialize a flag to track whether the correct password is found
    password_found = False
    
    # Loop through different password lengths
    for length in range(1, max_length + 1):
        # Check if the password is already found, break the loop if true
        if password_found:
            break
        
        # Call the generate_password function to attempt to find the password
        password_found = generate_password("", target_hash, charset, length)

def generate_password(prefix, target_hash, charset, length):
    # Check if the desired password length has been reached
    if length == 0:
        # Hash the generated password using MD5
        hashed_password = hashlib.md5(prefix.encode('utf-8')).hexdigest()
        
        # Print the current testing combination
        print(f"Testing combination - Password: {prefix}")

        # Check if the hashed password matches the target hash
        if hashed_password == target_hash:
            print(f"Password found: {prefix}")
            return True  # Return True if the correct password is found
    else:
        # Recursive call to generate all possible combinations
        for char in charset:
            if generate_password(prefix + char, target_hash, charset, length - 1):
                return True

if __name__ == "__main__":
    # Prompt the user for input
    target_hash = input("Enter the target hash: ")
    charset = input("Enter the character set to use: ")
    max_length = int(input("Enter the maximum password length: "))
    
    # Start the brute-force attack
    simple_bruteforce(target_hash, charset, max_length)
