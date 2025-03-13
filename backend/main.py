from fastapi import FastAPI, UploadFile, File
from cryptography.fernet import Fernet

app = FastAPI()
key = Fernet.generate_key()
cipher = Fernet(key)

@app.post("/encrypt")
async def encrypt_file(file: UploadFile = File(...)):
    content = await file.read()
    encrypted_data = cipher.encrypt(content)
    return {"filename": file.filename, "encrypted_data": encrypted_data.decode()}
