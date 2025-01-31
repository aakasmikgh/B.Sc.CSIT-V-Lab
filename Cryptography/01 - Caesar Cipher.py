import tkinter as tk
from tkinter import messagebox
 
# Caesar Cipher Encryption Function
def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - shift + key) % 26 + shift)
        else:
            ciphertext += char
    return ciphertext.upper()  # Convert the ciphertext to uppercase
 
# Caesar Cipher Decryption Function
def caesar_decrypt(ciphertext, key, original_plaintext):
    plaintext = ""
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            # Decrypt the character
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            # Restore the original case from the plaintext
            if original_plaintext[i].isupper():
                plaintext += decrypted_char.upper()
            else:
                plaintext += decrypted_char.lower()
        else:
            plaintext += char
    return plaintext
 
# Encryption Button Command
def encrypt_text():
    plaintext = plaintext_entry.get()
    key = key_entry.get()
    try:
        key = int(key)
        ciphertext = caesar_encrypt(plaintext, key)
        ciphertext_entry.delete(0, tk.END)
        ciphertext_entry.insert(0, ciphertext)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the key.")
 
# Decryption Button Command
def decrypt_text():
    ciphertext = ciphertext_entry.get()
    key = key_entry.get()
    original_plaintext = plaintext_entry.get()  # Get the original plaintext for case preservation
    try:
        key = int(key)
        regenerated_plaintext = caesar_decrypt(ciphertext, key, original_plaintext)
        regenerated_plaintext_entry.delete(0, tk.END)
        regenerated_plaintext_entry.insert(0, regenerated_plaintext)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the key.")
 
# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher GUI")
 
# Plaintext Label and Entry
plaintext_label = tk.Label(root, text="Plaintext:")
plaintext_label.grid(row=0, column=0, padx=10, pady=10)
plaintext_entry = tk.Entry(root, width=30)
plaintext_entry.grid(row=0, column=1, padx=10, pady=10)
plaintext_entry.insert(0, "hello")
 
# Key Label and Entry
key_label = tk.Label(root, text="Key:")
key_label.grid(row=1, column=0, padx=10, pady=10)
key_entry = tk.Entry(root, width=30)
key_entry.grid(row=1, column=1, padx=10, pady=10)
key_entry.insert(0, "3")
 
# Ciphertext Label and Entry
ciphertext_label = tk.Label(root, text="Ciphertext:")
ciphertext_label.grid(row=2, column=0, padx=10, pady=10)
ciphertext_entry = tk.Entry(root, width=30)
ciphertext_entry.grid(row=2, column=1, padx=10, pady=10)
 
# Regenerated Plaintext Label and Entry
regenerated_plaintext_label = tk.Label(root, text="Regenerated Plaintext:")
regenerated_plaintext_label.grid(row=3, column=0, padx=10, pady=10)
regenerated_plaintext_entry = tk.Entry(root, width=30)
regenerated_plaintext_entry.grid(row=3, column=1, padx=10, pady=10)
 
# Encrypt Button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=4, column=0, padx=10, pady=10)
 
# Decrypt Button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=4, column=1, padx=10, pady=10)
 
# Run the GUI
root.mainloop()