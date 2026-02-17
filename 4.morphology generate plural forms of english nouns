class PluralFSM:
    def plural(self, w):
        if w.endswith("y") and len(w) > 1 and w[-2] not in "aeiou":
            return w[:-1] + "ies"
        elif w.endswith(("s", "x", "z", "ch", "sh")):
            return w + "es"
        return w + "s"

fsm = PluralFSM()
words = ["cat", "dog", "bus", "box", "baby", "boy", "brush"]

for w in words:
    print(w, "->", fsm.plural(w))
