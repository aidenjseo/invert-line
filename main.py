import re
def invert_line(line):
    tokens = re.findall(r"\([^()]*\)|\S+", line)
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
