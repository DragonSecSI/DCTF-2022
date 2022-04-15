#!/bin/sh

cd compiler
make

cd ../compiler_working
make

cd ../vm
gcc vm.c -lcrypto -o vm

../compiler_working/compiler ../program.plum bin

echo "enter in order: 1 5 0 0 8 ../flag.txt ../flag.enc"

./vm