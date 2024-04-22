from cryptography.fernet import Fernet
import pandas as pd
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Create a new encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Define the encryption function
def encrypt(text):
    padder = padding.PKCS7(128).padder()
    padded_text = padder.update(text.encode()) + padder.finalize()
    return cipher_suite.encrypt(padded_text).decode()

# Define the decryption function
def decrypt(text):
    padded_text = cipher_suite.decrypt(text.encode())
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded_text) + unpadder.finalize()

# Read the CSV files
data1 = pd.read_csv('Invoices.csv')
data2 = pd.read_csv('Estimates.csv')

# Encrypt the Customer column in both DataFrames
data1['Encrypted_Customer'] = data1['Customer Name'].apply(lambda x: encrypt(str(x))[:10])
data2['Encrypted_Customer'] = data2['Customer Name'].apply(lambda x: encrypt(str(x))[:10])

# Save the DataFrames with encrypted names to new CSV files
data1.to_csv('data1_encrypted.csv', index=False)
data2.to_csv('data2_encrypted.csv', index=False)