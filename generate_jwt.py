import jwt
import time

def generate_jwt():
    app_id = "907053"
    private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAwh32siKy8xi2eNhITJEegFVxM5ooFYsDbHTteLhEbjbnY1Z3
nHxSBREMRSOauDKHbU8n3BRsmhG8qMwPHgOdUjiv0Yjm0X12JG3Exa30Vajp89aj
35+KMm40Ha7ZtXQLK0UifwjJhY5stZgYrYNfzuBgyn1fCkMm7KfVNNkHTIHow6yT
yMGSgrHH2xMB/WPdmWW48ASD4dRMWWJ30HFzBp5IWnCP+/PIeozzBBlfTYolfYAV
zKmQxw4NDUJS2LpUs+TOJaBustEs4leBriw4pZLO07FEKC6n0v5PRwls9DT0t0BD
IB1xH3445zKVvqUXWRCNCQMuQa3L3igsWr0m6wIDAQABAoIBAG1HLP/vZMpRmTfC
mkDwWTlp4EZqfDJUheLimGUjZvKc2fokTUW8/vd3N28cshcL6w1wSEIvBUxeu9RS
vBfrdP86hk/xP++jL4UmfmXCnhAy/TGWHb7gM45cV9519n2eDEOZsefN7JTRLwWz
0ACuOptd2V9k4MIIN7t2aCJOIzu/0ye445DafMTge+mA/IerZ00Ic8+1muQnmD4i
WxfCPChq2pVUt+gHZOyMHw/6D5FVGcNAQg3jWbEOaxe9fZrx0uu6g6ig7V0db5MM
82d1xheXEaq0hwxh6w9dN1ubGWQgnRoM0IHdA5HWaNCUphfaF7UzOTvbb+aFCHLj
vqlpodECgYEA6UVqr7g98bZmbWAATMEMdi/IT0A5D56Ph9uU4vEHYCUCyCmCK6db
chlY1m/hVmkn5rEQjMUzWgpjH48V5p3RiADilPRMqSajRVRZlmzsThX7bC2XH0a6
UV1U8RyEgqz+dHeH0J7JsLvMgRKDRTtXVk2VxU8DDOdhC/S93f2KuHUCgYEA1Qfo
sM1t9DTvxQwBI4ClvHqsE1ph12t7hplmxI4qavU1nk3ifX/NBidav+PMkd5CVUcg
mrVL8hFcpKX04BPHTM5y2CcRT9n1Kwm8GCjxG8Z4HENjsnCRP6ZbLSwnUVasKRtc
nYjvdkqBq1kUr4eB4aJkWdmjA2e6EhTg6DsVdd8CgYEAw96Cv3tvn+ctSEek2M38
XbyvcEQX5ZKZKFVrRcdnDwbkuBeKcoc7FKpN2vjkd/8h/uXMZLcs8DzqkFQ/6n23
s4AywSoEuL91tsAl3VYmcUap72K0kxF7XtiEe1Qbu/HwUvEO/FBoQFrgU7ysttQl
+JR63ssCX7Jk3XoqdxzufwUCgYAMYMlEfKtG5UyJRolKZs86hGY7OaU1vykOSRuP
kDMmw9i5ugzO/f4LvX2oaLQaRa/VBK0AUEh5aEjZyErSOlP6QoSpyptW6HM2bPpg
7QAVfRK9kazZUXEfIatqlIY0U7TtLonTHYHMfcfLDQIGsPj7A1SRY/P03rIRGuV2
mPhGQQKBgQCjvFHL9lMu6Kg2eD0FpBbZKG5evBZR7AMWW5Um2vWoHuZOBfjaeLh9
mXXUSuS5LuO/IMhYkmsvMyMnDO8K6hgbSQ/y1pZ4XMoNl08+VE1WNqs2QNLXrbxh
i4M3BTwuCF5lGm6GimdKwNAKH3z+HJ7jwIPpFjTBeqA/Glmlizc85w==
-----END RSA PRIVATE KEY-----
"""
    payload = {
        'iat': int(time.time()),
        'exp': int(time.time()) + 600,
        'iss': app_id
    }
    jwt_token = jwt.encode(payload, private_key, algorithm='RS256')
    return jwt_token.decode('utf-8')

if __name__ == "__main__":
    print(generate_jwt())
