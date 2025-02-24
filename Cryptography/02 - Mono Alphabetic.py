# Function to create a cipher mapping based on the key
def create_cipher(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_map = {alphabet[i]: key[i] for i in range(len(alphabet))}
    return cipher_map

# Function to encrypt the message
def encrypt(plaintext, cipher_map):
    encrypted_text = ""
    for char in plaintext:
        if char.upper() in cipher_map:
            encrypted_text += cipher_map[char.upper()].upper() if char.isupper() else cipher_map[char.upper()].lower()
        else:
            encrypted_text += char  # Keep spaces and special characters unchanged
    return encrypted_text

# Function to decrypt the message
def decrypt(ciphertext, cipher_map):
    reverse_cipher_map = {v: k for k, v in cipher_map.items()}  # Reverse the key mapping
    decrypted_text = ""
    for char in ciphertext:
        if char.upper() in reverse_cipher_map:
            decrypted_text += reverse_cipher_map[char.upper()].upper() if char.isupper() else reverse_cipher_map[char.upper()].lower()
        else:
            decrypted_text += char  # Keep spaces and special characters unchanged
    return decrypted_text

# Example key (can be any shuffled version of the alphabet)
key = "QWERTYUIOPASDFGHJKLZXCVBNM"  
cipher_map = create_cipher(key)

# Taking user input for encryption
plaintext = input("Enter the plaintext: ")
ciphertext = encrypt(plaintext, cipher_map)

print(f"Ciphertext: {ciphertext}")

# Asking user if they want to decrypt
decrypt_choice = input("Do you want to decrypt the message? (yes/no): ").strip().lower()

if decrypt_choice == "yes":
    decrypted_text = decrypt(ciphertext, cipher_map)
    print(f"Decrypted Text: {decrypted_text}")
else:
    print("Decryption skipped. Exiting program.")
