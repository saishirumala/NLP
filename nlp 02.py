def fsa_ends_with_ab(s):
    state = "q0"

    for ch in s:
        if state == "q0":
            state = "q1" if ch == "a" else "q0"
        elif state == "q1":
            state = "q2" if ch == "b" else "q1" if ch == "a" else "q0"
        elif state == "q2":
            state = "q1" if ch == "a" else "q0"

    return state == "q2"


strings = ["ab", "aab", "bab", "aba", "abc"]
for s in strings:
    print(s, "-> Accepted" if fsa_ends_with_ab(s) else "-> Rejected")
