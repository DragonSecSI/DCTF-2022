## Corrupt company - intended solution

0. You are given an image file named `nothing.jpg`.
1. Using forensic tools or just looking at hex file representation, it can be seen that the file contains a zip archive.
2. Zip archive can be saved as its own file and extracted using 7zip. It complains (because the central directory record is missing) but extracts a word file containing incriminating data.
3. The word file does not contain the flag so you need to look deeper. One of the files was not extracted yet.
4. Two options: cut out the second file or fix binary of its folder (starts with `30 4B` instead of `50 4B`).
5. On extraction, a text file appears but its contents are unreadable because of compression.
6. One option is to try adding bytes that tell 7zip to decompress - in this case `08`. 
7. Then 7zip can decompress the "zip" and you get the text file, this time readable.
8. Search for flag format.
