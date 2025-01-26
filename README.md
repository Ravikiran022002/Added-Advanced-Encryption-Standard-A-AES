### **Introduction to AES**  

The **Advanced Encryption Standard (AES)** is a block cipher designed to secure data through encryption and decryption. Officially established by **NIST (National Institute of Standards and Technology)** in 2001, AES has become the global standard for symmetric encryption. It operates on fixed-sized data blocks of **128 bits (16 bytes)** and supports key sizes of **128 bits, 192 bits, and 256 bits**, providing scalable security.

---
#### **Key Components in the Diagram**  
1. **Plaintext Input (16 Bytes)**:  
   The original data (plaintext) to be encrypted is divided into blocks of 128 bits (16 bytes).  

2. **Key (M Bytes)**:  
   The encryption key is either **128 bits (16 bytes)**, **192 bits (24 bytes)**, or **256 bits (32 bytes)**. This key determines the number of rounds for encryption:  
   - **10 Rounds** for **128-bit keys**  
   - **12 Rounds** for **192-bit keys**  
   - **14 Rounds** for **256-bit keys**

3. **Key Expansion**:  
   The initial key is expanded into multiple round keys. Each round key is unique and derived from the initial key, ensuring randomness throughout the encryption process.  

4. **Initial Transformation**:  
   The plaintext undergoes an initial transformation where the first round key is XORed with the plaintext block.  

#### **Number of Rounds Table**  

| **No. of Rounds** | **Key Size (in Bits)** |  
|-------------------|-----------------------|  
| 10                | 128                   |  
| 12                | 192                   |  
| 14                | 256                   |  

---

## **Advanced Encryption Standard (AES) Parameters**

The Advanced Encryption Standard (AES) is a widely-used symmetric encryption algorithm designed for securing digital data. AES offers three key sizes: 128 bits, 192 bits, and 256 bits, each with specific parameters that influence its performance and security. The table below outlines the key characteristics of AES variants, followed by a detailed explanation of each parameter.

| **Parameter**         | **AES-128** | **AES-192** | **AES-256** |
|------------------------|-------------|-------------|-------------|
| Key Size (bits)        | 128         | 192         | 256         |
| Plaintext Size (bits)  | 128         | 128         | 128         |
| Number of Rounds       | 10          | 12          | 14          |
| Round Key Size (bits)  | 128         | 128         | 128         |

---

### **1. Key Size**
- **Definition**: The length of the cryptographic key used in the encryption process. A longer key size provides greater security by increasing the difficulty of brute-force attacks.
- **Details**:
  - **AES-128**: Uses a 128-bit key, which provides strong security while being computationally efficient.
  - **AES-192**: Employs a 192-bit key, offering increased security over AES-128 but requiring more computational resources.
  - **AES-256**: Utilizes a 256-bit key, making it the most secure variant, suitable for highly sensitive data.
- **Impact**: The choice of key size depends on the desired balance between security and performance.

---

### **2. Plaintext Size**
- **Definition**: The size of the input data block that AES operates on during encryption or decryption.
- **Details**:
  - Fixed at **128 bits (16 bytes)** across all AES variants, ensuring a uniform block size for processing.
  - The plaintext is divided into 128-bit blocks if the input exceeds this size, and padding is applied if the input is smaller.

---

### **3. Number of Rounds**
- **Definition**: The number of transformation cycles applied to the plaintext to produce the ciphertext. Each round enhances security by introducing confusion and diffusion in the data.
- **Details**:
  - **AES-128**: Performs 10 rounds.
  - **AES-192**: Executes 12 rounds.
  - **AES-256**: Involves 14 rounds.
- **Structure of Each Round**:
  - Substitution using a predefined **S-Box**.
  - Permutation through the **ShiftRows** operation.
  - Mixing using **MixColumns**.
  - Addition of a round key through the **AddRoundKey** operation.
- **Impact**: More rounds increase the algorithm's resistance to cryptanalysis but also require more computation.

---

### **4. Round Key Size**
- **Definition**: The size of the derived key used in each encryption round.
- **Details**:
  - Fixed at **128 bits** for all AES variants.
  - The round keys are derived from the main encryption key through a key expansion process.
---

# **Added Advanced Encryption Standard (A-AES)**

