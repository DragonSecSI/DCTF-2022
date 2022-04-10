from random import randrange

wordlist="" 
with open("wordlist.txt", "r") as f: 
    wordlist=f.readlines()

def genWord(): 
    word=""
    for i in range(4): 
        word+=wordlist[randrange(0,len(wordlist))].strip()
    return word

if __name__=="__main__": 
    word=genWord()
    encrypted="0 "
    previous=ord(word[0])
    for i in word[1:]: 
        distance=ord(i)-previous
        if distance > 14: 
            distance -=26
        if distance < -14: 
            distance +=26
        encrypted+=str(distance) + " "
        previous=ord(i)

    print("This is the encrypted password: " + encrypted + ". ")
    print("Can you decrypt it?")
    password=input("Enter password: ")
    flag="dctf{RelativeDistanceCoolEncoding}"
    if password.strip()==word: 
       print("Congrats")
       print(flag)
