import argparse
import base64
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


# Function to encrypt plaintext
def encrypt(plaintext, key):
    # Convert key and plaintext to bytes (computers work with bytes)
    key_bytes = key.encode('utf-8')
    plaintext_bytes = plaintext.encode('utf-8')

    # Check if key is the right length (16, 24, or 32 bytes for AES)
    if len(key_bytes) not in [16, 24, 32]:
        raise ValueError("Key must be 16, 24, or 32 characters long.")

    # Generate a random IV (Initialization Vector) - makes encryption safer
    iv = os.urandom(16)

    # Pad the plaintext so it's the right size for AES (using PKCS7 padding)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext_bytes) + padder.finalize()

    # Set up the AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the padded data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Combine IV and ciphertext, then encode to Base64 (easy to store/send)
    iv_and_ciphertext = iv + ciphertext
    base64_output = base64.b64encode(iv_and_ciphertext).decode('utf-8')

    return base64_output


# Function to decrypt ciphertext
def decrypt(ciphertext_base64, key):
    # Convert key to bytes
    key_bytes = key.encode('utf-8')

    # Check key length
    if len(key_bytes) not in [16, 24, 32]:
        raise ValueError("Key must be 16, 24, or 32 characters long.")

    iv_and_ciphertext = base64.b64decode(ciphertext_base64)
    iv = iv_and_ciphertext[:16]
    ciphertext = iv_and_ciphertext[16:]

    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    # Decrypt the data
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext_bytes = unpadder.update(padded_data) + unpadder.finalize()

    plaintext = plaintext_bytes.decode('utf-8')

    return plaintext
def main():
    parser = argparse.ArgumentParser(description="Simple AES Encryption/Decryption Tool")
    parser.add_argument("text", nargs="?", help="The plaintext (for encrypt) or Base64 ciphertext (for decrypt)")
    parser.add_argument("--key", default="your secret key", help="The secret key (default: 'ThisIsA16CharKey')")
    parser.add_argument("--mode", choices=["encrypt", "decrypt"], default="encrypt",
                        help="Mode: 'encrypt' or 'decrypt' (default: encrypt)")

    args = parser.parse_args()

    if args.text is None:
        import sys
        args.text = sys.stdin.read().strip()

    if args.mode == "encrypt":
        encrypted = encrypt(args.text, args.key)
        print("Encrypted Text (Base64):", encrypted)
    elif args.mode == "decrypt":
        decrypted = decrypt(args.text, args.key)
        print("Decrypted Text:", decrypted)

if __name__ == "__main__":
    main()