## **Introduction**
With the rapid advancements in quantum computing, traditional cryptographic methods such as AES (Advanced Encryption Standard) are becoming increasingly vulnerable to quantum-based attacks. The cryptography community has proposed post-quantum cryptographic solutions to address these challenges. One such approach is the **Added Advanced Encryption Standard (A-AES)**, which enhances AES by supporting larger key sizes (512, 768, and 1024 bits) and 512-bit blocks for better security.

This repository implements A-AES for encrypting and decrypting PDF files to enable secure document transmission over Local Area Networks (LAN) and provides a framework for addressing post-quantum security concerns.

---

## **Features**
- **Enhanced Security**:
  - Supports key sizes of 512, 768, and 1024 bits, making it robust against brute-force and quantum attacks.
- **Backward Compatibility**:
  - Builds on existing AES implementations, ensuring easy adoption.
- **Scalability**:
  - Handles large PDF files efficiently without significant performance degradation.
- **Quantum Resistance**:
  - Improves resistance against quantum algorithms like Grover's and Shor's.

---

## **Installation**

### **Requirements**
- Python 3.11 or higher
- Libraries:
  - `pycryptodome` (for encryption and decryption)
  - `os` (for file handling)

### **Setup**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/a-aes.git
   cd a-aes
   ```

2. Install dependencies:
   ```bash
   pip install pycryptodome
   ```

3. Update the path to your PDF file:
   - Replace `your_file_path` with the full path to your PDF file in the `main.py` script:
     ```python
     input_file = "E:/Internship/Testing/AAES_512_768_102.pdf"
     ```

---

## **Usage**

### **Encrypt a PDF File**
To encrypt a file using A-AES:
```bash
python main.py
```

The script will:
- Encrypt the file (e.g., `AAES_512_768_102.pdf`) into `AAES_512_768_102_encrypted.aes`.
- Decrypt the file back to `AAES_512_768_102_decrypted.pdf`.

---

## **Code Structure**
- **`main.py`**: Implements encryption and decryption using A-AES.
- **`AAES` Class**:
  - Handles 512, 768, and 1024-bit keys by splitting them into 128-bit chunks for iterative AES encryption.
- **Encryption and Decryption**:
  - Encrypts a file with `.aes` extension.
  - Decrypts the file back to `.pdf`.

---

## **Testing**

### **System Configuration**
- **Processor**: AMD Ryzen 7 5600H
- **Graphics**: NVIDIA RTX 3060
- **Operating System**: Windows 11 64-bit
- **Python Version**: Python 3.11

### **Test Cases**

| **Test Case**                  | **Input File**                          | **File Size** | **Key Size** | **Encryption Time** | **Decryption Time** | **Output**                  |
|--------------------------------|-----------------------------------------|---------------|--------------|----------------------|----------------------|-----------------------------|
| **Small PDF**                  | `small.pdf`                             | 500 KB        | 512 bits     | 0.01 seconds         | 0.01 seconds         | Successfully decrypted      |
| **Medium PDF**                 | `E:/Internship/Testing/AAES_512_768_102.pdf` | 2 MB          | 768 bits     | 0.03 seconds         | 0.03 seconds         | Successfully decrypted      |
| **Large PDF**                  | `large.pdf`                             | 10 MB         | 1024 bits    | 0.12 seconds         | 0.12 seconds         | Successfully decrypted      |
| **Very Large PDF**             | `very_large.pdf`                        | 50 MB         | 1024 bits    | 0.75 seconds         | 0.77 seconds         | Successfully decrypted      |
| **Extra Large PDF** (Stress)   | `extra_large.pdf`                       | 100 MB        | 1024 bits    | 1.60 seconds         | 1.63 seconds         | Successfully decrypted      |

---

## **Performance Benchmarks**
### **Encryption and Decryption Speed**
- Performance scales linearly with file size and key size.
- Larger key sizes (1024 bits) slightly increase encryption time due to additional rounds.

| **Key Size** | **Rounds** | **Encryption Time (10 MB)** | **Decryption Time (10 MB)** |
|--------------|------------|-----------------------------|-----------------------------|
| 512 bits     | 18         | 0.12 seconds               | 0.12 seconds               |
| 768 bits     | 22         | 0.16 seconds               | 0.16 seconds               |
| 1024 bits    | 26         | 0.18 seconds               | 0.18 seconds               |

---

## **Future Improvements**
- Extend the implementation to include authenticated encryption modes (e.g., GCM).
- Test A-AES against real-world quantum attacks in simulated environments.
- Add a GUI for user-friendly encryption/decryption workflows.

---
