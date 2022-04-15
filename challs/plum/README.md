Need to either patch the compiler or the binary it outputs. The bin file needs to be identical to the one that the working compiler outputs -> hashes match.
Then you compile the program.plum file and run it with the vm to decrypt the flag.
# Fixes to the compiler:
- registers are off by one, need to decrement them all
- division: left and right operand are swapped
- substraction op adds garbage print ops, need to remove those
- remove fake flag garbage ops next to print op
- lte, gte ops are swapped, need to swap them back
- string constants are not null terminated -> they should be