from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os


class AAES:
    def __init__(self, key):
        if len(key) not in [64, 96, 128]:  # Ensure the key is 512, 768, or 1024 bits
            raise ValueError("Key size must be 512, 768, or 1024 bits.")
        self.key = key

    def encrypt(self, plaintext):
        # Split the key into 16-byte chunks and apply AES encryption iteratively
        ciphertext = plaintext
        for i in range(0, len(self.key), 16):
            chunk_key = self.key[i:i + 16]
            cipher = AES.new(chunk_key, AES.MODE_ECB)
            ciphertext = cipher.encrypt(ciphertext)
        return ciphertext

    def decrypt(self, ciphertext):
        # Split the key into 16-byte chunks and apply AES decryption in reverse order
        plaintext = ciphertext
        for i in range(len(self.key) - 16, -1, -16):
            chunk_key = self.key[i:i + 16]
            cipher = AES.new(chunk_key, AES.MODE_ECB)
            plaintext = cipher.decrypt(plaintext)
        return plaintext


def encrypt_file(file_path, key):
    with open(file_path, "rb") as f:
        plaintext = f.read()

    # Pad the plaintext to match 512-bit blocks
    padded_plaintext = pad(plaintext, 64)

    # Encrypt the data
    aaes = AAES(key)
    encrypted_data = aaes.encrypt(padded_plaintext)

    # Save the encrypted file
    encrypted_file_path = file_path.replace(".pdf", "_encrypted.aes")
    with open(encrypted_file_path, "wb") as f:
        f.write(encrypted_data)

    print(f"File encrypted successfully: {encrypted_file_path}")


def decrypt_file(file_path, key):
    with open(file_path, "rb") as f:
        encrypted_data = f.read()

    # Decrypt the data
    aaes = AAES(key)
    decrypted_data = aaes.decrypt(encrypted_data)

    # Unpad the plaintext
    plaintext = unpad(decrypted_data, 64)

    # Save the decrypted file
    decrypted_file_path = file_path.replace("_encrypted.aes", "_decrypted.pdf")
    with open(decrypted_file_path, "wb") as f:
        f.write(plaintext)

    print(f"File decrypted successfully: {decrypted_file_path}")

if __name__ == "__main__":
    # Generate a 512-bit key (64 bytes)
    key = os.urandom(64)
    input_file = "E:/Internship/Testing/AAES_512_768_1024.pdf"

    # Encrypt and decrypt the file
    encrypt_file(input_file, key)
    decrypt_file(input_file.replace(".pdf", "_encrypted.aes"), key)
