## RockJWT
flag: dctf{n0t_th4t_s3cr3t_1s_1t}

### Solution
1. Download volatility3 from https://github.com/volatilityfoundation/volatility3
2. Run command `python3 volatility3/vol.py -f MEMORY.DMP windows.filescan.FileScan > filescan.txt`
3. In `filescan.txt` search for the `secret.txt` file, it should be on Desktop, copy its address
4. Use command `python3 volatility3/vol.py -f MEMORY.DMP windows.dumpfiles.DumpFiles --virtaddr 0xa881f76be300` to extract the file
5. `cat <extracted_file>` and you get the b64 encoded flag
6. Decode it `echo ZGN0ZntuMHRfdGg0dF9zM2NyM3RfMXNfMXR9 | base64 -d`
7. You have the flag dctf{n0t_th4t_s3cr3t_1s_1t}