## Unauthorized Access
flag: dctf{dragons}

### Solution
1. We need to find the USB device that is not present in the auth.json
2. Since only serial numbers are unique for each device we compare those
3. One stands out (use py script to check each if it is in auth.json) -> use check.py
4. Copy serial into google and md5 reverse search it
5. We get "dragons", input this into dctf{} and you get the flag