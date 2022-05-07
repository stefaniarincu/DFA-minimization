from collections import defaultdict

class DFA(object):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.states = [x for x in f.readline()[:-1].split()]
            self.values = [x for x in f.readline()[:-1].split()]
            self.start_state = f.readline()[:-1]
            self.final_states = [x for x in f.readline()[:-1].split()]

            self.nr_muchii = int(f.readline())
            self.transitions = {}

            for i in range(0, self.nr_muchii):
                current_state, val, next_state = f.readline().split()
                if current_state not in self.transitions:
                    self.transitions[current_state] = {}
                self.transitions[current_state][val] = next_state

            self.part = [self.final_states]

            self.part.append([x for x in self.states if x not in self.final_states])

    def remove(self):
        g = defaultdict(list)
        for k, v in self.transitions.items():
            g[k[0]].append(v)
        stack = [self.start_state]
        reachable_states = set()

        while stack:
            state = stack.pop()

            if state not in reachable_states:
                stack += g[state]

            reachable_states.add(state)

        self.states = [state for state in self.states if state in reachable_states]

        self.final_states = [state for state in self.final_states if state in reachable_states]

        self.transitions = {(k[0], k[1]): v for k, v in self.transitions.items() if k[0] in reachable_states}

    def minimize(self):
        index = {}
        for stare in self.part[1]:
            index[stare] = 1

        for stare in self.part[0]:
            index[stare] = 0

        while True:
            dim = len(self.part)
            for mult in self.part:
                if len(mult) > 1:
                    mark = {}
                    for val in self.values:
                        mark[val] = index[self.transitions[mult[0]][val]]
                    for st in mult[1:]:
                        for val in self.values:
                            dest = self.transitions[st][val]
                            if index[dest] != mark[val]:
                                index[st] = dim
                                mult.remove(st)
                                if len(self.part) == dim:
                                    self.part.append([st])
                                else:
                                    self.part[-1] += st
                                break
            if dim == len(self.part):
                break

        self.states = [",".join(sorted(m)) for m in self.part]

        trans = {}
        for stare in self.part:
            for val in self.values:
                if self.states[index[stare[0]]] not in trans:
                    trans[self.states[index[stare[0]]]] = {}
                trans[self.states[index[stare[0]]]][val] = self.states[index[self.transitions[stare[0]][val]]]

        self.transitions = trans
        self.start_state = self.states[index[self.start_state]]

        fin = self.states[index[self.final_states[0]]]
        self.final_states = fin
        print(f'Noua stare initiala este: {self.start_state}')
        print(f'Noua stare finala este: {self.final_states}')
        print(f'Noul automat are: {len(self.states)} stari')


filename = 'int'
dfa = DFA(filename)
print("Inainte de minimizare:")
for key in dfa.transitions:
    for sec_key in dfa.transitions[key]:
        print(f'{key} -- {sec_key} --> {dfa.transitions[key][sec_key]}')

print("Dupa minimizare:")
dfa.minimize()
for key in dfa.transitions:
    for sec_key in dfa.transitions[key]:
        print(f'{key} -- {sec_key} --> {dfa.transitions[key][sec_key]}')

