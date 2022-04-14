xxd -p 'nothing.jpg' |  tr -d '\n' | rev | sed 's/4030b405/P/g' | cut -d 'P' -f 1 | rev > h1.txt;
{echo "504b030"; cat h1.txt} | tr -d '\n' | sed 's/504b0301400000000/504b03041400000008/g' > h2.txt;
xxd -r -p h2.txt secret.zip;
7z e secret.zip;
cat not_important.txt | grep 'dctf{.*}' | tr -d "\t\n\r ";