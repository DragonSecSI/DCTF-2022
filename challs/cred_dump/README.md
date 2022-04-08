## Secure Creds
flag: dctf{n0_ant1v1ru5_l0l}

### Solution
1. Its a lsass dump, which holds all credentials of the current users
2. We use mimikatz to extract the passwords
3. Disable antivirus, download mimikatz from https://github.com/gentilkiwi/mimikatz
4. Open it and `cd` to the folder with dump file
5. Use `sekurlsa::minidump lsass.DMP` to load the dump file
6. Use `sekurlsa::logonPasswords` to show passwords
7. The plaintext password should be somewhere to the top of the output
8. We get the flag dctf{n0_ant1v1ru5_l0l}