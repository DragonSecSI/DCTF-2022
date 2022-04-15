# Problem Description
Naor-Reingold PRF's are a generic tool for computing a PRF on $n$ bits of
input [b1,...,bn]: 
one takes $n+1$ group elements as keys [k0,...,kn] input and uses the group operation x to compute: 
k0 x k1^b1 x ... x kn^bn. The ^bi just means that the group action is applied
iff the i-th bit of the input is 1. 
The PRF omits always adding the additional key element k0, which is why the
exploit works. 

One gets 20-sth strings and have to compute a valid signature for one of them. 

# Intuition
The PRF is algebraic: given the string/signature pairs for the strings 1001 and 0010, you can compute 1011 by applying the group action aka adding the two signatures which are just points on the curve

# Solution
Iterate over each to-sign string and combine all signatures (two) to check if
maybe one is good. 

# Hint \#1
I made sure in every generator function there is (at least) one combinable
element. 

# Hint \#2
There are five different combinable elements which may frustrate the challenge
operators, but this is just so they don't just copy/paste (ish). We could turn
up the sleep parameter. 

# Note from the author
You always add k0, which is a mitigation against this "attack" which is really
just the group action without nice trapdoor applied. The challenge
itself is probably just to understand NR PRF's and group actions, idk. I chose
EC as it is somewhat straightforward but also gives ppl the opportunity to
think about curves. Also the brute forcing is trival(ish, still depth-three
loop for the naive solution)
