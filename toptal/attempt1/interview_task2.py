def findWord(rules):
    # map of char -> node
    rules_map = {
        # letter : rule
    }

    preceding_map = {}

    letters = set()

    for rule in rules:
        a, b = rule.split('>')
        letters.add(a)
        letters.add(b)
        rules_map[a] = b
        preceding_map[b] = a

    first = None

    print(f'preceding: {preceding_map}')

    for l in letters:
        if l not in preceding_map:
            first = l
            break

    word = first
    curr = first
    while curr in rules_map:
        word += rules_map[curr]
        curr = rules_map[curr]

    return word

print(findWord(["P>E","E>R","R>U"]))
res = findWord(["I>N","A>I","P>A","S>P"])
print(f'res: {res}')
print(findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]))
print(findWord(["I>F", "W>I", "S>W", "F>T"]))
print(findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]))
print(findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"]))