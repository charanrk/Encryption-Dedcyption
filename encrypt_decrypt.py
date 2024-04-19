def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, key):
    return encrypt(text, -key)

def main():
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
    if choice == 'E':
        plaintext = input("Enter the plaintext to encrypt: ")
        key = int(input("Enter the key (shift value): "))
        encrypted_text = encrypt(plaintext, key)
        print("Encrypted text:", encrypted_text)
    elif choice == 'D':
        ciphertext = input("Enter the ciphertext to decrypt: ")
        key = int(input("Enter the key (shift value): "))
        decrypted_text = decrypt(ciphertext, key)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()
