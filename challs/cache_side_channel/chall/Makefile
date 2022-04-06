# https://www.cprogramming.com/tutorial/shared-libraries-linux-gcc.html
# 

crypto: crypto.c
	gcc -c -Wall -Werror -fpic crypto.c -falign-functions=4096
	gcc -shared -o libcrypto.so crypto.o -lsodium

host: host.c libcrypto.so
	gcc -L$(shell pwd) -Wall -o host host.c -lcrypto -lsodium -lrt

attacker-comp: attacker.c
	gcc -c -Wall attacker.c -lsodium

attacker-link: attacker.o libcrypto.so
	gcc -L$(shell pwd) -Wall -o attacker attacker.o -lcrypto -lrt