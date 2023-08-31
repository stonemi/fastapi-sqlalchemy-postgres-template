from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic
import secrets

security = HTTPBasic()

def validate_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    # encode the credentials to compare
    input_user_name = credentials.username.encode("utf-8")
    input_password = credentials.password.encode("utf-8")

    # DO NOT STORE passwords in plain text. Store them in secure location like vaults or database after encryption.
    # This is just shown for educational purposes
    stored_username = bytearray('test', encoding='utf-8')
    stored_password = bytearray('test', encoding='utf-8')

    is_username = secrets.compare_digest(input_user_name, stored_username)
    is_password = secrets.compare_digest(input_password, stored_password)

    if is_username and is_password:
        return {"auth message": "authentication successful"}

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid credentials",
                        headers={"WWW-Authenticate": "Basic"})