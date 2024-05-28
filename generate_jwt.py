import jwt
import time

def generate_jwt():
    app_id = "907053"
    private_key = "fRUZIdvwPQXGbwd20ghmrQmvtkzEcILB6XGUVoIZuiA"
    payload = {
        'iat': int(time.time()),
        'exp': int(time.time()) + 600,
        'iss': app_id
    }
    jwt_token = jwt.encode(payload, private_key, algorithm='RS256')
    return jwt_token.decode('utf-8')

if __name__ == "__main__":
    print(generate_jwt())
