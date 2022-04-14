file = open("seek.c", "r")
file2 = open("sol.txt", "w")

#parse the c code
i=0

for line in file:
    i+=1
    if(i>=20 and i<=746):
        #fseek(fp,540,SEEK_SET);c=fgetc(fp);if(c != 32){oops();} we parse this line for numbers(position, charr)

        position=line.split(",")[1]
        charr=line.split(";")[2][8::].split(")")[0]
        #print(charr,position)

        file2.seek(int(position),0)
        file2.write(chr(int(charr)))
        #write the char to the file to get the flag
        
    