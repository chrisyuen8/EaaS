from fastapi import FastAPI, File, UploadFile
import base64

app = FastAPI()

@app.post("/encrypt")
async def encrypt_file(file: UploadFile = File(...)):
    file_content = await file.read()
    encrypted_data = base64.b64encode(file_content).decode("utf-8")
    return {"filename": file.filename, "encrypted_data": encrypted_data}

@app.post("/decrypt")
async def decrypt_data(encrypted_data: str):
    decrypted_content = base64.b64decode(encrypted_data.encode("utf-8")).decode("utf-8")
    return {"decrypted_data": decrypted_content}

import os
from fastapi.responses import FileResponse

UPLOAD_DIR = "encrypted_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/encrypt")
async def encrypt_file(file: UploadFile = File(...)):
    file_content = await file.read()
    encrypted_data = base64.b64encode(file_content).decode("utf-8")
    
    # Save to a file
    encrypted_file_path = os.path.join(UPLOAD_DIR, f"{file.filename}.enc")
    with open(encrypted_file_path, "w") as enc_file:
        enc_file.write(encrypted_data)

    return {"filename": file.filename, "encrypted_file": encrypted_file_path}

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/octet-stream", filename=filename)
    return {"error": "File not found"}
