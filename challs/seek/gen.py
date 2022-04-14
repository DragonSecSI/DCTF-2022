file = open("flag.txt", "r")


i=0
j=0

for line in file:
    for character in line:
        #print("%c %d %d" % (character,i,j))
        print("fseek(fp,{i},SEEK_SET);".format(i=i)+"c=fgetc(fp);" +"if(c != {c}){{oops();}}".format(c=ord(character)))
        i+=1
            
        
