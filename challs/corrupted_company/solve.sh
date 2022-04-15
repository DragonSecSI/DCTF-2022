xxd -p 'nothing.jpg' |  tr -d '\n' | rev | sed 's/4030b405/P/g' | cut -d 'P' -f 1 | rev > h1.txt;
echo -n "504b030" > h2.txt;
cat h1.txt | tr -d '\n' >> h2.txt;
cat h2.txt|  tr -d '\r\n' | sed 's/504b0301400000000/504b03041400000008/g' > h3.txt;
xxd -r -p h3.txt secret.zip;
7z e secret.zip;
cat not_important.txt | grep 'dctf{.*}' | tr -d "\t\n\r ";