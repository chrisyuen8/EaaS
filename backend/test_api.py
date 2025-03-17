import requests
import json
import base64

# API Endpoints
ENCRYPT_URL = "http://localhost:8000/encrypt"
DECRYPT_URL = "http://localhost:8000/decrypt"

# Test file path
TEST_FILE = "test.txt"
DECRYPTED_FILE = "decrypted_test.txt"

# Step 1: Create a test file
with open(TEST_FILE, "w") as f:
    f.write("This is a test file for encryption and decryption.")

# Step 2: Encrypt the file
files = {'file': open(TEST_FILE, 'rb')}
encrypt_response = requests.post(ENCRYPT_URL, files=files)

if encrypt_response.status_code == 200:
    encrypted_data = encrypt_response.json()
    encrypted_text = encrypted_data["encrypted_data"]
    print("[✅] Encryption successful.")
else:
    print("[❌] Encryption failed:", encrypt_response.text)
    exit(1)

# Step 3: Decrypt the file
decrypt_payload = json.dumps({"encrypted_data": encrypted_text})
decrypt_headers = {"Content-Type": "application/json"}
decrypt_response = requests.post(DECRYPT_URL, data=decrypt_payload, headers=decrypt_headers)

if decrypt_response.status_code == 200:
    decrypted_data = decrypt_response.json()["decrypted_data"]
    with open(DECRYPTED_FILE, "w") as f:
        f.write(decrypted_data)
    print("[✅] Decryption successful.")
else:
    print("[❌] Decryption failed:", decrypt_response.text)
    exit(1)

# Step 4: Verify Integrity
with open(TEST_FILE, "r") as original, open(DECRYPTED_FILE, "r") as decrypted:
    if original.read() == decrypted.read():
        print("[✅] File integrity check passed!")
    else:
        print("[❌] File integrity check failed!")

print("✅ All tests completed successfully.")

