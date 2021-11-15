from typing import NewType


def solve(s: str, t:str) -> str:
    dct_t = dict()
    for letter in t:
        dct_t[letter] = dct_t.get(letter, 0) + 1

    unique = len(dct_t)
    remaining = unique
    left = 0
    min_sub = [0, float("inf")]
    dct_s = dict()

    #s = "ADOBECODEBANC"
    #t = "ABC"

    for right in range(len(s)):
        letter = s[right]

        if dct_t.get(letter) == None:
            continue

        dct_s[letter] = dct_s.get(letter, 0) + 1
        if dct_s[letter] == dct_t[letter]:
            remaining -= 1

        while remaining == 0 and left <= right:
            letter = s[left]
            if dct_t.get(letter) == None:
                left += 1
                continue

            if right - left < min_sub[1] - min_sub[0]:
                min_sub[0] = left
                min_sub[1] = right

            if dct_s[letter] == dct_t[letter]:
                remaining += 1
            dct_s[letter] -= 1
            left += 1

    return s[min_sub[0]:min_sub[1] + 1] if min_sub[1] != float("inf") else ""


s = "ADOBECODEBANC"
t = "ABC"
print(solve(s, t))