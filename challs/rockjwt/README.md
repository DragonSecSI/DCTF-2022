## RockJWT
flag: dctf{r0cky0u_f0r_7h3_w1n}

### Solution
1. Get JWT from url
2. Look at src and see that you need `auth_level: admin`
3. Decode JWT and get rockyou.txt
4. Make python script to try all passwords in rockoyu
5. Find pass `light_dragon123`
6. Send GET request to /secret with bearer token as auth and get flag