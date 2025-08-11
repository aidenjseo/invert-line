
def tokenize(line):
    tokens = []
    word = ""
    in_parens = False

    for ch in line:
        if ch == "(":
            if word:
                tokens.append(word)
                word = ""
            in_parens = True
            word += ch
        elif ch == ")":
            word += ch
            tokens.append(word)
            word = ""
            in_parens = False
        elif ch.isspace() and not in_parens:
            if word:
                tokens.append(word)
                word = ""
        else:
            word += ch

    if word:
        tokens.append(word)
    return tokens

def invert_line(line):
    tokens = tokenize(line)
    tokens.reverse()

    if tokens and tokens[0] and tokens[0][-1] in ".!?":
        tokens[0] = tokens[0][-1] + tokens[0][:-1]
    for i in range(len(tokens)):
        if tokens[i].startswith("(") and tokens[i].endswith(")"):
            inside = tokens[i][1:-1]
            inside_words = inside.split()         
            inside_words.reverse()                 
            if inside_words and inside_words[0][-1] in ".!?":
                inside_words[0] = inside_words[0][-1] + inside_words[0][:-1]
            tokens[i] = "(" + " ".join(inside_words) + ")" 
    return " ".join(tokens)


example = "(not color) that are kept in acrylic cases."
print(invert_line(example))
# ex. output: .cases acrylic in kept are that (color not)
