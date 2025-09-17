# Simple Encryptor
# Simple Encryptor CTF Challenge

## Overview
This CTF challenge provides an encrypted file flag.enc created by a simple custom encryptor.  
The goal is to reverse the encryption and recover the original plaintext (the flag).  

## though process
Decomping the encrypt executable provides the functions used for encryption


The encryptor is intentionally simple and demonstrates common mistakes in weak encryption, such as:  
- Using srand(time()) for randomness (predictable seeds)  
- Using the standard libc rand() function (not cryptographically secure)  
- Storing the seed in plaintext within the encrypted file  

Understanding this file format and the encryption logic allows straightforward decryption.

---

## File Format
- **First 4 bytes (little-endian):** Seed used to initialize srand() 
- **Remaining bytes:** Ciphertext  

---

## Encryption Algorithm
For each byte in the plaintext:

r1 = rand() & 0xff
r2 = rand() & 7
c = rol((plaintext_byte ^ r1) & 0xff, r2)

markdown
Copy code

- r1 and r2 are pseudo-random values generated using libc rand().  
- rol is a left-rotate by r2 bits.  

---

## Decryption Algorithm
To recover the original plaintext:

1. Read the 4-byte seed from the beginning of flag.enc.  
2. Initialize the libc RNG with srand(seed).  
3. For each ciphertext byte c:
r1 = rand() & 0xff
r2 = rand() & 7
plaintext_byte = ror(c, r2) ^ r1

##this can be automated by python scipt which is provided.
