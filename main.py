

import re
def invert_line(line):
    #split into tokens, but keep (...) as one token
    tokens = re.findall(r"\([^()]*\)|\S+", line)

    # reverse the outer sentence
    tokens.reverse()

    # if the first token ends with punctuation, move it to the front
    if tokens and tokens[0] and tokens[0][-1] in ".!?":
        tokens[0] = tokens[0][-1] + tokens[0][:-1]

    #reverse the words inside parentheses
    for i in range(len(tokens)):
        if tokens[i].startswith("(") and tokens[i].endswith(")"):
            inside = tokens[i][1:-1]               # remove ()
            inside_words = inside.split()          # split inside
            inside_words.reverse()                 # reverse inside words
            if inside_words and inside_words[0][-1] in ".!?":
                inside_words[0] = inside_words[0][-1] + inside_words[0][:-1]
            tokens[i] = "(" + " ".join(inside_words) + ")"  # reassemble
    return " ".join(tokens)


example = "(not color) that are kept in acrylic cases."
print(invert_line(example))

# ex. output: .cases acrylic in kept are that (color not)
