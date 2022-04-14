Intended solution

0. Unzip the `cfg.zip`
1. Read folder/file structure and notice that each folder can contain one or more folders and files.
Notice the connection between title of the challenge and context-free grammars, so that folder containing folders and 
files can be interpreted as productions. The folders are _nonterminals_, files are _terminals_.
Alternatively, interpret this as mappings. The folder maps to its contents.
2. Get these productions / mappings into text form for easier processing.
3. Simplify and reduce using rules for productions such as:
    - remove unused nonterminals (not reachable from starting point, traditionally denoted as S)
    - remove empty productions (such as A -> epsilon)
    - remove unit productions (such as A -> B)
4. Some parts are quickly guessable, others can be permuted from given letters and word lengths.