import jwt
import time
import sys

def generate_jwt(app_id, private_key):
    payload = {
        'iat': int(time.time()),
        'exp': int(time.time()) + 600,
        'iss': app_id
    }
    jwt_token = jwt.encode(payload, private_key, algorithm='RS256')
    return jwt_token.decode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_jwt.py <app_id> <private_key>")
        sys.exit(1)

    app_id = sys.argv[1]
    private_key = sys.argv[2]
    print(generate_jwt(app_id, private_key))
