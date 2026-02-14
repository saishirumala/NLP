def tag(word):
    if word.endswith("ing"): return "VBG"
    if word.endswith("ed"): return "VBD"
    if word[0].isupper(): return "NNP"
    return "NN"

def tbl(sentence):
    words = sentence.split()
    tags = [tag(w) for w in words]

    for i in range(len(words)):
        if i > 0 and words[i-1] == "to" and tags[i] == "NN":
            tags[i] = "VB"
        if words[i].endswith("ly"):
            tags[i] = "RB"

    return zip(words, tags)

sentence = "Sai likes to play football quickly"

for w, t in tbl(sentence):
    print(w, "-->", t)
