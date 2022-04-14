import itertools
import string
from random import shuffle, randint, sample, choice

alphabet = string.ascii_lowercase + string.digits + "{_}"
epsilon = 'eps'

score_dict = {**{epsilon: 0},
              **{a: 1 for a in alphabet},
              **{b: 2 for b in string.ascii_uppercase if b != 'S'},
              **{'S': 3}}

class Grammar():
    def __init__(self, grammar_file):
        self.terminals = alphabet
        self.productions = {}
        self.strings = []

        self.parse(grammar_file)

    def print_productions(self):
        for s, m in self.productions.items():
            print(s, '->', "|".join(m))

    def parse(self, grammar_file):
        with open(grammar_file, "r") as f:
            for line in f:
                p = get_production(line)
                self.add_production(p)

    def add_production(self, p):
        s, m = p
        if s in self.productions.keys():
            self.productions[s] += m
        else:
            self.productions[s] = m

    def get_nonterminals(self):
        return set([s for s in self.productions.keys()] +
                   [y for m in self.productions.values() for x in m for y in x.split(" ") if x.isupper()])

    def get_terminals(self):
        return set([y for m in self.productions.values() for x in m for y in x.split(" ") if x in alphabet])

    def get_last_nonterminal(self):
        key = lambda x: sum([10**i * ord(c) for i, c in enumerate(x[::-1])])
        return sorted(list(self.get_nonterminals()), key=key)[-1]

    def execute_productions(self):
        new_strings = []

        if self.strings:
            for s in self.strings:
                for p in self.productions:
                    if p.symbol in s:
                        new_strings += self.use_mapping(s, p.symbol, p.mappings)
        else:
            for p in self.productions:
                if p.symbol == 'S':
                    new_strings += self.use_mapping('S', p.symbol, p.mappings)


        self.strings += new_strings

    def use_mapping(self, s, symbol, mapping):
        new_strings = []
        for m in mapping:
            new_s = s[:].replace(symbol, m, 1)
            new_strings.append(new_s)
        return new_strings

    def find_strings(self):
        return [s.replace(' ', '') for s in self.strings if s.islower()]

    def replace_terminals(self):
        new_productions = []
        last_nonterminal = self.get_last_nonterminal()
        nt = next_nonterminal(last_nonterminal)

        for s, ms in self.productions.items():
            p = ms[:]

            if any(x.islower for x in p):
                for c in p:
                    production = get_production("", nonterminal=nt, mappings=[c])
                    new_productions.append(production)
                    nt = next_nonterminal(nt)

                    production = get_production("", nonterminal=nt, mappings=[p[0].replace('c', nt)])
                    new_productions.append(production)
                    nt = next_nonterminal(nt)

            else:
                new_productions.append(p)

        self.productions = dict(new_productions)

    def reduce_mappings(self):
        new_productions = []
        last_nonterminal = self.get_last_nonterminal()
        nt = next_nonterminal(last_nonterminal)

        for s, ms in self.productions.items():
            if s == 'S':
                continue

            p = ms[:]

            while len(p) > 1:
                production = get_production("", nonterminal=nt, mappings=p[:2])
                new_productions.append(production)

                p = p[2:]
                nt = next_nonterminal(nt)

            if len(p) > 0:
                production = get_production("", nonterminal=nt, mappings=p)
                new_productions.append(production)
                nt = next_nonterminal(nt)

        self.productions = {**self.productions, **dict(new_productions)}

    def simplify(self):
        self.remove_unused_nonterminals()
        self.remove_empty_productions()
        self.remove_unit_productions()
        self.remove_unused_nonterminals()

    def remove_unit_productions(self):
        while self.contains_unit_productions():

            for s, m in list(self.productions.items())[::-1]:
                for mi in m:

                    # unit production
                    if mi.count(" ") == 0 and mi.isupper():
                        s_remove = mi

                        # replace with what s_remove maps to
                        replace_with = self.productions[s_remove]
                        new_mappings = self.productions[s]

                        for mapping in replace_with:
                            for x in new_mappings[::-1]:
                                if s_remove in x:
                                    new_mappings.remove(x)
                                    new_mappings.append(x.replace(s_remove, mapping))

                        self.productions[s] = list(set(new_mappings))

    def contains_unit_productions(self):
        for s, m in self.productions.items():
            for x in m:
                if x.count(" ") == 0 and x.isupper():
                    return True
        return False

    def remove_unused_nonterminals(self):
        used_terminals = set('S')
        all_terminals = self.get_nonterminals()
        nonvisited = self.productions.copy()
        n_nonvisited_prev = len(nonvisited) + 1

        while nonvisited and len(nonvisited) < n_nonvisited_prev:
            n_nonvisited_prev = len(nonvisited)

            for t in used_terminals:
                if t in nonvisited.keys():
                    mappings = nonvisited.pop(t)
                    terminals = [x for m in mappings for x in m.split(" ") if x.isupper()]
                    used_terminals = used_terminals.union(set(terminals))

        unused_terminals = all_terminals.difference(used_terminals)

        if nonvisited:
            unused_terminals = unused_terminals.union(set(nonvisited.keys()))

        for t in unused_terminals:
            try:
                del self.productions[t]
            except Exception:
                pass

    def remove_empty_productions(self):
        for t in self.productions.keys():
            if "|".join(self.productions[t]) == epsilon:
                del self.productions[t]

    @staticmethod
    def remove_loops(productions):
        for s, m in productions:
            if s == "|".join(m):
                del productions[s]

    def merge_productions(self):
        new_productions = {}

        for s1, m1 in self.productions.items():

            if s1 in new_productions.keys():
                new_productions[s1] += m1
            else:
                new_productions[s1] = m1

        self.productions = dict([get_production("", nonterminal=s, mappings=m) for s, m in new_productions.items()])

    def remove_duplicates(self):
        new_productions = list(self.productions.items())

        for s1, m1 in self.productions.items():
            for s2, m2 in self.productions:

                # A -> x and B -> x will be reduced to A -> x
                if s1 != s2 and m1 == m2:
                    for p in new_productions[::-1]:
                        if p.symbol == 'S':
                            continue
                        if p.symbol == s2:
                            if p.mappings == m2:
                                new_productions.remove(p)
                            else:
                                p.symbol = s1
                        p.mappings = list(set([m.replace(s2, s1) for m in p.mappings]))

            self.remove_loops(new_productions)

            for s, m in new_productions:
                print(s, '->', "|".join(m))
            print("")

        self.productions = dict(new_productions)

    def add_useless_productions(self, n=1000):
        nt = self.get_last_nonterminal()
        nts = []
        for _ in range(n):
            nt = next_nonterminal(nt)
            nts.append(nt)

        letters = set(alphabet).difference(set(self.get_terminals()))

        for x in nts:
            if randint(0, 5) == 0:
                production = get_production("", nonterminal=x, mappings=sample(nts, randint(1,15)))
                self.add_production(production)

        for y in letters:
            for x in nts:
                if randint(0, 25) == 0:
                    production = get_production("", nonterminal=x, mappings=[y])
                    self.add_production(production)


    def scramble_nonterminals(self):
        nonterminals = self.get_nonterminals()
        nonterminals.remove('S')

        shuffled_nonterminals = list(nonterminals)
        shuffle(shuffled_nonterminals)

        mapping = {x: y for x, y in zip(nonterminals, shuffled_nonterminals)}
        mapping['S'] = 'S'
        new_productions = []

        for s, ms in self.productions.items():
            new_mappings = [" ".join([mapping[x] if x not in alphabet else x for x in m.split(" ")]) for m in ms]
            new_production = get_production("", nonterminal=mapping[s], mappings=new_mappings)
            new_productions.append(new_production)

        self.productions = dict(new_productions)

    def get_flag(self, ns=[0,0,7,0,4,0,2,0,3,0,7,0,4,0]):
        flag_mappings = self.productions['S']
        print(flag_mappings)

        print("Obviously the first part translates to dctf")
        print("Similarly every second and last to {_}\n")
        print("The only thing left is to permutate possibilites for flag parts")

        for n, field in zip(ns, flag_mappings[0].split(" ")):
            if n==0:
                pass
            else:
                ms = self.productions[field][0].split(" ")
                if field in ms:
                    ms.remove(field)
                m = ms[0]
                chars = self.productions[m]
                options = itertools.product(chars, repeat=n)
                for o in options:
                    x = "".join(o)
                    if x in "c0nt3xt_fR33_15_n07_m34n1ng_fr33":
                        print(x)

def next_nonterminal(nonterminal):
    nt = nonterminal[:]

    # skip 'S' which is the starting symbol
    if nt == 'R':
        return 'T'

    elif nt[-1] != 'Z':
        nt = nt[:-1] + chr(ord(nt[-1]) + 1)
        return nt

    elif len(nt) > 1:
        return next_nonterminal(nt[:-1]) + 'A'

    else:
        return 'AA'

def get_production(string_production, nonterminal=None, mappings=[]):
    if string_production:
        left, right = string_production.split("->")
        nonterminal = left.strip()
        mappings = list(set([m.strip() if m.strip() else '' for m in right.split("|")]))
        return nonterminal, mappings
    else:
        return nonterminal, mappings


grammar = Grammar("chall/cfg.txt")
#grammar.reduce_mappings()
#grammar.add_useless_productions()
#grammar.scramble_nonterminals()
grammar.simplify()
#grammar.print_productions()
grammar.get_flag()
