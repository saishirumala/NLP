import re

def pos_tagger(sentence):
    rules = [
        (r'^\d+(\.\d+)?$', "NUM"),
        (r'.*ing$', "VBG"),
        (r'.*ed$', "VBD"),
        (r'.*ly$', "RB"),
        (r'.*(ous|ful|able)$', "JJ"),
        (r'^[A-Z][a-z]*$', "NNP")
    ]
    
    result = []
    for word in sentence.split():
        tag = "NN"
        for pattern, t in rules:
            if re.match(pattern, word, re.IGNORECASE):
                tag = t
                break
        result.append((word, tag))
    return result


sentence = "Sai is running quickly and completed 3 tasks successfully"

for w, t in pos_tagger(sentence):
    print(w, "-->", t)
