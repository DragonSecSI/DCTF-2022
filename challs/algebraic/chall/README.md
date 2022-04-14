- preprocessing.py: generates fresh keys and pregenerated signatures. Run once
  if sth gets leaked
- subset\_sigs: private. contains signatures they are able to forge ( a bit
  artificial, but no other good way, sorry)
- previous\_sigs: public
- algebraic.py: public, slightly modified file 
- algebraic\_real.py: private challenge file, includes generate\_chal 
