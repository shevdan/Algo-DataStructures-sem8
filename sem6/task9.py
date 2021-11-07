def is_pal(word: str):
    return word == word[::-1]


def solve(words: list) -> list:
    result = []
    words_dict = dict()
    for i, word in enumerate(words):
        words_dict[word] = i

    for i, word in enumerate(words):
        if word and words_dict.get("") != None and is_pal(word):
            result.extend([[words_dict[""], i], [i, words_dict[""]]])
        if word and words_dict.get(word[::-1]) != None and words_dict.get(word[::-1]) != i:
            result.append([words_dict[word[::-1]], i])
        for j in range(1, len(word)):
            if is_pal(word[0:j]) and words_dict.get(word[j:][::-1]) != None:
                result.append([words_dict[word[j:][::-1]], i])
            if is_pal(word[j:]) and words_dict.get(word[0:j][::-1]) != None:
                result.append([i, words_dict[word[0:j][::-1]]])

    return result


lst = ["abcd","dcba","lls","s","sssll"]
print(solve(lst))